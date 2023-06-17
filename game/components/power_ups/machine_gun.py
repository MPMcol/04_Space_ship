import pygame

from game.utils.constants import MACHINE_GUN_TYPE, IMAGE_MACHINE_GUN
from game.components.power_ups.power_up import PowerUp

class MachineGun(PowerUp):
    def __init__(self):
        super().__init__(IMAGE_MACHINE_GUN, MACHINE_GUN_TYPE)