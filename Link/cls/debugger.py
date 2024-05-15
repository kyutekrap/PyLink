from .property import Property


class Debugger:
    @staticmethod
    def log(message: str):
        """
        :param message: Custom message to log
        :return: Printed via built-in logging module with DEBUG tag
        """
        Property.logger.debug(message)
