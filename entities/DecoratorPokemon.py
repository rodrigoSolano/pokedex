from entities.BasePokemon import BasePokemon

class DecoratorPokemon(BasePokemon):

    def __init__(self,pokemon):
        self.__pokemon__ = pokemon

    def getWeaknessesByType(self):
        return self.__pokemon__.getWeaknessesByType()

    def getStrengthsByType(self):
        return self.__pokemon__.getStrengthsByType()

    def getTypes(self):
        return self.__pokemon__.getType()

    def getName(self):
        return self.__pokemon__.getName()