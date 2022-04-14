# from typing import Callable

class Menu:
    def __init__(self, options) -> None:
        self._options = options

    def getOption(self) -> dict:
        return self._options
    
    # TODO: fix and add those methods
    # def addOption(self, key: int, func: Callable) -> None:
    #     self._options.update(key, func)

    # def rmvOption(self, key: int) -> None:
    #     del self._options[key]