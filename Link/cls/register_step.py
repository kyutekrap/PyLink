import time
import logging
from typing import Any
from .property import create_local_storage
from .create_step import CreateStep
from .system import System


class register_step:
    def __init__(self, Debug=False):
        """
        Wrapper class to implement before & after methods for CreateStep
        """
        self.start_time = None
        self.debug = Debug

    def __call__(self, func):
        name = func.__name__
        def wrapper(*args, **kwargs):
            result = None
            if self.before_execute(name):
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    logging.error(e)
                    create_local_storage.set_jump(System.Die)
                self.after_execute(name, result)
            return result
        setattr(CreateStep, name, wrapper)
        return wrapper

    def before_execute(self, name: str) -> bool:
        """
        Set start time and validate step
        :return: If valid step
        """
        if self.debug:
            self.start_time = time.time() * 1000
        return False if create_local_storage.get_jump() and create_local_storage.get_jump() is not name else True

    def after_execute(self, name: str, result: Any):
        """
        End of Step exec, kill self
        """
        if self.debug:
            logging.info(f'{name} - Process Time: {time.time() * 1000 - self.start_time}')
        if result is not None:
            create_local_storage.set_results(name, result)
        del self
