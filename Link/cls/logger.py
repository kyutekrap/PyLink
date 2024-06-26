import io


class Logger:
    def __init__(self):
        self.stream = io.StringIO()

    def info(self, message: str) -> None:
        self.stream.write(f'INFO - {message}\n')

    def debug(self, message: str) -> None:
        self.stream.write(f'DEBUG - {message}\n')

    def error(self, message: str) -> None:
        self.stream.write(f'ERROR - {message}\n')

    def flush(self) -> str:
        return self.stream.getvalue()

    def exit(self) -> None:
        self.stream.close()
        del self
