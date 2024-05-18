from .logger import Logger


class Props:
    _results = None
    _next = None
    _logger = None

    def __init__(self, id: int):
        Props._results = {id: dict()}
        Props._next = {id: dict()}
        Props._logger = {id: Logger()}

    @staticmethod
    def set_results(id: int, key: str, val: str):
        Props._results[id][key] = val

    @staticmethod
    def get_results(id: int, key: str):
        return Props._results.get(id).get(key)

    @staticmethod
    def set_next(id: int, val: str):
        Props._next[id] = val

    @staticmethod
    def get_next(id: int):
        return Props._next.get(id)

    @staticmethod
    def set_logger(id: int):
        return Props._logger[id]

    @staticmethod
    def get_logger(id: int):
        return Props._logger.get(id)

    @staticmethod
    def del_item(id: int):
        Props._results.pop(id)
        Props._next.pop(id)
        Props._logger.pop(id)
