import random
import pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp(Sprite):
    def __init__(self, image, type, size = (40, 40)):
        self.image = image
        self.type = type
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(120, (SCREEN_WIDTH - 120))
        self.rect.y = random.randint((SCREEN_HEIGHT / 2), (SCREEN_HEIGHT - 80))
        self.start_time = pygame.time.get_ticks()

    def update(self, power_ups):
        if pygame.time.get_ticks() >= self.start_time + 4000:
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

