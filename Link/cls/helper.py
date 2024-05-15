import functools
import time

from .property import Property


class Helper:
    def __init__(self, *args, **kwargs):
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
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None

            self.debug = kwargs.get('Debug')
            self.persist = kwargs.get('Persist')

            if self.before_execute(*args, **kwargs):

                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    if self.debug:
                        Property.logger.error(f"{str(e)}\n")

                self.after_execute(result, *args, **kwargs)

            return result

        return wrapper

    def before_execute(self, *args, **kwargs) -> bool:
        """
        :return: Validates conditional skipping of Step
        """
        exec = False if Property.next and Property.next is not args[0] else True
        if self.debug:
            self.start_time = time.time() * 1000
        return exec

    def after_execute(self, result, *args, **kwargs):
        """
        End of Step exec, kills self
        """
        if self.start_time:
            Property.logger.info(f'{args[0]} - Process Time: {str(time.time() * 1000 - self.start_time)}')
        if self.persist:
            Property.results[args[0]] = result
        del self
