# screens/menu_screen.py
import pygame
from screens.base_screen import BaseScreen
from utils.button_manager import Button
from config import COLORS, WINDOW_WIDTH, WINDOW_HEIGHT

class MenuScreen(BaseScreen):
    def __init__(self, screen, change_screen_callback, player):
        super().__init__(screen, change_screen_callback)
        self.player = player
        
        # Initialize button dimensions
        button_width = 300
        button_height = 80
        spacing = 20
        start_y = 250

        # Create game buttons
        self.game_buttons = []
        button_configs = [
            ("Spelling Fun!", COLORS['PINK'], "spelling"),
            ("Math Magic!", COLORS['MINT_GREEN'], "math"),
            ("Science Safari!", COLORS['PURPLE'], "science")
        ]

        for i, (text, color, game_type) in enumerate(button_configs):
            button = Button(
                pygame.Rect(
                    (WINDOW_WIDTH - button_width) // 2,
                    start_y + i * (button_height + spacing),
                    button_width,
                    button_height
                ),
                text,
                color,
                self.font_medium
            )
            self.game_buttons.append((button, game_type))

    def handle_event(self, event):
        """Handle events specific to menu screen."""
        super().handle_event(event)
        return True

    def update(self):
        """Update menu screen state."""
        if not super().update():
            return False
            
        mouse_pos = pygame.mouse.get_pos()
        
        for button, game_type in self.game_buttons:
            if button.update(mouse_pos):
                self.change_screen("game", game_type=game_type, player=self.player)
                
        return True

    def handle_back(self):
        """Handle back button in menu screen."""
        self.change_screen("player_select")
        return True

    def draw(self):
        """Draw the menu screen."""
        self.screen.fill(COLORS['LIGHT_BLUE'])
        self.back_button.draw(self.screen)
        self.draw_title(f"{self.player}'s Learning Adventure!")
        
        for button, _ in self.game_buttons:
            button.draw(self.screen)

    def handle_back(self):
        """Handle back button in menu screen"""
        try:
            self.change_screen("player_select")
            return True
        except Exception as e:
            self.logger.error(f"Error in menu back: {str(e)}")
            return True