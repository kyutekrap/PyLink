from Link import Props
import inspect


def Decision(params: dict):
    """
    Conditional statement
    :param params: { name of step : bool }
    """
    pid = id(inspect.stack()[1].function)
    for key, value in params.items():
        if value:
            Props.set_next(pid, key)
            break
