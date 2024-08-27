from typing import Any
from .Flow import Flow
import logging
from .System import System


def Decision(x: Any, cases: dict):
    """
    Set next step in thread local storage
    :param x: Value to switch on
    :param cases: Dict of cases
    :return:
    """
    try:
        for case, value in cases.items():
            if eval(f"{x} {value}"):
                Flow.set_next(case)
                break

    except Exception as e:
        logging.error(f"Decision - {e}")
        Flow.set_next(System.Die)
