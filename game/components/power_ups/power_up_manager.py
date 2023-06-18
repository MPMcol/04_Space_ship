import pygame
import random

from game.components.power_ups.shield import Shield
from game.components.power_ups.machine_gun import MachineGun
from game.components.power_ups.mini_spaceship import MiniSpaceship
from game.components.power_ups.speed import Speed
from game.utils.constants import SPACESHIP_SHIELD, SHIELD_TYPE, DEFAULT_TYPE, SPEED_TYPE, MINI_SPACESHIP_TYPE, IMAGE_MINI_SPACESHIP, SOUND_SPEED, SOUND_MINI_SPACESHIP, SOUND_DEFAULT,SOUND_MACHINE_GUN, SOUND_SHIELD

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appears = pygame.time.get_ticks() + 8000
        self.duration = 6
        self.power_ups_available = {0: Shield,1: MiniSpaceship,2: Speed,3: MachineGun}
        self.default_sound = pygame.mixer.Sound(SOUND_DEFAULT)
        self.speed_sound = pygame.mixer.Sound(SOUND_SPEED)
        self.machine_gun_sound = pygame.mixer.Sound(SOUND_MACHINE_GUN)
        self.mini_spaceship_sound = pygame.mixer.Sound(SOUND_MINI_SPACESHIP)
        self.shield_sound = pygame.mixer.Sound(SOUND_SHIELD)

        self.sounds_power_ups = {"shield" : self.shield_sound, "speed" : self.speed_sound, "machine gun" : self.machine_gun_sound, "mini spaceship" : self.mini_spaceship_sound}
        
    def generate_power_up(self):
        power_up = self.power_ups_available[random.randint(0, len(self.power_ups_available) - 1)]()
        self.when_appears = pygame.time.get_ticks() + 8000
        self.power_ups.append(power_up)
        self.default_sound.play()
        

    def update(self, game):
        current_time = pygame.time.get_ticks()

        if len(self.power_ups) < 1 and current_time >= self.when_appears and game.player.has_power_up == False and game.player.power_up_type == DEFAULT_TYPE:
            self.generate_power_up()
    
        for power_up in self.power_ups:
            power_up.update(self.power_ups)
            if game.player.rect.colliderect(power_up):
                self.sounds_power_ups[power_up.type].play()
                power_up.start_time = pygame.time.get_ticks()
                game.player.power_up_type = power_up.type
                game.player.has_power_up = True
                game.player.power_up_time = power_up.start_time + (self.duration * 1000)
                self.when_appears = game.player.power_up_time + 8000
                if power_up.type == SHIELD_TYPE:
                    game.player.set_image((65,75),SPACESHIP_SHIELD)
                elif power_up.type == MINI_SPACESHIP_TYPE:
                    game.player.set_image((20,20),IMAGE_MINI_SPACESHIP)
                elif power_up.type == SPEED_TYPE:
                    game.player.increased_speed = True
                else:
                    game.player.set_image()
                self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups.clear()
        self.when_appears = pygame.time.get_ticks() + 8000
