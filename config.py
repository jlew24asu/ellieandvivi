# config.py

import pygame
from pathlib import Path

# Colors and Display Settings
WINDOW_WIDTH = 1024
WINDOW_HEIGHT = 768
FPS = 60

COLORS = {
    'PINK': (255, 192, 203),
    'PURPLE': (147, 112, 219),
    'LIGHT_BLUE': (173, 216, 230),
    'MINT_GREEN': (152, 255, 152),
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0)
}

# File paths
BASE_DIR = Path(__file__).parent
SAVE_DIR = BASE_DIR / "saves"
SAVE_DIR.mkdir(exist_ok=True)
