from entities.DecoratorPokemon import DecoratorPokemon
from entities.pokemonTypes.config import type_strengths  
from entities.pokemonTypes.config import type_weaknesses

class ElectricPokemon(DecoratorPokemon):

    strengths = type_strengths['electric']
    weaknesses = type_weaknesses['electric']
    typeName = "Electric"

    def __init__(self, pokemon):
        super().__init__(pokemon)
        self.pokemon = pokemon

    def getWeaknessesByType(self):
        return self.weaknesses + self.pokemon.getWeaknessesByType()

    def getStrengthsByType(self):
        return   self.strengths + self.pokemon.getStrengthsByType()

    def getTypes(self):
        return [self.typeName] + self.pokemon.getTypes()

    def getName(self):
        return self.pokemon.getName()