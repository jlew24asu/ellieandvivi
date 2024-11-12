# utils/button_manager.py
import pygame
from config import COLORS

class Button:
    """
    A class to handle interactive buttons in the game.
    Manages drawing, hover states, and click detection.
    """
    def __init__(self, rect, text, color, font=None, border_radius=15, hover_color=COLORS['WHITE']):
        """
        Initialize a button.
        
        Args:
            rect: Pygame Rect defining button position and size
            text: Button text
            color: Button background color
            font: Font to use for text (defaults to system font if None)
            border_radius: Radius for rounded corners
            hover_color: Color of border when button is hovered
        """
        self.rect = rect
        self.text = text
        self.color = color
        self.font = font or pygame.font.Font(None, 48)
        self.border_radius = border_radius
        self.hover_color = hover_color
        self.is_hovered = False
        self.click_sound = None
        self.was_pressed = False

    def draw(self, screen):
        pygame.draw.rect(
            screen, 
            self.color, 
            self.rect, 
            border_radius=self.border_radius
        )
        
        if self.is_hovered:
            pygame.draw.rect(
                screen,
                self.hover_color,
                self.rect,
                3,
                border_radius=self.border_radius
            )
        
        text_surface = self.font.render(self.text, True, COLORS['BLACK'])
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def update(self, mouse_pos):
        previous_hover = self.is_hovered
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
        mouse_pressed = pygame.mouse.get_pressed()[0]
        
        if self.is_hovered and mouse_pressed and not self.was_pressed:
            self.was_pressed = True
            return True
            
        if not mouse_pressed:
            self.was_pressed = False
            
        return False

class ButtonGroup:
    """
    Manages a group of related buttons.
    Useful for menu screens or button layouts.
    """
    def __init__(self):
        self.buttons = []

    def add(self, button):
        self.buttons.append(button)

    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)

    def update(self, mouse_pos):
        clicked = []
        for i, button in enumerate(self.buttons):
            if button.update(mouse_pos):
                clicked.append(i)
        return clicked

    def arrange_vertical(self, start_y, spacing):
        current_y = start_y
        for button in self.buttons:
            button.rect.y = current_y
            current_y += button.rect.height + spacing