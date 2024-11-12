# screens/game_screen.py
import pygame
from screens.base_screen import BaseScreen
from utils.button_manager import Button
from config import COLORS, WINDOW_WIDTH, WINDOW_HEIGHT

class GameScreen(BaseScreen):
    def __init__(self, screen, change_screen_callback, game_type=None, player=None):
        """Initialize the game screen."""
        super().__init__(screen, change_screen_callback)
        self.game_type = game_type
        self.player = player
        self.score = 0
        
        # Game state
        self.is_game_active = False
        self.show_results = False
        
        # Create start button
        self.start_button = Button(
            pygame.Rect(
                (WINDOW_WIDTH - 300) // 2,
                WINDOW_HEIGHT // 2,
                300,
                80
            ),
            "Start Game",
            COLORS['MINT_GREEN'],
            self.font_medium
        )
        
        self.logger.info(f"GameScreen initialized with type: {game_type} for player: {player}")

    def update(self):
        """Update game state."""
        try:
            super().update()
            mouse_pos = pygame.mouse.get_pos()
            
            if not self.is_game_active:
                if self.start_button.update(mouse_pos):
                    self.is_game_active = True
                    self.setup_game()
        except Exception as e:
            self.logger.error(f"Error in game screen update: {str(e)}")

    def draw(self):
        """Draw the game screen."""
        try:
            self.screen.fill(COLORS['LIGHT_BLUE'])
            self.back_button.draw(self.screen)
            
            if self.is_game_active:
                self.draw_game()
            elif self.show_results:
                self.draw_results()
            else:
                self.draw_start_screen()
        except Exception as e:
            self.logger.error(f"Error in game screen draw: {str(e)}")

    def draw_start_screen(self):
        """Draw the initial game screen with start button."""
        try:
            self.draw_title(f"Welcome to {self.game_type.title()}!")
            self.start_button.draw(self.screen)
            
            # Draw instructions
            instructions = self.get_game_instructions()
            for i, line in enumerate(instructions):
                self.draw_centered_text(
                    line,
                    WINDOW_HEIGHT // 2 + 100 + (i * 40),
                    self.font_small
                )
        except Exception as e:
            self.logger.error(f"Error drawing start screen: {str(e)}")

    def draw_game(self):
        """Draw the active game screen."""
        try:
            self.draw_title(f"{self.player}'s {self.game_type.title()} Game")
            self.draw_score()
        except Exception as e:
            self.logger.error(f"Error drawing game screen: {str(e)}")

    def draw_score(self):
        """Draw the current score."""
        try:
            score_text = f"Score: {self.score}"
            score_surface = self.font_medium.render(score_text, True, COLORS['BLACK'])
            score_rect = score_surface.get_rect(topleft=(20, 80))
            self.screen.blit(score_surface, score_rect)
        except Exception as e:
            self.logger.error(f"Error drawing score: {str(e)}")

    def draw_results(self):
        """Draw the game results screen."""
        try:
            self.draw_title("Game Over!")
            self.draw_centered_text(
                f"Final Score: {self.score}",
                WINDOW_HEIGHT // 2
            )
        except Exception as e:
            self.logger.error(f"Error drawing results: {str(e)}")

    def setup_game(self):
        """Set up the game state. Should be overridden by specific game implementations."""
        pass

    def add_score(self, points):
        """Add points to the score."""
        try:
            self.score += points
            self.logger.info(f"Score updated: {self.score}")
        except Exception as e:
            self.logger.error(f"Error updating score: {str(e)}")

    def get_game_instructions(self):
        """Get game-specific instructions."""
        return ["Instructions coming soon!"]

    def handle_back(self):
        """Handle back button - return to menu"""
        try:
            self.logger.info("Handling back button in game screen")
            self.change_screen("menu", player=self.player)
            return True
        except Exception as e:
            self.logger.error(f"Error in handle_back: {str(e)}")
            return True