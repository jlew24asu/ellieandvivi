# main.py
import pygame
import sys
import traceback
from config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS
from screens.player_select import PlayerSelect
from screens.menu_screen import MenuScreen
from screens.game_screen import GameScreen
from games.spelling.spelling_game_screen import SpellingGameScreen
from utils.logger import setup_logger

class Game:
    def __init__(self):
        self.logger = setup_logger()
        self.logger.info("Initializing game...")
        
        try:
            pygame.init()
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            pygame.display.set_caption("Ellie & Vivi's Learning Adventure!")
            self.clock = pygame.time.Clock()
            self.running = True
            self.current_screen = PlayerSelect(self.screen, self.change_screen)
            self.logger.info("Game initialized successfully")
        except Exception as e:
            self.logger.error(f"Error during initialization: {str(e)}")
            self.logger.error(traceback.format_exc())
            raise

    def change_screen(self, screen_name, **kwargs):
        try:
            self.logger.info(f"Changing screen to: {screen_name} with args: {kwargs}")
            
            if screen_name == "menu":
                self.current_screen = MenuScreen(self.screen, self.change_screen, **kwargs)
            elif screen_name == "player_select":
                self.current_screen = PlayerSelect(self.screen, self.change_screen)
            elif screen_name == "game":
                game_type = kwargs.get('game_type')
                if game_type == "spelling":
                    self.current_screen = SpellingGameScreen(
                        self.screen, 
                        self.change_screen, 
                        kwargs.get('player')
                    )
                elif game_type in ["math", "science"]:
                    self.current_screen = GameScreen(
                        self.screen, 
                        self.change_screen, 
                        **kwargs
                    )
                else:
                    self.logger.warning(f"Unknown game type: {game_type}")
                    return
                    
            self.logger.info("Screen changed successfully")
        except Exception as e:
            self.logger.error(f"Error changing screen: {str(e)}")
            self.logger.error(traceback.format_exc())
            # Try to recover
            self.current_screen = PlayerSelect(self.screen, self.change_screen)

    def update(self):
        try:
            self.current_screen.update()
        except Exception as e:
            self.logger.error(f"Error in update: {str(e)}")
            self.logger.error(traceback.format_exc())

    def draw(self):
        try:
            self.current_screen.draw()
            pygame.display.flip()
        except Exception as e:
            self.logger.error(f"Error in draw: {str(e)}")
            self.logger.error(traceback.format_exc())

    def cleanup(self):
        try:
            self.logger.info("Cleaning up game resources...")
            pygame.quit()
            self.logger.info("Cleanup completed")
        except Exception as e:
            self.logger.error(f"Error during cleanup: {str(e)}")
            self.logger.error(traceback.format_exc())

    def run(self):
        self.logger.info("Starting game loop")
        try:
            while self.running:
                self.clock.tick(FPS)
                
                # Handle events
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.logger.info("Quit event received")
                        self.running = False
                        break
                    if not self.current_screen.handle_event(event):
                        self.running = False
                        break

                if not self.running:
                    break

                # Update and check if we should continue
                if not self.current_screen.update():
                    self.logger.info("Screen update signaled quit")
                    self.running = False
                    break

                # Draw
                self.current_screen.draw()
                pygame.display.flip()

        except Exception as e:
            self.logger.error(f"Error in game loop: {str(e)}")
            self.logger.error(traceback.format_exc())
        finally:
            self.cleanup()

if __name__ == "__main__":
    try:
        game = Game()
        game.run()
    except Exception as e:
        logger = setup_logger()
        logger.critical(f"Fatal error: {str(e)}")
        logger.critical(traceback.format_exc())
        sys.exit(1)