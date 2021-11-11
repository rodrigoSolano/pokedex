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
            return None

    def getExamplesPokemonStrengthsAndWeaknessesAgainst(self, pokemon: Pokemon) -> dict:
        url = "https://pokeapi.co/api/v2/type/"
        strengths = pokemon.getStrengthsByType()
        weaknesses = pokemon.getWeaknessesByType()
        pokemons_strengths = []
        pokemon_weaknesses = []
        pokemon_types = pokemon.getTypes()

        for strength in strengths:
            if strength  not in pokemon_types:
                pokemon_strength = requests.get(url + strength.lower())
                pokemon_strength = pokemon_strength.json()
                pokemons_strengths.append(pokemon_strength["pokemon"][0]["pokemon"]["name"])
        
        for weakness in weaknesses:
            if weakness  not in pokemon_types:
                pokemon_weakness = requests.get(url + weakness.lower())
                pokemon_weakness = pokemon_weakness.json()
                pokemon_weaknesses.append(pokemon_weakness["pokemon"][0]["pokemon"]["name"])
        
        name_pokemon = pokemon.getName()

        if name_pokemon in pokemons_strengths:
            pokemons_strengths.remove(name_pokemon)
        if name_pokemon in pokemon_weaknesses:
            pokemon_weaknesses.remove(name_pokemon)

        return {"strengths": pokemons_strengths, "weaknesses": pokemon_weaknesses}