import io
import logging


class Logger:
    def __init__(self):
        """
        Log to StringIO
        """
        self.stream = io.StringIO()
        self.handler = logging.StreamHandler(self.stream)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        self.handler.setFormatter(formatter)

        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)
        self.log.addHandler(self.handler)

    def info(self, message: str) -> None:
        self.log.info(message)

    def debug(self, message: str) -> None:
        self.log.debug(message)

    def error(self, message: str) -> None:
        self.log.error(message)

    def flush(self) -> str:
        self.handler.flush()
        return self.stream.getvalue()

    def exit(self) -> None:
        self.log.removeHandler(self.handler)
        self.handler.close()
        del self
        