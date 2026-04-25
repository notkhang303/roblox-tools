import logging

# Configure the logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Logger:
    """
    A simple logger class to log messages in different severity levels.
    """
    
    @staticmethod
    def info(message: str) -> None:
        """
        Log an informational message.
        
        :param message: The message to log.
        """
        logging.info(message)
    
    @staticmethod
    def warning(message: str) -> None:
        """
        Log a warning message.
        
        :param message: The message to log.
        """
        logging.warning(message)
    
    @staticmethod
    def error(message: str) -> None:
        """
        Log an error message.
        
        :param message: The message to log.
        """
        logging.error(message)
    
    @staticmethod
    def debug(message: str) -> None:
        """
        Log a debug message.
        
        :param message: The message to log.
        """
        logging.debug(message)

# Example usage
if __name__ == '__main__':
    Logger.info('This is an info message')
    Logger.warning('This is a warning message')
    Logger.error('This is an error message')
    Logger.debug('This is a debug message')