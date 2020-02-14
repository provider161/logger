import inspect
import logging
import sys

from logging import StreamHandler


def get_logger(name="tests"):
    """
    Simple logger with stdout logging
    :param name:
    name for the logger
    :return:
    logger
    """

    # create the logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # create the log-handlers
    stdout_handler = StreamHandler(stream=sys.stdout)

    # add formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    stdout_handler.setFormatter(formatter)

    # add the handlers
    logger.addHandler(stdout_handler)

    return logger


def get_caller_name():
    """
    Returns the name of the function that called it
    """

    return inspect.currentframe().f_back.f_code.co_name
