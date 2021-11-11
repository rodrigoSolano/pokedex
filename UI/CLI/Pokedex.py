from entities.PokemonRepository import PokemonRepository
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
            pokemon = None
            print("1. Get pokemon by name")
            print("2. Get pokemon by id")
            print("3. Exit")
            print("Please enter a number: ", end="")
            choice = input()
            try:
                choice = int(choice)
            except ValueError:
                print("Invalid choice")
                print("")
                continue
            if choice == 1:
                print("Please enter a pokemon name: ", end="")
                pokemon_name = input()
                pokemon = self.getPokemonByName(pokemon_name)
            elif choice == 2:
                print("Please enter a pokemon id: ", end="")
                pokemon_id = int(input())
                pokemon = self.getPokemonById(pokemon_id)
            elif choice == 3:
                break
            else:
                print("Invalid choice")
                print("")
                continue
            
            if pokemon is not None:
                self.showPokemonInfo(pokemon)                    
            else:
                print("Pokemon not found")
                
            print("")

    def showPokemonInfo(self,pokemon: BasePokemon):
        pokemon_examples = self.pokemonRepository.getExamplesPokemonStrengthsAndWeaknessesAgainst(pokemon)
        weakness_pokemon_examples = pokemon_examples["strengths"]
        strength_pokemon_examples = pokemon_examples["weaknesses"]

        pokemon_name = pokemon.getName()
        pokemon_types = str(pokemon.getTypes())
        pokemon_strengths_by_type = pokemon.getStrengthsByType()
        pokemon_weaknesses_by_type = pokemon.getWeaknessesByType()

        for pokemon_strength in pokemon_strengths_by_type:
            if pokemon_strength in pokemon_types:
                pokemon_strengths_by_type.remove(pokemon_strength)

        for pokemon_weakness in pokemon_weaknesses_by_type:
            if pokemon_weakness in pokemon_types:
                pokemon_weaknesses_by_type.remove(pokemon_weakness)

        pokemon_strengths_by_type = str(pokemon_strengths_by_type)
        pokemon_weaknesses_by_type = str(pokemon_weaknesses_by_type)

        weakness_pokemon_examples = str(weakness_pokemon_examples)
        strength_pokemon_examples = str(strength_pokemon_examples)

        print("{:>18}".format("Name: ") + pokemon_name)
        print("{:>18}".format("Types: ") + pokemon_types)
        print("{:>18}".format("Strengths types: ") + pokemon_strengths_by_type)
        print("{:>18}".format("Examples: ") + weakness_pokemon_examples)
        print("{:>18}".format("Weaknesses types: ") + pokemon_weaknesses_by_type)  
        print("{:>18}".format("Examples: ") + strength_pokemon_examples)          
    
    def getPokemonByName(self, pokemonName:str) -> BasePokemon:
        return self.pokemonRepository.getPokemonByName(pokemonName)

    def getPokemonById(self, pokemonId:int) -> BasePokemon:
        return self.pokemonRepository.getPokemonById(pokemonId)