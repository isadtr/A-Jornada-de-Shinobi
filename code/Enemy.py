import pygame
from entity import Entity

class Enemy(Entity):
    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        super().__init__(name, surf, rect)

    def move(self) -> None:
        """
        Exemplo de movimentação do inimigo.
        Aqui, movemos o inimigo para a esquerda.
        """
        self.rect.x -= 1  # Ajuste a velocidade conforme necessário
