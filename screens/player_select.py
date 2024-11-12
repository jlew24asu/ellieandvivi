# screens/player_select.py
import pygame
from screens.base_screen import BaseScreen
from utils.button_manager import Button
from config import COLORS, WINDOW_WIDTH, WINDOW_HEIGHT

class PlayerSelect(BaseScreen):
    def __init__(self, screen, change_screen_callback):
        super().__init__(screen, change_screen_callback)
        
        # Initialize button dimensions
        button_width = 300
        button_height = 80
        spacing = 40
        start_y = WINDOW_HEIGHT // 2 - button_height - spacing // 2

        # Create Ellie's button
        self.ellie_button = Button(
            pygame.Rect(
                (WINDOW_WIDTH - button_width) // 2,
                start_y,
                button_width,
                button_height
            ),
            "Ellie",
            COLORS['PINK'],
            self.font_medium
        )

        # Create Vivi's button
        self.vivi_button = Button(
            pygame.Rect(
                (WINDOW_WIDTH - button_width) // 2,
                start_y + button_height + spacing,
                button_width,
                button_height
            ),
            "Vivi",
            COLORS['MINT_GREEN'],
            self.font_medium
        )

    def handle_event(self, event):
        """Handle events specific to player select screen."""
        super().handle_event(event)
        return True

    def update(self):
        """Update player select screen state."""
        if not super().update():
            return False
            
        mouse_pos = pygame.mouse.get_pos()
        
        if self.ellie_button.update(mouse_pos):
            self.change_screen("menu", player="ELLIE")
        elif self.vivi_button.update(mouse_pos):
            self.change_screen("menu", player="VIVI")
            
        return True

    def handle_back(self):
        """Handle back button in player select screen."""
        return False  # Signal to quit game

    def draw(self):
        """Draw the player select screen."""
        self.screen.fill(COLORS['LIGHT_BLUE'])
        self.back_button.draw(self.screen)
        self.draw_title("Who's Playing Today?")
        self.ellie_button.draw(self.screen)
        self.vivi_button.draw(self.screen)

    def handle_back(self):
        """Handle back button in player select screen"""
        try:
            return False  # Signal to quit game
        except Exception as e:
            self.logger.error(f"Error in player select back: {str(e)}")
            return False