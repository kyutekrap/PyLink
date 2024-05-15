from Link.cls.property import Property


def GetStep(name: str, key: str):
    """
    :param name: Name of Step
    :param key: Key to reference
    :return: None, else respective value
    """
    step = Property.results.get(name)
    return step[key] if step else None
