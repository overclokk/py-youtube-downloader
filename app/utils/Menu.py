class Menu:
    options = {}

    def __init__(self) -> None:
        pass

    def getOption(self) -> dict:
        return self.options
    
    def addOption(self, key, func) -> None:
        self.options.update(key, func)

    def rmvOption(self, key) -> None:
        del self.options[key]