import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from codes.const import COLOR_DARK, MENU_OPTION, COLOR_LIGHT


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('../asset/orig.png')
        self.rect = self.surf.get_rect(left = 0, top = 0)

        # Carregar a imagem PNG extra (por cima do fundo)
        self.overlay_surf = pygame.image.load('../asset/samurai-menu.png')  # Caminho da nova imagem
        self.overlay_rect = self.overlay_surf.get_rect(center = (400, 240))  # Ajuste de posição

    def run(self):
        pygame.mixer_music.load('../Asset/Blackmoor Ninjas.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source = self.surf, dest = self.rect)

            self.menu_text(30, "A JORNADA", COLOR_DARK, (150, 70))
            self.menu_text(30, "DE SHINOBI", COLOR_DARK, (150, 110))

            # Desenhar a imagem extra sobre o fundo
            self.window.blit(self.overlay_surf, self.overlay_rect)

            for i in range(len(MENU_OPTION)):
                self.menu_text(16,MENU_OPTION[i], COLOR_LIGHT, (150, 160 + 30 * i))



            pygame.display.flip()

            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: pygame.font.Font = pygame.font.SysFont(name = "Lucida Sans Typewriter", size = text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color)
        text_rect: pygame.Rect = text_surf.get_rect(center = text_center_pos)
        self.window.blit(text_surf, text_rect)
