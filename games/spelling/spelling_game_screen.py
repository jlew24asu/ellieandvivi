# games/spelling/spelling_game_screen.py
import pygame
from screens.game_screen import GameScreen
from games.spelling.ellie_spelling import EllieSpelling
from games.spelling.vivi_spelling import ViviSpelling
from config import COLORS, WINDOW_WIDTH, WINDOW_HEIGHT

class SpellingGameScreen(GameScreen):
    def __init__(self, screen, change_screen_callback, player):
        super().__init__(screen, change_screen_callback, "spelling", player)
        
        # Initialize the appropriate spelling game based on player
        self.spelling_game = (
            EllieSpelling() if player == "ELLIE" 
            else ViviSpelling()
        )
        
        # Input handling
        self.user_input = ""
        self.input_active = False
        
        # Create input box
        self.input_box = pygame.Rect(
            WINDOW_WIDTH//2 - 200,
            WINDOW_HEIGHT//2,
            400,
            50
        )
        
        # Feedback messages
        self.feedback = ""
        self.feedback_timer = 0
        self.feedback_duration = 2000  # 2 seconds in milliseconds
        
        self.logger.info(f"SpellingGameScreen initialized for player: {player}")

    def handle_event(self, event):
        """Handle pygame events."""
        super().handle_event(event)
        
        if self.is_game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Handle input box activation
                self.input_active = self.input_box.collidepoint(event.pos)
            elif event.type == pygame.KEYDOWN and self.input_active:
                self.handle_key_input(event)

    def handle_key_input(self, event):
        """Handle keyboard input for the spelling game."""
        try:
            if not self.input_active:
                return
                
            if event.key == pygame.K_RETURN:
                self.check_spelling()
            elif event.key == pygame.K_BACKSPACE:
                self.user_input = self.user_input[:-1]
            else:
                # Only allow letters
                if event.unicode.isalpha() or event.unicode.isspace():
                    self.user_input += event.unicode
        except Exception as e:
            self.logger.error(f"Error handling key input: {str(e)}")

    def check_spelling(self):
        """Check if the spelling is correct and update score."""
        try:
            if self.spelling_game.check_answer(self.user_input):
                self.add_score(1)
                self.feedback = "Correct!"
            else:
                correct_word = self.spelling_game.get_correct_word()
                self.feedback = f"Not quite! The word was: {correct_word}"
            
            self.feedback_timer = pygame.time.get_ticks()
            self.user_input = ""
            self.spelling_game.reset_challenge()
        except Exception as e:
            self.logger.error(f"Error checking spelling: {str(e)}")

    def draw_game(self):
        """Draw the active spelling game screen."""
        try:
            # Draw base game elements
            super().draw_game()
            
            # Draw the current sentence
            sentence = self.spelling_game.get_current_sentence()
            self.draw_centered_text(sentence, WINDOW_HEIGHT//2 - 100)
            
            # Draw input box
            pygame.draw.rect(self.screen, COLORS['WHITE'], self.input_box, border_radius=10)
            if self.input_active:
                pygame.draw.rect(self.screen, COLORS['PURPLE'], self.input_box, 3, border_radius=10)
            
            # Draw user input
            input_surface = self.font_medium.render(self.user_input, True, COLORS['BLACK'])
            input_rect = input_surface.get_rect(center=self.input_box.center)
            self.screen.blit(input_surface, input_rect)
            
            # Draw feedback if timer is active
            current_time = pygame.time.get_ticks()
            if current_time - self.feedback_timer < self.feedback_duration:
                feedback_color = (
                    COLORS['MINT_GREEN'] if "Correct" in self.feedback 
                    else COLORS['PINK']
                )
                self.draw_centered_text(
                    self.feedback,
                    WINDOW_HEIGHT//2 + 100,
                    color=feedback_color
                )
        except Exception as e:
            self.logger.error(f"Error drawing game: {str(e)}")

    def setup_game(self):
        """Set up a new spelling game."""
        try:
            self.spelling_game.reset_challenge()
            self.user_input = ""
            self.feedback = ""
            self.feedback_timer = 0
            self.logger.info("Spelling game setup complete")
        except Exception as e:
            self.logger.error(f"Error setting up game: {str(e)}")

    def handle_back(self):
        """Handle back button in spelling game"""
        try:
            self.logger.info(f"Handling back button press for player: {self.player}")
            self.change_screen("menu", player=self.player)
            return True
        except Exception as e:
            self.logger.error(f"Error handling back button: {str(e)}")
            return True

    def get_game_instructions(self):
        """Get spelling-specific instructions."""
        return [
            "Complete the sentence by spelling the missing word",
            "Type your answer and press Enter to submit",
            "Get 1 point for each correct spelling!",
            f"These words are chosen for {self.player.title()}'s age group"
        ]

    def add_score(self, points):
        """Add points to the score."""
        try:
            self.score += points
            self.logger.info(f"Score updated: {self.score}")
        except Exception as e:
            self.logger.error(f"Error updating score: {str(e)}")