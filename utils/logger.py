# utils/logger.py
import logging
import sys
from pathlib import Path

def setup_logger():
    """Set up logging configuration"""
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_dir / "game.log"),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    return logging.getLogger("EllieViviGame")