import pygame
from entity import Entity

class Background(Entity):
    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        super().__init__(name, surf, rect)

    def move(self) -> None:
        """
        Se quiser fazer um efeito de 'parallax' ou algo do tipo, implemente aqui.
        Por enquanto, deixamos estático (sem movimento).
        """
        pass
