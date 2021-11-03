from repository.PokemonAPIRepository import PokemonAPIRepository
from entities.BasePokemon import BasePokemon

class Pokedex:
    def __init__(self):
        self.pokemonRepository = PokemonAPIRepository()

    def run(self):
        self.showMenu()

    def showMenu(self):
        print("Welcome to 'THE POKEDEX'")
        while True:
            print("1. Get pokemon by name")
            print("2. Get pokemon by id")
            print("3. Exit")
            print("Please enter a number: ", end="")
            choice = input()
            if choice == "1":
                print("Please enter a pokemon name: ", end="")
                pokemon_name = input()
                pokemon = self.getPokemonByName(pokemon_name)
                self.showPokemonInfo(pokemon)
            elif choice == "2":
                print("Please enter a pokemon id: ", end="")
                pokemon_id = int(input())
                pokemon = self.getPokemonById(pokemon_id)
                self.showPokemonInfo(pokemon)
            elif choice == "3":
                break
            print("")

    def showPokemonInfo(self,pokemon:BasePokemon):
        print("Name: " + str(pokemon.getName()))
        print("Types: " + str(pokemon.getTypes()))
        print("Strengths types: " + str(pokemon.getStrengthsByType()))
        print("Weaknesses types: " + str(pokemon.getWeaknessesByType()))            
    
    def getPokemonByName(self, pokemonName:str) -> BasePokemon:
        return self.pokemonRepository.getPokemonByName(pokemonName)

    def getPokemonById(self, pokemonId:int) -> BasePokemon:
        return self.pokemonRepository.getPokemonById(pokemonId)