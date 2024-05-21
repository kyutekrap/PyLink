import threading

from .logger import Logger


class Props(threading.local):
    _local_storage = threading.local()

    def __init__(self):
        self._local_storage.__dict__.update({
            "results": dict(),
            "next": dict(),
            "logger": Logger()
        })

    @staticmethod
    def set_results(key: str, val: str):
        Props._local_storage.results[key] = val

    @staticmethod
    def get_results(key: str):
        return Props._local_storage.results.get(key, None)

    @staticmethod
    def set_next(val: str):
        Props._local_storage.next = val

    @staticmethod
    def get_next():
        return getattr(Props._local_storage, "next", None)

    @staticmethod
    def _set_logger():
        Props._local_storage.logger = Logger()

    @staticmethod
    def get_logger():
        return getattr(Props._local_storage, "logger")

    @staticmethod
    def del_item():
        del Props._local_storage
