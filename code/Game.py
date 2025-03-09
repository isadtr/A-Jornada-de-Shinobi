import pygame

from code.Menu import Menu


# import pygame
# from level import Level
#
# class Game:
#     def __init__(self, window: pygame.Surface):
#         """
#         Gerencia o loop principal do jogo.
#         :param window: Superfície principal do jogo (janela).
#         """
#         self.window = window
#         self.level = Level(self.window)
#         self.level.create()  # Cria as entidades do nível
#
#     def run(self) -> None:
#         """
#         Loop principal do jogo.
#         """
#         clock = pygame.time.Clock()
#         running = True
#
#         while running:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     running = False
#
#             # Preenche a tela com uma cor (ex: preto)
#             self.window.fill((0, 0, 0))
#
#             # Atualiza e desenha o nível
#             self.level.run()
#
#             # Atualiza a tela
#             pygame.display.flip()
#             clock.tick(60)
#
#         pygame.quit()

class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         pygame.quit()  # close window
            #         quit()
