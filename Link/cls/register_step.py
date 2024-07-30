import time
import logging
from typing import Any

from .property import create_local_storage
from .create_step import CreateStep
from .system import System


class register_step:
    def __init__(self):
        """
        Wrapper class to implement before & after methods for CreateStep
        """
        self.start_time = None

    def __call__(self, func):
        def wrapper(name: str, params: dict, Debug=False, Persist=False):
            result = None

            if self.before_execute(name, Debug):

                try:
                    result = func(name, params, Debug=Debug, Persist=Persist)
                except Exception as e:
                    if Debug:
                        logging.error(e)
                        create_local_storage.set_jump(System.Die)

                self.after_execute(name, result, Debug, Persist)

            return result

        setattr(CreateStep, func.__name__, wrapper)
        return wrapper

    def before_execute(self, name: str, Debug: bool) -> bool:
        """
        :return: Validate step
        """
        if Debug:
            self.start_time = time.time() * 1000
        return False if create_local_storage.get_jump() and create_local_storage.get_jump() is not name else True

    def after_execute(self, name: str, result: Any, Debug: bool, Persist: bool):
        """
        End of Step exec, kill self
        """
        if Debug:
            logging.info(f'{name} - Process Time: {time.time() * 1000 - self.start_time}')
        if Persist:
            create_local_storage.set_results(name, result)
        del self
