import pygame

WIN_WIDTH = 570
WIN_HEIGHT = 320

COLOR_DARK = (20, 8, 31)
COLOR_LIGHT = (255,255,255)
COLOR_SELECT = (20, 8, 31)

MENU_OPTION = (
    'NEW GAME 1P',
    'NEW GAME 2P - COOPERATIVE',
    'SCORE',
    'EXIT'
)

ENTITY_SPEED = {
    'level01_0': 0,
    'level01_1': 0.66,
    'level01_2': 1.33,
    'level01_3': 2,
    'level01_4': 2.66,
    'shinobi': 3,
    'player2': 3,
    'enemy1': 1,
    'enemy2': 2,
}

SPAWN_TIME = 4000



PLAYER_KEY_UP = {'shinobi': pygame.K_UP,'player2': pygame.K_w}
PLAYER_KEY_DOWN = {'shinobi': pygame.K_DOWN, 'player2': pygame.K_s}
PLAYER_KEY_LEFT = {'shinobi': pygame.K_LEFT, 'player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'shinobi': pygame.K_RIGHT, 'player2': pygame.K_d}
PLAYER_KEY_ATTACK = {'shinobi': pygame.K_RCTRL, 'player2': pygame.K_LCTRL}

EVENT_ENEMY = pygame.USEREVENT + 1