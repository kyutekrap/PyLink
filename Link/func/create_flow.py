from Link import Property


def CreateFlow(name: str, flow: list, **kwargs) -> str:
    """
    Succeeds after all the Steps. Kills globals.
    """
    global Property

    debug_log = Property.logger.flush()
    Property.logger.exit()
    del Property
    return debug_log
