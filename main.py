import pygame
import sys
from enum import Enum
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

# Colors
COLORS = {
    'PINK': (255, 192, 203),
    'PURPLE': (147, 112, 219),
    'LIGHT_BLUE': (173, 216, 230),
    'MINT_GREEN': (152, 255, 152),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0)
}

class GameState(Enum):
    MENU = 1
    SPELLING = 2
    MATH = 3
    SCIENCE = 4

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Ellie & Vivi's Learning Adventure!")
        self.clock = pygame.time.Clock()
        self.state = GameState.MENU
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
        
    def draw_button(self, text, rect, color, hover=False):
        pygame.draw.rect(self.screen, color, rect, border_radius=15)
        if hover:
            pygame.draw.rect(self.screen, COLORS['WHITE'], rect, 3, border_radius=15)
        text_surface = self.font_medium.render(text, True, COLORS['BLACK'])
        text_rect = text_surface.get_rect(center=rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_menu(self):
        self.screen.fill(COLORS['LIGHT_BLUE'])
        
        # Title
        title = self.font_large.render("Ellie & Vivi's Learning Adventure!", True, COLORS['PURPLE'])
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 100))
        self.screen.blit(title, title_rect)

        # Menu buttons
        button_width = 300
        button_height = 80
        spacing = 20
        start_y = 250

        buttons = [
            ("Spelling Fun!", COLORS['PINK'], GameState.SPELLING),
            ("Math Magic!", COLORS['MINT_GREEN'], GameState.MATH),
            ("Science Safari!", COLORS['PURPLE'], GameState.SCIENCE)
        ]

        for i, (text, color, state) in enumerate(buttons):
            button_rect = pygame.Rect(
                (WINDOW_WIDTH - button_width) // 2,
                start_y + i * (button_height + spacing),
                button_width,
                button_height
            )
            
            mouse_pos = pygame.mouse.get_pos()
            hover = button_rect.collidepoint(mouse_pos)
            self.draw_button(text, button_rect, color, hover)
            
            if hover and pygame.mouse.get_pressed()[0]:
                self.state = state

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if self.state == GameState.MENU:
                self.draw_menu()
            elif self.state == GameState.SPELLING:
                self.screen.fill(COLORS['PINK'])
                # Placeholder for spelling game
                text = self.font_large.render("Spelling Game Coming Soon!", True, COLORS['WHITE'])
                self.screen.blit(text, text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)))
            elif self.state == GameState.MATH:
                self.screen.fill(COLORS['MINT_GREEN'])
                # Placeholder for math game
                text = self.font_large.render("Math Game Coming Soon!", True, COLORS['WHITE'])
                self.screen.blit(text, text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)))
            elif self.state == GameState.SCIENCE:
                self.screen.fill(COLORS['PURPLE'])
                # Placeholder for science game
                text = self.font_large.render("Science Game Coming Soon!", True, COLORS['WHITE'])
                self.screen.blit(text, text.get_rect(center=(WINDOW_WIDTH//2, WINDOW_HEIGHT//2)))

            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()