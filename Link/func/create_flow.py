from Link import Props
import inspect


def CreateFlow(name: str, flow: list, **kwargs) -> str:
    """
    Succeeds after all the Steps.
    """
    pid = id(inspect.stack()[1].function)
    debug_log = Props.get_logger(pid).flush()
    Props.get_logger(pid).exit()
    Props.del_item(pid)
    return debug_log
