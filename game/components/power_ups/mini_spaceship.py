from game.components.power_ups.power_up import PowerUp
from game.utils.constants import IMAGE_MINI_SPACESHIP, MINI_SPACESHIP_TYPE

class MiniSpaceship(PowerUp):
    def __init__(self):
        super().__init__(IMAGE_MINI_SPACESHIP, MINI_SPACESHIP_TYPE, (35, 35))