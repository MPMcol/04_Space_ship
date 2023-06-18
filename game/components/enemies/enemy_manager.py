import random
import pygame

from game.components.enemies.enemy import Enemy
from game.utils.constants import SHIELD_TYPE, SCREEN_WIDTH

class EnemyManager:
    def __init__(self):
        self.enemies = []


    def update(self, game):
        self.add_enemy()
        for enemy in self.enemies:
            enemy.update(self.enemies, game)
            if enemy.rect.colliderect(game.player.rect):
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    pygame.time.delay(1500)
                    game.death_count.update()
                    game.calculate_highest_score()
                break
        

    def add_enemy(self):
        enemy_type = random.randint(1, 5)

        if enemy_type == 1:
            enemy = Enemy()
        else:
            enemy = Enemy(speed_x=random.randint(5,7), speed_y=random.randint(5,7), move_x_for=[50, SCREEN_WIDTH - 60])

        if len(self.enemies) < 5:
            self.enemies.append(enemy)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def reset(self):
        self.enemies = []