import time
import logging
from typing import Any
from .property import create_local_storage


class Step:
    def __init__(self, Debug=False):
        """
        Wrapper class to implement before & after methods for CreateStep
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
                except Exception as e:
                    logging.error(e)
                self.after_execute(name, result)
            return result

        setattr(Step, name, wrapper)
        return wrapper

    def before_execute(self, name: str) -> bool:
        """
        Set start time
        Validate step
        :return: If valid
        """
        if self.debug:
            self.start_time = time.time() * 1000
        next_step = create_local_storage.get_next()
        return next_step == name if next_step is not None else True

    def after_execute(self, name: str, result: Any):
        """
        End of Step exec, kill self
        """
        if self.debug:
            logging.info(f'{name} - Process Time: {time.time() * 1000 - self.start_time}')
        if result is not None:
            create_local_storage.set_results(name, result)
        del self