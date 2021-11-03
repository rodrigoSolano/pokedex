from abc import ABC, abstractmethod

class BasePokemon(ABC):
    @abstractmethod
    def getWeaknessesByType(self):
        pass

    @abstractmethod
    def getStrengthsByType(self):
        pass

    @abstractmethod
    def getTypes(self):
        pass

    @abstractmethod
    def getName(self):
        pass