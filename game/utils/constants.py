import pygame
import os

# Global Constants
TITLE = "Spaceships Game"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))

SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
IMAGE_MACHINE_GUN = pygame.image.load(os.path.join(IMG_DIR, 'Other/machineGun.png'))
IMAGE_SPEED = pygame.image.load(os.path.join(IMG_DIR, 'Other/speed.png'))
IMAGE_MINI_SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, 'Other/miniSpaceship.png'))

GIF_EXPLOTE = pygame.image.load(os.path.join(IMG_DIR, 'Other/explote.gif'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = 'default'
SHIELD_TYPE = 'shield'
MACHINE_GUN_TYPE = 'machine gun'
SPEED_TYPE = 'speed'
MINI_SPACESHIP_TYPE = 'mini spaceship'

SPACESHIP = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship.png"))
SPACESHIP_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Spaceship/spaceship_shield.png"))
BULLET = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_1.png"))

BULLET_ENEMY = pygame.image.load(os.path.join(IMG_DIR, "Bullet/bullet_2.png"))
ENEMIES = (pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_1.png")), pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_2.png")), pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_3.png")),pygame.image.load(os.path.join(IMG_DIR, "Enemy/enemy_4.png")))

FONT_STYLE = 'freesansbold.ttf'

BULLET_SOUND = os.path.join(IMG_DIR, "other/sonido_disparo_enemigo.mp3")
ENVIROMENT_SOUND = os.path.join(IMG_DIR, "other/sonido_ambiente.mp3")

SOUND_SHIELD = os.path.join(IMG_DIR, "other/sonido_power_up_escudo.mp3")
SOUND_MACHINE_GUN = os.path.join(IMG_DIR, "other/sonido_power_up_machine_gun.mp3")
SOUND_SPEED = os.path.join(IMG_DIR, "other/sonido_power_up_velocidad.mp3")
SOUND_MINI_SPACESHIP = os.path.join(IMG_DIR, "other/sonido_power_up_mini_nave.mp3")
SOUND_DEFAULT = os.path.join(IMG_DIR, "other/sonido_normalidad.mp3")
SOUND_GAME_OVER = os.path.join(IMG_DIR, "other/sound_game_over.mp3")