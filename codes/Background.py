from codes.Entity import Entity
from codes.const import WIN_WIDTH, ENTITY_SPEED


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    # def move(self):
    #     self.rect.centerx -= ENTITY_SPEED[self.name]  #image speed
    #     if self.rect.right <= 0:
    #         self.rect.left = WIN_WIDTH
    # def move(self, mover):
    #     if mover:
    #         self.rect.centerx -= ENTITY_SPEED[self.name]
    #         if self.rect.right <= 0:
    #             self.rect.left = WIN_WIDTH
    def move(self, direcao=0):
        """Move o background na direção indicada (-1 = esquerda, 1 = direita)."""
        self.rect.centerx -= ENTITY_SPEED[self.name] * direcao

        # Reseta a posição quando sai da tela
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
        elif self.rect.left >= WIN_WIDTH:
            self.rect.right = 0
