import sys
import random

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from codes.Enemy import Enemy
from codes.Entity import Entity
from codes.EntityFactory import EntityFactory
from codes.EntityMediator import EntityMediator
from codes.Player import Player
from codes.const import WIN_HEIGHT, C_LIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME, C_GREEN, C_CYAN, WIN_WIDTH


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level01_'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        self.timeout = 20000  # 20 seconds
        self.enemies_defeated = 0 # contador de inimigos derrotados

        if game_mode in MENU_OPTION[1]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))

        pygame.time.set_timer(EVENT_ENEMY,SPAWN_TIME)

    def display_objective_screen(self):
            # Carrega a imagem que será animada
            overlay_image = pygame.image.load('../asset/samurai-menu.png').convert_alpha()
            # Inicia a posição da imagem fora da tela (à esquerda)
            overlay_rect = overlay_image.get_rect(center = (-overlay_image.get_width() // 2, WIN_HEIGHT // 1.5))

            # Define a mensagem do objetivo
            objective_text = "Objetivo: Elimine 15 inimigos"
            text_size = 20
            text_color = (255, 255, 255)
            text_pos = (WIN_WIDTH // 6, WIN_HEIGHT // 2)

            # Velocidade de animação (pixels por frame)
            slide_speed = 10

            # ANIMAÇÃO DE ENTRADA: deslizar da esquerda até o centro
            while overlay_rect.centerx < WIN_WIDTH // 1.2:
                self.window.fill((20, 0, 20))
                overlay_rect.centerx += slide_speed
                self.window.blit(overlay_image, overlay_rect)
                self.level_text(text_size, objective_text, text_color, text_pos)
                pygame.display.flip()
                pygame.time.delay(30)

            # Mantém a tela com o objetivo por 5 segundos
            t0 = pygame.time.get_ticks()
            while pygame.time.get_ticks() - t0 < 3000:
                self.window.fill((20, 0, 20))
                self.window.blit(overlay_image, overlay_rect)
                self.level_text(text_size, objective_text, text_color, text_pos)
                pygame.display.flip()
                pygame.time.delay(30)

            # ANIMAÇÃO DE SAÍDA: deslizar para a direita até sair da tela
            while overlay_rect.left < WIN_WIDTH:
                self.window.fill((20, 0, 20))
                overlay_rect.centerx += slide_speed
                self.window.blit(overlay_image, overlay_rect)
                self.level_text(text_size, objective_text, text_color, text_pos)
                pygame.display.flip()
                pygame.time.delay(30)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
            text_font = pygame.font.SysFont(name = "Lucida Sans Typewriter", size = text_size)
            text_surf = text_font.render(text, True, text_color).convert_alpha()
            text_rect = text_surf.get_rect(center = text_pos)
            self.window.blit(text_surf, text_rect)

    def run(self):

        self.display_objective_screen()

        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            # Verifica se o jogador está pressionando as teclas de movimento
            keys = pygame.key.get_pressed()

            # Define a direção do movimento: 1 para direita, -1 para esquerda, 0 para parado
            direcao = 0
            if keys[pygame.K_RIGHT]:
                direcao = 1
            elif keys[pygame.K_LEFT]:
                direcao = -1
            # mover = keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]

            for ent in self.entity_list:
                self.window.blit(source = ent.surf, dest = ent.rect)
                # Se for um background (nome que inicia com "level01_"), move-o somente se 'mover' for True
                if ent.name.startswith("level01_"):
                    ent.move(direcao)
                else:
                    ent.move()


                if isinstance(ent, (Player, Enemy)):
                    attack = ent.attack()
                    if attack is not None:
                        self.entity_list.append(attack)
                if ent.name == 'shinobi':   # HUD
                    self.level_text(text_size = 14, text = f'Player1 - Health: {ent.health} | Score: {ent.score}',
                                    text_color = C_GREEN,
                                    text_pos = (10, 20))
                if ent.name == 'player2':
                    self.level_text(text_size = 14, text = f'Player2 - Health: {ent.health} | Score: {ent.score}',
                                    text_color = C_CYAN,
                                    text_pos = (280, 20))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))



            # printed text
            self.level_text(text_size = 14, text = f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s',
                            text_color = C_LIGHT, text_pos = (10, 5))
            self.level_text(text_size = 14, text = f'fps: {clock.get_fps() :.0f}', text_color = C_LIGHT,
                            text_pos = (250, 5))
            self.level_text(text_size = 14, text = f'entidades: {len(self.entity_list)}', text_color = C_LIGHT,
                            text_pos = (400, 5))
            # self.level_text(text_size = 14, text = f'fps: {clock.get_fps() : 0f}', text_color = COLOR_LIGHT,
            #                 text_pos = (10, WIN_HEIGHT - 35))
            # self.level_text(text_size = 14, text = f'entidades: {len(self.entity_list)}', text_color = COLOR_LIGHT,
            #                 text_pos = (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            # Colisões e saúde
            EntityMediator.verify_collision(entity_list=self.entity_list)
            defeated = EntityMediator.verify_health(entity_list=self.entity_list)
            self.enemies_defeated += defeated

            # Verifica se o player está morto (considerando que Player é uma instância de Player)
            players_alive = [ent for ent in self.entity_list if isinstance(ent, Player)]
            if not players_alive:
                # Exibe a mensagem centralizada de "Você morreu" ou "Game Over"
                self.level_text(
                    text_size = 40,
                    text = "Game Over",
                    text_color = (255, 0, 0),  # vermelho, por exemplo
                    text_pos = (WIN_WIDTH // 4, WIN_HEIGHT // 2)
                )
                pygame.display.flip()
                pygame.time.delay(3000)  # pausa por 3 segundos para o jogador ver a mensagem
                return  # encerra o nível ou redireciona para o menu

            if self.enemies_defeated >= 15:
                self.level_text(text_size = 40, text="Objetivo Concluído!",text_color=(20,0,50),text_pos=(WIN_WIDTH // 8, WIN_HEIGHT // 2))
                pygame.display.flip()
                pygame.time.delay(3000)
                return


        pass


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name = "Lucida Sans Typewriter", size = text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left = text_pos[0], top = text_pos[1])
        self.window.blit(source = text_surf, dest = text_rect)
