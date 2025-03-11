from codes.Background import Background
from codes.const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level01_':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'level01_{i}', position))
                    list_bg.append(Background(f'level01_{i}', (WIN_WIDTH, position[1])))  # Corrigido
                    #list_bg.append(Background(f'level01_{i}', position(WIN_WIDTH, 0)))
                return list_bg

    #
    # def get_entity(self, entity_type: str):
    #     """
    #     Cria uma instância de Entity (ou suas subclasses) baseada em 'entity_type'.
    #     """
    #     if entity_type == "player":
    #         # Exemplo de Player com um retângulo 50x50, começando em (100,100)
    #         surf = pygame.Surface((50, 50))
    #         surf.fill((0, 255, 0))  # Cor verde para identificar
    #         rect = surf.get_rect(topleft=(100, 100))
    #         return Player("Player", surf, rect)
    #
    #     elif entity_type == "enemy":
    #         # Exemplo de Enemy com um retângulo 50x50, começando em (300,100)
    #         surf = pygame.Surface((50, 50))
    #         surf.fill((255, 0, 0))  # Cor vermelha para identificar
    #         rect = surf.get_rect(topleft=(300, 100))
    #         return Enemy("Enemy", surf, rect)
    #
    #     elif entity_type == "background":
    #         # Exemplo de Background (tamanho da tela 800x600)
    #         surf = pygame.Surface((800, 600))
    #         surf.fill((50, 50, 50))  # Cinza para identificar
    #         rect = surf.get_rect(topleft=(0, 0))
    #         return Background("Background", surf, rect)
    #
    #     else:
    #         raise ValueError(f"Tipo de entidade '{entity_type}' não reconhecido.")
