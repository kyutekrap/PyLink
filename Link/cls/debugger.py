from .property import Props


class Debugger:
    @staticmethod
    def log(message: str):
        """
        :param message: Custom message to log
        :return: Printed via built-in logging module with DEBUG tag
        """
        Props.get_logger().debug(message)
