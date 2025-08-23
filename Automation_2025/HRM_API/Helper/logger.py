
import logging

def get_logs(name):
    '''
    Configures and returns a logger instance for the specified name.
    This function sets up a logger that outputs messages to a file named
    "test_log.log" with a detailed format including timestamp, level, and message.
    The logging level for both the logger and the file handler is set to DEBUG,
    meaning all messages (DEBUG, INFO, WARNING, ERROR, CRITICAL) will be recorded.
    Args:
        name (str): The name of the logger to be created or retrieved.
                    It's recommended to use '__name__' for module-level loggers.
    Returns:
        logging.Logger: A configured logger instance.
    '''
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  #CEWID
    file_handler=logging.FileHandler("test_log.log")
    file_handler.setLevel(logging.DEBUG)
    logformat=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(logformat)
    logger.addHandler(file_handler)
    return logger



