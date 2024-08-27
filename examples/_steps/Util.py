import random
from PyLink import Step


class Util:
    @staticmethod
    @Step(Debug=True)
    def GenerateId(x: int) -> int:
        return x * random.randrange(1, 10)
