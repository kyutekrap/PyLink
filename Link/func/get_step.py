from Link import Props


def GetStep(name: str):
    """
    :param name: Name of Step
    :return: None, else respective value
    """
    return Props.get_results(name)
