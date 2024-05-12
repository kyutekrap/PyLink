import argparse
import sys
import logging
import functools
import time
import threading


# ===== Thread-safe Globals (START)
tls = threading.local()

tls.results = dict()
tls.next = None
# ===== Thread-safe Globals (END)

# ===== Logging Setup (START)
logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
# ===== Logging Setup (END)


class Debugger:
    @staticmethod
    def log(message: str):
        """
        :param message: Custom message to log
        :return: Printed via built-in logging module with DEBUG tag
        """
        logging.debug(message)


class Helper:
    def __init__(self, *args, **kwargs):
        """
        Wrapper class to implement before & after methods for CreateStep static methods
        :param args: *
        :param kwargs: Available [Debug: bool, Persist: bool]
        Debug - logs processing time for a Step
        Persist - saves Step returns in tls.result
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

                result = func(*args, **kwargs)
                self.after_execute(result, *args, **kwargs)

            return result

        return wrapper

    def before_execute(self, *args, **kwargs) -> bool:
        """
        :return: Validates conditional skipping of Step
        """
        exec = False if tls.next and tls.next is not args[0] else True
        if self.debug:
            self.start_time = time.time() * 1000
        return exec

    def after_execute(self, result, *args, **kwargs):
        """
        End of Step exec, kills self
        """
        if self.start_time:
            logging.info(f'{args[0]} - Process Time: {str(time.time() * 1000 - self.start_time)}')
        if self.persist:
            tls.results[args[0]] = result
        del self


class CreateStep:
    @staticmethod
    @Helper()
    def ExampleCustomMethod(name: str, params: dict, **kwargs) -> dict | None:
        """
        :param name: Name of Step (*Unique str recommended)
        :param params: Any type of dict. (*Conventional writing of keys with `$` recommended)
        :param kwargs: Available [Debug, Persist] as aforementioned
        :return: None, else Key-Value dict to save on Persist=True
        """
        list_of_tuples = list((a, b) for a, b in list(zip(*params.get("$values").values())))
        list_of_tuples = str(list_of_tuples)[1:-1]
        sql_stmt = f'INSERT INTO {params.get("$table")} {tuple(params.get("$values").keys())} VALUES {list_of_tuples}'
        # ** sql_stmt->prepare->execute **
        return {"affected_rows": 2}


def GetStep(name: str, key: str):
    """
    :param name: Name of Step
    :param key: Key to reference
    :return: None, else respective value
    """
    step = tls.results.get(name)
    return step[key] if step else None


def CreateFlow(name: str, flow: list, **kwargs) -> None:
    """
    Succeeds after all the Steps. Kills locals.
    """
    del tls.results
    del tls.next


def Decision(params: dict):
    """
    Conditional statement
    :param params: { name of step : bool }
    """
    for key, value in params.items():
        if value:
            tls.next = key
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("code", type=str)
    args = parser.parse_args()

    sys.exit(exec(args.code))
