# screens/base_screen.py
import pygame
from utils.button_manager import Button
from config import COLORS, WINDOW_WIDTH
from utils.logger import setup_logger

class BaseScreen:
    def __init__(self, screen, change_screen_callback):
        self.screen = screen
        self.change_screen = change_screen_callback
        self.font_large = pygame.font.Font(None, 74)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
        self.logger = setup_logger()  # Initialize logger in base class
        
        # Create back button
        self.back_button = Button(
            pygame.Rect(20, 20, 100, 40),
            "Back",
            COLORS['WHITE'],
            self.font_small,
            border_radius=8
        )

    def handle_event(self, event):
        """Base event handler that all screens should implement or inherit."""
        return True

    def update(self):
        """Update screen state."""
        try:
            mouse_pos = pygame.mouse.get_pos()
            if self.back_button.update(mouse_pos):
                return self.handle_back()
            return True
        except Exception as e:
            self.logger.error(f"Error in base update: {str(e)}")
            return True

    def draw(self):
        """Base draw method that all screens must implement."""
        raise NotImplementedError("Screens must implement draw method")

    def handle_back(self):
        """Default back behavior - should be overridden."""
        return True

    def draw_title(self, text):
        title = self.font_large.render(text, True, COLORS['PURPLE'])
        title_rect = title.get_rect(center=(WINDOW_WIDTH//2, 100))
        self.screen.blit(title, title_rect)

    def draw_centered_text(self, text, y_position, font=None, color=COLORS['BLACK']):
        font = font or self.font_medium
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH//2, y_position))
        self.screen.blit(text_surface, text_rect)

    def create_button(self, text, y_position, width=300, height=80, color=COLORS['MINT_GREEN']):
        """
        Create a centered button at a specific vertical position.
        
        Args:
            text: Button text
            y_position: Vertical position for the button
            width: Button width (default 300)
            height: Button height (default 80)
            color: Button color (default MINT_GREEN)
            
        Returns:
            Button: New button instance
        """
        return Button(
            pygame.Rect(
                (WINDOW_WIDTH - width) // 2,
                y_position,
                width,
                height
            ),
            text,
            color,
            self.font_medium
        )