from game.components.enemies.enemy import Enemy
import random

class EnemyManager:
    def __init__(self):
        self.enemies = []


    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)

    def add_enemy(self):
        enemy_type = random.randint(1, 2)

        if enemy_type == 1:
            enemy = Enemy()
        else:
            enemy = Enemy(speed_x=6, speed_y=3, move_x_for=[50, 100])

        if len(self.enemies) < 1:
            self.enemies.append(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)