import inspect
import logging


def custom_logger1():

    log_name = inspect.stack()[1][3]

    logger = logging.getLogger(log_name)

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("./Logs/log.log", mode='a')

    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger
