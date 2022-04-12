from typing import Callable


class Menu:
    options = {}

    def __init__(self) -> None:
        pass

    def getOption(self) -> dict:
        return self.options
    
    def addOption(self, key: int, func: Callable) -> None:
        self.options.update(key, func)

    def rmvOption(self, key: int) -> None:
        del self.options[key]