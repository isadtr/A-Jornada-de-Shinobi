import pygame.key

from codes.Entity import Entity
from codes.PlayerShot import PlayerShot
from codes.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH, PLAYER_KEY_UP, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, \
    PLAYER_KEY_RIGHT, PLAYER_KEY_ATTACK, ENTITY_SHOT_DELAY


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        # Atributos para o pulo vertical
        self.is_jumping = False
        self.jump_vel = 0
        self.jump_speed = 6  # Velocidade inicial do pulo
        self.gravity = 0.5  # Valor da gravidade

    # def update(self):
    #     pass

    def move(self):  # movimento do personagem com setas
        pressed_key = pygame.key.get_pressed()

        # Inicia o pulo se a tecla UP for pressionada e o personagem estiver "no chão"
        if pressed_key[PLAYER_KEY_UP[self.name]]:
            self.is_jumping = True
            self.jump_vel = -self.jump_speed  # Valor negativo para subir

        if self.is_jumping:
            # Atualiza a posição vertical aplicando a velocidade de pulo e a gravidade
            self.rect.centery += self.jump_vel
            self.jump_vel += self.gravity  # Aumenta a velocidade (em direção à queda)
            # Se atingir o "chão", encerra o pulo
            if self.rect.bottom >= WIN_HEIGHT:
                self.rect.bottom = WIN_HEIGHT
                self.is_jumping = False


        # if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
        #     self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        pass

    def attack(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_ATTACK[self.name]]:
                return PlayerShot(name=f'{self.name}Attack', position=(self.rect.centerx,self.rect.centery))




