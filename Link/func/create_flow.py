from Link.cls.property import Property


def CreateFlow(name: str, flow: list, **kwargs) -> str:
    """
    Succeeds after all the Steps
    :param name: Name of Flow
    :param flow: All the Steps
    :param kwargs:
    :return: Log output
    """
    global Property

    debug_log = Property.logger.flush()
    Property.logger.exit()
    del Property
    return debug_log
