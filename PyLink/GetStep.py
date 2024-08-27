from .Flow import Flow


def GetStep(name: str):
    """
    :param name: Name of Step
    :return: None, else respective value
    """
    return Flow.get_step(name)
