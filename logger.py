import logging
from logging.handlers import RotatingFileHandler

def setup_logger(log_file, max_bytes=10485760, backup_count=5):
    """
    Sets up a rotating logger.
    
    Args:
        log_file (str): The log file path.
        max_bytes (int): Maximum file size before rotation.
        backup_count (int): Number of backup files to keep.
    """  
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)  
    handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Example usage
if __name__ == '__main__':
    log = setup_logger('app.log')
    log.info('Logger setup complete.')