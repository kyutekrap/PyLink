import time
import logging
import threading
from typing import Any, Callable
from queue import Queue


class Flow:
    _local_storage = threading.local()

    def __init__(self, Debug=False, Thread=False, Wait=False):
        """
        Initialize Flow instance.
        :param Debug: If True, enables debug mode.
        :param Thread: If True, run the flow in a separate thread.
        :param Wait: If True, wait for the thread to complete.
        """
        self.start_time = None
        self.debug = Debug
        self.run_in_thread = Thread
        self.wait_for_thread = Wait
        self.next = None

    def _init_local_storage(self):
        """
        Initialize thread-local storage for this instance.
        If storage already exists, it is reused.
        """
        if not hasattr(Flow._local_storage, "_initialized"):
            self._initialize_storage()
        else:
            self.next = Flow._local_storage._next

    def _initialize_storage(self):
        """
        Initialize the local storage attributes.
        """
        Flow._local_storage._step = {}
        Flow._local_storage._next = None
        Flow._local_storage._flow = {}
        Flow._local_storage._initialized = True
        Flow._local_storage._counter = 0

    def __call__(self, func):
        """
        Implement before and after execution.
        Register function to Flow.
        :param func: Decorated function.
        :return: Function after decoration.
        """
        name = func.__name__

        def wrapper(*args, **kwargs):
            if self.run_in_thread:
                result_queue = Queue()
                thread = threading.Thread(target=self._run_flow, args=(func, name, result_queue, args, kwargs))
                thread.start()

                if self.wait_for_thread:
                    thread.join()
                    return result_queue.get()

                return None
            else:
                return self._run_flow(func, name, None, args, kwargs)

        wrapper._debug = self.debug
        setattr(Flow, name, wrapper)
        return wrapper

    def _run_flow(self, func, name, result_queue, args, kwargs) -> Any:
        """
        Run the flow and manage the before and after execution steps.
        :param func: The function to run as the flow.
        :param name: The name of the flow function.
        :param result_queue: The queue to store the result (used in threading).
        :param args: The positional arguments to pass to the function.
        :param kwargs: The keyword arguments to pass to the function.
        """
        result = None

        if self.before_execute(name):
            result = func(*args, **kwargs)
            self.after_execute(name, result, result_queue)

        return result

    def before_execute(self, name: str) -> bool:
        """
        Set start time for execution.
        Create local storage.
        Validate flow.
        :return: If valid
        """
        self.start_time = time.time() * 1000

        self._init_local_storage()
        Flow._local_storage._counter += 1

        is_valid = self.next == name and type(self.next) is type(name) if self.next is not None else True
        if is_valid:
            Flow.set_next()
        return is_valid

    def after_execute(self, name: str, result: Any, result_queue: Queue) -> None:
        """
        End of Flow execution, clear storage if this is the main Flow, clean up.
        :param name: Name of the executed function.
        :param result: Result of the executed function.
        """
        if result is not None:
            Flow.set_flow(name, result)

        if result_queue is not None:
            result_queue.put(result)

        Flow._local_storage._counter -= 1

        if Flow._local_storage._counter == 0:
            Flow._local_storage._step.clear()
            Flow._local_storage._next = None
            Flow._local_storage._flow.clear()
            del Flow._local_storage._initialized
            del Flow._local_storage._counter

        if self.debug:
            logging.info(f"{name} - Process Time: {time.time() * 1000 - self.start_time}ms")

    @staticmethod
    def set_next(case: str = None):
        """
        Set the next value in the thread-local storage.
        :param case: The value to set.
        """
        Flow._local_storage._next = case

    @staticmethod
    def get_next() -> Any:
        """
        Get the next value from the thread-local storage.
        :return: The next value.
        """
        return Flow._local_storage._next

    @staticmethod
    def set_step(key: str, val: str):
        """
        Set a value in the thread-local storage under a specific key.
        :param key: Key under which the value should be stored.
        :param val: Value to store.
        """
        Flow._local_storage._step[key] = val

    @staticmethod
    def get_step(key: str) -> Any:
        """
        Get a value from the thread-local storage using a specific key.
        :param key: Key whose associated value needs to be retrieved.
        :return: The value associated with the key.
        """
        return Flow._local_storage._step.get(key, None)

    @staticmethod
    def set_flow(key: str, val: str):
        """
        Set a value in the thread-local storage under a specific key.
        :param key: Key under which the value should be stored.
        :param val: Value to store.
        """
        Flow._local_storage._flow[key] = val

    @staticmethod
    def get_flow(key: str) -> Any:
        """
        Get a value from the thread-local storage using a specific key.
        :param key: Key whose associated value needs to be retrieved.
        :return: The value associated with the key.
        """
        return Flow._local_storage._flow.get(key, None)

    @staticmethod
    def get_debug_flag(func: Callable) -> bool:
        return getattr(func, "_debug", False)
