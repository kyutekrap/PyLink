from .property import Props
import inspect


class Debugger:
    @staticmethod
    def log(message: str):
        """
        :param message: Custom message to log
        :return: Printed via built-in logging module with DEBUG tag
        """
        Props.get_logger(id(inspect.stack()[1].function)).debug(message)
