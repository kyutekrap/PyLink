from .property import create_local_storage


def GetStep(name: str):
    """
    :param name: Name of Step
    :return: None, else respective value
    """
    return create_local_storage.get_results(name)
