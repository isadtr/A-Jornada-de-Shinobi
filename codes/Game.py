import pygame

from codes.Level import Level
from codes.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from codes.Menu import Menu


class Game:
    def __init__(self):
        self.window = None
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            # sets the menu options
            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()
            elif menu_return == MENU_OPTION[3]:  # exit
                pygame.quit()
                quit()
            else:
                pass



