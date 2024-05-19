from Link import Props
import inspect


def GetStep(name: str, key: str):
    """
    :param name: Name of Step
    :param key: Key to reference
    :return: None, else respective value
    """
    pid = id(inspect.stack()[1].function)
    step = Props.get_results(pid, name)
    if step:
        return step.get(key, None)
