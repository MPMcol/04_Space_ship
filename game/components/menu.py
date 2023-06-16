import pygame

from game.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH

class Menu:
    HALF_SCREEN_HEIGHT = SCREEN_HEIGHT // 2
    HALF_SCREEN_WIDTH = SCREEN_WIDTH // 2

    def __init__(self, message, screen):
        screen.fill((255, 255, 255))
        self.font = pygame.font.Font(FONT_STYLE, 30)
        self.rendered_lines = []
        self.update_message(message.splitlines())
        self.line_height = self.font.get_linesize()

    def handle_events_on_menu(self, game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False
                game.playing = False
            if event.type == pygame.KEYDOWN:
                game.run()
        
    def update(self, game):
        pygame.display.update()
        self.handle_events_on_menu(game)
    
    def draw(self, screen):      
        total_height = len(self.rendered_lines) * self.line_height
        y = (SCREEN_HEIGHT - total_height) // 2 + 50

        for i, rendered_line in enumerate(self.rendered_lines):
            rect = rendered_line.get_rect()
            rect.centerx = self.HALF_SCREEN_WIDTH
            rect.centery = y + i * self.line_height
            screen.blit(rendered_line, rect)
        self.rendered_lines = []

    def update_message(self, message_lines):
        for message in message_lines:
            self.rendered_lines.append(self.font.render(message, True, (0,0, 0)))

    def reset_screen_color(self,screen):
        screen.fill((255, 255, 255))
