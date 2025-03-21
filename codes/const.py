import pygame

WIN_WIDTH = 570
WIN_HEIGHT = 320

C_DARK = (20, 8, 31)
C_LIGHT = (255, 255, 255)
C_SELECT = (20, 8, 31)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)


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
    'shinobiAttack': 1,
    'player2': 3,
    'player2Attack': 1,
    'enemy1': 1,
    'enemy1Attack': 3,
    'enemy2': 2,
    'enemy2Attack': 3,
}

SPAWN_TIME = 4000



PLAYER_KEY_UP = {'shinobi': pygame.K_UP,'player2': pygame.K_w}
PLAYER_KEY_DOWN = {'shinobi': pygame.K_DOWN, 'player2': pygame.K_s}
PLAYER_KEY_LEFT = {'shinobi': pygame.K_LEFT, 'player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'shinobi': pygame.K_RIGHT, 'player2': pygame.K_d}
PLAYER_KEY_ATTACK = {'shinobi': pygame.K_SPACE, 'player2': pygame.K_LCTRL}


EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_HEALTH = {
    'level01_0':999,
    'level01_1': 999,
    'level01_2': 999,
    'level01_3': 999,
    'level01_4': 999,
    'shinobi': 300,
    'shinobiAttack': 1,
    'player2': 300,
    'player2Attack': 1,
    'enemy1': 50,
    'enemy1Attack': 1,
    'enemy2': 60,
    'enemy2Attack': 1,
}


ENTITY_SHOT_DELAY = {
    'shinobi': 20,
    'player2': 15,
    'enemy1': 60,
    'enemy2': 85,

}

ENTITY_DAMAGE = {
    'level01_0': 0,
    'level01_1': 0,
    'level01_2': 0,
    'level01_3': 0,
    'level01_4': 0,
    'shinobi': 1,
    'shinobiAttack': 25,
    'player2': 1,
    'player2Attack': 20,
    'enemy1': 1,
    'enemy1Attack': 20,
    'enemy2': 1,
    'enemy2Attack': 15,
}

ENTITY_SCORE = {
    'level01_0': 0,
    'level01_1': 0,
    'level01_2': 0,
    'level01_3': 0,
    'level01_4': 0,
    'shinobi': 0,
    'shinobiAttack': 0,
    'player2': 0,
    'player2Attack': 0,
    'enemy1': 100,
    'enemy1Attack': 0,
    'enemy2': 125,
    'enemy2Attack': 0,
}