from game.components.power_ups.power_up import PowerUp
from game.utils.constants import IMAGE_SPEED, SPEED_TYPE

class Speed(PowerUp):
    def __init__(self):
        super().__init__(IMAGE_SPEED, SPEED_TYPE)