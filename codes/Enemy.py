import pygame

from codes.EnemyShot import EnemyShot
from codes.Entity import Entity
from codes.const import ENTITY_SPEED, WIN_WIDTH, ENTITY_SHOT_DELAY


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]


    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # image speed
    def attack(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name = f'{self.name}Attack', position = (self.rect.centerx, self.rect.centery))
