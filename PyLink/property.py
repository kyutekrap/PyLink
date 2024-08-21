import threading


class create_local_storage(threading.local):
    _local_storage = threading.local()

    def __init__(self):
        pass

    @staticmethod
    def set_results(key: str, val: str):
        """
        Set a value in the thread-local storage under a specific key
        :param key: Key under which the value should be stored
        :param val: Value to store in the thread-local storage
        :return:
        """
        create_local_storage._local_storage.__dict__[key] = val

    @staticmethod
    def get_results(key: str):
        """
        Retrieves a value from the thread-local storage using the provided key
        :param key: Key whose associated value needs to be retrieved
        :return:
        """
        return create_local_storage._local_storage.__dict__.get(key, None)

    @staticmethod
    def clear():
        """
        Clears all the key-value pairs stored in the thread-local storage
        :return:
        """
        create_local_storage._local_storage.__dict__.clear()
