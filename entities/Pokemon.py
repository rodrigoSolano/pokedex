from entities.BasePokemon import BasePokemon

class Pokemon(BasePokemon):

    def __init__(self, id: int, name: str) -> None:
        self.__name__ = name
        self.__id__ = id

    def getWeaknessesByType(self):
        return []

    def getStrengthsByType(self):
        return []

    def getTypes(self):
        return []

    def getName(self):
        return self.__name__

