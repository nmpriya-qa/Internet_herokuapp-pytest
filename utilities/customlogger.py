import inspect
import logging

def custom_logger():
    # 1.) This is used to get the  class / method name from where this customLogger method is called
    log_name = inspect.stack()[1][3]

    # 2.) Create the logging object and pass the logName in it
    logger = logging.getLogger(log_name)

    # 3.) Set the Log level
    logger.setLevel(logging.DEBUG)

    # 4.) Create the fileHandler to save the logs in the file
    file_handler = logging.FileHandler("./Logs/log.log", mode='a')

    # 5.) Set the logLevel for file_handler
    file_handler.setLevel(logging.DEBUG)

    # 6.) Create the formatter in which format do you like to save the logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s : %(message)s',
                                  datefmt='%d/%m/%y %I:%M:%S %p %A')

    # 7.) Set the formatter to file_handler
    file_handler.setFormatter(formatter)

    # 8.) Add file handler to logging
    logger.addHandler(file_handler)

    #  9.) Finally return the logging object

    return logger