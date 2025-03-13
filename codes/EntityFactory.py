from codes.Background import Background
from codes.Enemy import Enemy
from codes.Player import Player
from codes.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level01_':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'level01_{i}', position))
                    list_bg.append(Background(f'level01_{i}', (WIN_WIDTH, position[1])))  # Corrigido
                return list_bg
            case 'Player1':
                return Player('shinobi',(10, WIN_HEIGHT / 1.3))
            case 'Player2':
                return Player('player2', (30, WIN_HEIGHT / 1.32))
            case 'Enemy1':
                return Enemy('enemy1', (WIN_WIDTH, WIN_HEIGHT / 1.25))
            case 'Enemy2':
                return Enemy('enemy2', (WIN_WIDTH, WIN_HEIGHT / 1.22))

