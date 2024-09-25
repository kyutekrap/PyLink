import time
import logging
from .Flow import Flow
from .System import System
from typing import Callable


class Step:
    def __init__(self, Debug=False):
        """
        Class variables
        """
        self.start_time = None
        self.debug = Debug

    def __call__(self, func):
        """
        Implement before and after execution
        Register function to Step
        :param func: Decorated function
        :return: Function after decoration
        """
        name = func.__name__

        def wrapper(*args, **kwargs):
            result = None
            if self.before_execute(name):
                try:
                    result = func(*args, **kwargs)
                    if result is not None:
                        Flow.set_step(name, result)
                    self.after_execute(name)

                except Exception as e:
                    logging.getLogger("PyLink").error(f"{name} - {e}")
                    Flow.set_next(System.Die)

            return result

        wrapper._debug = self.debug
        setattr(Step, name, wrapper)
        return wrapper

    def before_execute(self, name: str) -> bool:
        """
        Set time
        Validate step
        :return: If valid
        """
        self.start_time = time.time() * 1000
        next_step = Flow.get_next()
        is_valid = next_step == name and type(next_step) is type(name) if next_step is not None else True
        if is_valid:
            Flow.set_next()
        return is_valid

    def after_execute(self, name: str):
        """
        End of Step exec, kill self
        """
        if self.debug:
            logging.getLogger("PyLink").info(f"{name} - Process Time: {time.time() * 1000 - self.start_time}ms")
        del self

    @staticmethod
    def get_debug_flag(func: Callable) -> bool:
        return getattr(func, "_debug", False)
