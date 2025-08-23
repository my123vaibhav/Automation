import logging
import os
from datetime import datetime

# Log file path
LOG_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")


def get_logger(name: str = "pytest-playwright"):
    """Return a configured logger instance."""

    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # File Handler
        file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
        file_handler.setLevel(logging.DEBUG)

        # Formatter
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
