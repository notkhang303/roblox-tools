import logging
from logging.handlers import RotatingFileHandler


def setup_logger(log_file='app.log', log_level=logging.INFO, max_bytes=5 * 1024 * 1024, backup_count=3):  
    """Setup a logger with rotation capabilities."""
    logger = logging.getLogger(__name__)
    logger.setLevel(log_level)

    # Create a file handler for logging
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Clear any existing handlers, then add the new handler
    if logger.hasHandlers():
        logger.handlers.clear()
    logger.addHandler(handler)

    return logger


# Example usage
if __name__ == '__main__':
    logger = setup_logger()
    logger.info('Logger is set up with rotation.')
