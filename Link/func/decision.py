from Link import Props


def Decision(params: dict):
    """
    Conditional statement
    :param params: { name of step : bool }
    """
    for key, value in params.items():
        if value:
            Props.set_next(key)
            break
