from .property import create_local_storage


class register_flow:
    def __init__(self):
        pass

    def __call__(self, func):
        def wrapper(*args, **kwargs):

            create_local_storage()

            return func(*args, **kwargs)
        return wrapper
