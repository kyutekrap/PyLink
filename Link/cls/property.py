import threading

from .logger import Logger


class Property:
    results = dict()
    next = None
    logger = Logger()
