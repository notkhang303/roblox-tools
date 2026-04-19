import logging
from logging.handlers import RotatingFileHandler

# Set up the logger configuration

def setup_logger(log_file='app.log', max_bytes=5*1024*1024, backup_count=3):
    """Sets up a rotating logger."""
    # Create a logger object
    logger = logging.getLogger('roblox_tools_logger')
    logger.setLevel(logging.DEBUG)  # Set the logging level to DEBUG
    
    # Create a handler for rotating log files
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    handler.setLevel(logging.DEBUG)  # Set the handler level to DEBUG
    
    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    # Add the handler to the logger
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    logger = setup_logger()  # Call the setup function
    logger.debug('This is a debug message.')
    logger.info('Logger is set up correctly.')
    logger.warning('This is a warning message.')
    logger.error('An error has occurred!')
    logger.critical('Critical issue!'),
