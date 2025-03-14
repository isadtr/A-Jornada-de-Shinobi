from codes.Enemy import Enemy
from codes.EnemyShot import EnemyShot
from codes.Entity import Entity
from codes.PlayerShot import PlayerShot
from codes.const import WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent:Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                ent.health = 0
        if isinstance(ent, PlayerShot):
            if ent.rect.left >= WIN_WIDTH:
                ent.health = 0
        if isinstance(ent, EnemyShot):
            if ent.rect.left <= 0:
                ent.health = 0



    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)