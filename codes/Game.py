import pygame

from codes.const import WIN_WIDTH, WIN_HEIGHT
from codes.Menu import Menu


class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass




