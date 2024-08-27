from typing import Any
from .Flow import Flow


def Decision(x: Any, cases: dict):
    """
    Set next step in thread local storage
    :param x: Value to switch on
    :param cases: Dict of cases
    :return:
    """
    for case, value in cases.items():
        if x == value:
            Flow.set_next(case)
