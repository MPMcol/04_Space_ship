import pygame

from game.utils.constants import BG, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE, ICON, FONT_STYLE, ENVIROMENT_SOUND, SOUND_DEFAULT, SOUND_GAME_OVER
from game.components.spaceship import Spaceship
from game.components.enemies.enemy_manager import EnemyManager
from game.components.bullets.bullet_manager import BulletManager
from game.components.menu import Menu
from game.components.counter import Counter
from game.components.power_ups.power_up_manager import PowerUpManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.game_over_sound = pygame.mixer.Sound(SOUND_GAME_OVER)
        self.enviroment_sound = pygame.mixer.Sound(ENVIROMENT_SOUND)

        self.playing = False
        self.game_speed = 10

        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = EnemyManager()
        self.bullet_manager = BulletManager()
        self.running = False
        self.menu = Menu('Press any key to start', self.screen)
        

        self.score = Counter()
        self.death_count = Counter()
        self.highest_score = Counter()

        self.power_up_manager = PowerUpManager()


    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.game_over_sound.stop()
        self.enviroment_sound.set_volume(0.1)
        self.enviroment_sound.play(-1)
        self.reset()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset(self):
        self.enemy_manager.reset()
        self.score.reset()
        self.player.reset()
        self.bullet_manager.reset()
        self.power_up_manager.reset()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                pygame.quit()
                quit()

        

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)
        

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))

        self.draw_background()
        self.player.draw(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        
        pygame.display.update()
        pygame.display.flip()

    def draw_power_up_time(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000)
            if time_to_show >= 0:
                message = f'{self.player.power_up_type.capitalize()} is enabled for {time_to_show} in seconds'
                font = pygame.font.Font(FONT_STYLE, 20)
                text = font.render(message, True, (255,255,255))
                text_rect = text.get_rect()
                text_rect.center = (300, 50)
                self.screen.blit(text, text_rect)
            else:
                default_sound = pygame.mixer.Sound(SOUND_DEFAULT)
                default_sound.play()
                self.player.has_power_up = False
                self.player.power_up_type = DEFAULT_TYPE
                self.player.power_up_time = 0
                self.player.set_image()
                self.power_up_manager.reset()
                self.player.increased_speed = False



    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg-image_height))

        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg-image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_menu(self):
        self.menu.reset_screen_color(self.screen)
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count.count == 0:
            self.enviroment_sound.stop()
            self.game_over_sound.set_volume(0.1)
            self.game_over_sound.play(-1)
            self.menu.draw(self.screen)
        else:
            self.enviroment_sound.stop()
            self.game_over_sound.set_volume(0.1)
            self.game_over_sound.play(-1)
            message = f'Game over. Press any key to restart.\nYour score: {self.score.count}\nHighest score: {self.highest_score.count}\nTotal deaths: {self.death_count.count}'            
            self.menu.update_message(message.splitlines())
            self.menu.draw(self.screen)

        icon = pygame.transform.scale(ICON, (80,120))
        self.screen.blit(icon, (half_screen_width - 50, half_screen_height - 150))
        self.menu.update(self)

    def calculate_highest_score(self):
        if self.score.count > self.highest_score.count:
            self.highest_score.set_count(self.score.count)
