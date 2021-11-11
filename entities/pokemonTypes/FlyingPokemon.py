from entities.DecoratorPokemon import DecoratorPokemon
from entities.pokemonTypes.config import type_strengths  
from entities.pokemonTypes.config import type_weaknesses

class FlyingPokemon(DecoratorPokemon):
    strengths = type_strengths['flying']
    weaknesses = type_weaknesses['flying']
    typeName = "Flying"

    def __init__(self, pokemon):
        super().__init__(pokemon)
        self.pokemon = pokemon

    def getWeaknessesByType(self):
        return self.weaknesses + self.pokemon.getWeaknessesByType()

    def getStrengthsByType(self):
        return self.strengths + self.pokemon.getStrengthsByType()

    def getTypes(self):
        return [self.typeName] + self.pokemon.getTypes()

    def getName(self):
        return self.pokemon.getName()