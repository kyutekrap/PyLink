from typing import Any
from .property import create_local_storage


def Decision(x: Any, cases: dict):
    """
    Set next step in thread local storage
    :param x: Value to switch on
    :param cases: Dict of cases
    :return:
    """
    for case, value in cases.items():
        if x == value:
            create_local_storage.set_next(case)
