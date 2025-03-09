import pygame

class Entity:
    def __init__(self, name: str, surf: pygame.Surface, rect: pygame.Rect):
        """
        Classe base (superclasse) para todos os tipos de entidades do jogo.
        :param name: Nome da entidade (Ex: "Player", "Enemy", etc.)
        :param surf: Superfície (imagem) da entidade
        :param rect: Retângulo que define posição e tamanho da entidade
        """
        self.name = name
        self.surf = surf
        self.rect = rect

    def move(self) -> None:
        """
        Método genérico para mover a entidade.
        Classes filhas podem sobrescrevê-lo com comportamentos específicos.
        """
        pass
