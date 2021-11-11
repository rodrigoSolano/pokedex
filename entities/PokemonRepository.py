from abc import ABC, abstractmethod
from entities.Pokemon import Pokemon


class PokemonRepository(ABC):
    @abstractmethod
    def getPokemonById(self, id: int) -> Pokemon:
        pass

    @abstractmethod
    def getPokemonByName(self, name: str) -> Pokemon:
        pass

    @abstractmethod
    def getExamplesPokemonStrengthsAndWeaknessesAgainst(self, pokemon: Pokemon) -> list:
        pass