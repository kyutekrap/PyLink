import threading


class create_local_storage(threading.local):
    _local_storage = threading.local()

    def __init__(self):
        """
        Create local storage
        Persist results and flag steps
        Access property statically
        """
        create_local_storage._local_storage.__dict__.update({
            "_results": dict(),
            "_jump": dict()
        })

    @staticmethod
    def set_results(key: str, val: str):
        create_local_storage._local_storage._results[key] = val

    @staticmethod
    def get_results(key: str):
        return create_local_storage._local_storage._results.get(key, None)

    @staticmethod
    def set_jump(val: str):
        create_local_storage._local_storage.set_jump = val

    @staticmethod
    def get_jump():
        return getattr(create_local_storage._local_storage, "_jump", None)

    @staticmethod
    def clear():
        create_local_storage._local_storage.__dict__.clear()
