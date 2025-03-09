import pygame
from entity import Entity

class Player(Entity):
    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        super().__init__(name, surf, rect)

    def move(self) -> None:
        """
        Exemplo simples de movimentação do Player.
        Aqui, apenas movemos o player para a direita lentamente.
        """
        self.rect.x += 2  # Ajuste a velocidade conforme necessário
