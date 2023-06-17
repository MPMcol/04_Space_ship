import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.machine_gun import MachineGun
from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE, IMAGE_MACHINE_GUN, MACHINE_GUN_TYPE, DEFAULT_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = random.randint(2000, 5000)
        self.duration = 10
        self.power_ups_available = {SHIELD_TYPE: Shield(), MACHINE_GUN_TYPE: MachineGun()}


    def generate_power_up(self):
        power_up = self.power_ups_available[random.choice(list(self.power_ups_available.keys()))]
        print(power_up.type)
        self.when_appears += random.randint(2000, 5000)
        self.power_ups.append(power_up)
        print(len(self.power_ups))

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) < 1 and current_time >= self.when_appears and game.player.has_power_up == False and game.player.power_up_type == DEFAULT_TYPE:
            self.generate_power_up()

        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups, game)
            if game.player.rect.colliderect(power_up):
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (self.duration * 1000)
                if power_up.type == SHIELD_TYPE:
                    game.player.set_image((65,75),SPACESHIP_SHIELD)
                else:
                    game.player.set_image()
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups.clear()
        self.when_appears = random.randint(2000, 5000)
