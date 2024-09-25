from _flows import *
from _steps import *
from PyLink import *
import logging

logger = logging.getLogger()
if logger.hasHandlers():
    logger.handlers.clear()

logger = logging.getLogger("PyLink")
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("app.log", mode="w")
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


if __name__ == '__main__':
    Flow.InsertUsers()
