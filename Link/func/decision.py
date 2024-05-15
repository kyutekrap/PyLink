from Link.cls.property import Property


def Decision(params: dict):
    """
    Conditional statement
    :param params: { name of step : bool }
    """
    for key, value in params.items():
        if value:
            Property.next = key
            break
