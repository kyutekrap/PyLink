from typing import TypedDict, Optional
import logging
from .Flow import Flow
from .System import System
import time


class Props(TypedDict, total=False):
    """
    update - x index args to update with function return
    epoch - x times to loop function execution
    cond - condition to continue the loop
    """
    update: Optional[int]
    epoch: Optional[int]
    cond: Optional[str]


class RecursiveFlow:
    """
    Call a Flow recursively based on special props
    """
    def __init__(self, props: Props):
        self.start = time.time() * 1000
        self.props = props
        self.func = None

    def __getattr__(self, name):
        self.func = getattr(Flow, name)
        self.name = name
        self.debug = None
        return self

    def __call__(self, *args, **kwargs):
        epochs = self.props.get("epoch", 1)
        update_index = self.props.get("update", None)
        condition = self.props.get("cond", None)

        args = list(args)
        response = None

        for _ in range(epochs):
            try:
                if self.func is None:
                    raise Exception(f"Method {self.name} not found")

                response = self.func(*args, **kwargs)
                self.debug = Flow.get_debug_flag(self.func)

                if update_index is not None:
                    if 0 <= update_index < len(args):
                        args[update_index] = response
                    else:
                        raise Exception(f"Invalid update index: {update_index}")

                if condition is not None:
                    condition_result = eval(f"{response} {condition}")
                    if not condition_result:
                        break

            except Exception as e:
                logging.getLogger("PyLink").error(f"{self.name} - {e}")
                Flow.set_next(System.Die)
                break

        if response is not None:
            Flow.set_flow(self.name, response)

        if self.debug:
            logging.getLogger("PyLink").info(f"{self.name} - Total Process Time: {time.time() * 1000 - self.start}ms")

        del self
