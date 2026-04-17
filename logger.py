import logging
from logging.handlers import RotatingFileHandler

def setup_logger(logger_name, log_file, level=logging.INFO):
    """Sets up a logger with rotation."""
    # Create a logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Create a file handler with rotation
    handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5)
    handler.setLevel(level)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    if not logger.handlers:
        logger.addHandler(handler)

    return logger

# Example usage:
# logger = setup_logger('my_logger', 'app.log')
# logger.info('This is an info message')