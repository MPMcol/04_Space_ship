import pygame
from game.utils.constants import SHIELD_TYPE, MACHINE_GUN_TYPE, BULLET_SOUND, SOUND_GAME_OVER

class BulletManager:
    def __init__(self):
        self.bullets = []
        self.enemy_bullets = []
        self.bullet_sound = pygame.mixer.Sound(BULLET_SOUND)
        self.bullet_sound.set_volume(0.4)

    def update(self, game):
        for bullet in self.bullets:
            bullet.update(self.bullets)

            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect) and bullet.owner != 'enemy':
                    game.enemy_manager.enemies.remove(enemy)
                    self.bullets.remove(bullet)
                    game.score.update()

        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)

            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                self.enemy_bullets.remove(bullet)
                if game.player.power_up_type != SHIELD_TYPE:
                    game.playing = False
                    pygame.time.delay(1500)
                    game.death_count.update()
                    game.calculate_highest_score()
                break

    def draw(self, screen):
        for bullet in self.enemy_bullets:
            bullet.draw(screen)
        for bullet in self.bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet, power_up_type):
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 2:
            self.bullet_sound.play()
            self.enemy_bullets.append(bullet)
        elif bullet.owner == 'player' and len(self.bullets) < 2:
            self.bullet_sound.play()
            self.bullets.append(bullet)
        elif bullet.owner == 'player' and power_up_type == MACHINE_GUN_TYPE and len(self.bullets) < 10:
            self.bullet_sound.play()
            self.bullets.append(bullet)

    def reset(self):
        self.bullets = []
        self.enemy_bullets = []