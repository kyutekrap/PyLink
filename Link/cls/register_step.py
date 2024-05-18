import time

from .property import Property
from .create_step import CreateStep


class register_step:
    def __init__(self):
        """
        Wrapper class to implement before & after methods for CreateStep static methods
        :param args: *
        :param kwargs: Available [Debug: bool, Persist: bool]
        Debug - logs processing time for a Step
        Persist - saves Step returns in Property.results
        """
        self.persist = None
        self.debug = None
        self.start_time = None

    def __call__(self, func):
        def wrapper(name: str, params: dict, **kwargs):
            result = None

            self.debug = kwargs.get('Debug')
            self.persist = kwargs.get('Persist')

            if self.before_execute(name):

                try:
                    result = func(name, params, **kwargs)
                except Exception as e:
                    if self.debug:
                        Property.logger.error(f"{str(e)}\n")

                self.after_execute(name, result)

            return result

        setattr(CreateStep, func.__name__, wrapper)
        return wrapper

    def before_execute(self, name) -> bool:
        """
        :return: Validates conditional skipping of Step
        """
        exec = False if Property.next and Property.next is not name else True
        if self.debug:
            self.start_time = time.time() * 1000
        return exec

    def after_execute(self, name, result):
        """
        End of Step exec, kills self
        """
        if self.start_time:
            Property.logger.info(f'{name} - Process Time: {str(time.time() * 1000 - self.start_time)}')
        if self.persist:
            Property.results[name] = result
        del self
