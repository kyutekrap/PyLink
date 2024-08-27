from .Flow import Flow


def GetFlow(name: str):
    """
    :param name: Name of Flow
    :return: None, else respective value
    """
    return Flow.get_flow(name)
