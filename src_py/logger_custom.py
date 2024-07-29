import logging
import os


def setup_logger(name, level=logging.DEBUG, logs_dir="./src_py/logs"):
    """
    The `setup_logger` function creates a custom logger with both console and file handlers, setting the
    log level and formatting for each.

    :param name: The `name` parameter in the `setup_logger` function is used to specify the name of the
    logger instance that will be created. This name is typically used to identify the logger when
    logging messages. In the provided code snippet, the `name` parameter is passed as "app" when
    creating the
    :param level: The `level` parameter in the `setup_logger` function specifies the logging level for
    the logger. In this case, the default logging level is set to `logging.DEBUG`, which means that all
    log messages of severity DEBUG and higher (DEBUG, INFO, WARNING, ERROR, CRITICAL) will be
    :param logs_dir: The `logs_dir` parameter in the `setup_logger` function is the directory where log
    files will be stored. By default, it is set to `"./src_py/logs"`, which means that log files will be
    stored in a directory named `logs` inside the `src_py` directory, defaults to ./src_py/logs
    (optional)
    :return: The `setup_logger` function returns a custom logger instance named "app" with specified
    logging level, handlers, formatters, and log file path.
    """
    logs_dir = "src_py/logs"
    log_file_path = os.path.join(logs_dir, "app.log")

    # Check if the logs directory exists, and create it if it doesn't
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)
        with open(log_file_path, "a") as log_file:
            pass

    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(log_file_path)
    c_handler.setLevel(level)
    f_handler.setLevel(level)

    # Create formatters and add them to the handlers
    log_format = "%(asctime)s : %(name)s - %(levelname)s - %(message)s (Line: %(lineno)d [%(filename)s], Module: [%(module)s] Function: [%(funcName)s])"
    # log_format2 = '%(asctime)s : %(name)s - %(levelname)s - %(message)s'
    c_format = logging.Formatter(log_format)
    f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger


# Create a logger instance
app_logger = setup_logger("app")
