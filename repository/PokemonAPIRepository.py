from entities.Pokemon import Pokemon
from entities.PokemonRepository import PokemonRepository
from entities.PokemonFactory import PokemonFactory
import requests


class PokemonAPIRepository(PokemonRepository):

    baseUrl = "https://pokeapi.co/api/v2/pokemon/"

    def __init__(self):
        super().__init__()

    def getPokemonById(self, id: int) -> Pokemon:
        return self.getPokemonData(self.baseUrl + str(id))

    def getPokemonByName(self, name: str) -> Pokemon:
        return self.getPokemonData(self.baseUrl + name)

    def getPokemonData(self, url: str) -> Pokemon:
        pokemon_data = requests.get(url)
        if pokemon_data:
            pokemon_data = pokemon_data.json()
            pokemon_name =  pokemon_data["name"]
            pokemon_id = pokemon_data["id"]
            pokemon_types = []
            for pokemon_type in pokemon_data["types"]:
                pokemon_types.append(pokemon_type["type"]["name"])
            pokemon = PokemonFactory.makePokemon(pokemon_id, pokemon_name, pokemon_types)
            return pokemon
        else:
