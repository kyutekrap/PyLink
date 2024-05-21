from Link import Props


def GetStep(name: str, key: str):
    """
    :param name: Name of Step
    :param key: Key to reference
    :return: None, else respective value
    """
    step = Props.get_results(name)
    if step:
        return step.get(key, None)
