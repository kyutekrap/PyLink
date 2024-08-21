from .property import create_local_storage
import time
import logging


class Flow:
    def __init__(self, Debug=False):
        """
        Wrapper class to implement before & after methods for CreateFlow
        """
        self.start_time = None
        self.debug = Debug

    def __call__(self, func):
        """
        Implement before and after execution
        Register function to Flow
        :param func: Decorated function
        :return: Function after decoration
        """
        name = func.__name__

        def wrapper(*args, **kwargs):
            self.before_execute()
            create_local_storage()
            result = func(*args, **kwargs)
            self.after_execute(name)
            return result

        setattr(Flow, name, wrapper)
        return wrapper

    def before_execute(self) -> None:
        """
        Set start time
        """
        if self.debug:
            self.start_time = time.time() * 1000

    def after_execute(self, name: str) -> None:
        """
        End of Flow exec, clear storage, kill self
        """
        if self.debug:
            logging.info(f'{name} - Process Time: {time.time() * 1000 - self.start_time}')
        create_local_storage.clear()
        del self
