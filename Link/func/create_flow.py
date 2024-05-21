from Link import Props


def CreateFlow(name: str, flow: list, **kwargs) -> str:
    """
    Succeeds after all the Steps.
    """
    debug_log = Props.get_logger().flush()
    Props.get_logger().exit()
    Props.del_item()
    return debug_log
