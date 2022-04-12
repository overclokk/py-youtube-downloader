from typing import List


class Menu:
    options = {}

    def __init__(self) -> None:
        pass

    def getOption(self) -> List:
        return self.options
    
    def addOption(self, key, func) -> None:
        self.options.update(key, func)

    def rmvOption(self, key) -> None:
        del self.options[key]