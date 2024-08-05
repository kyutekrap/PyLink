from .property import create_local_storage
import time
import logging


class register_flow:
    def __init__(self, Debug=False):
        """
        Wrapper class to implement before & after methods for CreateFlow
        """
        self.start_time = None
        self.debug = Debug

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            self.before_execute()
            create_local_storage()
            result = func(*args, **kwargs)
            self.after_execute(func.__name__)
            return result
        return wrapper

    def before_execute(self) -> None:
        """
        Set start time
        """
        if self.debug:
            self.start_time = time.time() * 1000

    def after_execute(self, name: str) -> None:
        """
        End of Flow exec, kill self
        """
        if self.debug:
            logging.info(f'{name} - Process Time: {time.time() * 1000 - self.start_time}')
        del self
