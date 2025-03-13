import pygame
from codes.Entity import Entity
from codes.const import ENTITY_SPEED, WIN_WIDTH


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # image speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
