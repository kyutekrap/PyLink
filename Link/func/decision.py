from Link import create_local_storage


def Decision(params: dict):
    """
    Conditional statement
    :param params: { name of step : bool }
    """
    for key, value in params.items():
        if value:
            create_local_storage.set_jump(key)
            break
