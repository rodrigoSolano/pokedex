from entities.Pokemon import Pokemon
from entities.pokemonTypes.FirePokemon import FirePokemon
from entities.pokemonTypes.WaterPokemon import WaterPokemon
from entities.pokemonTypes.GrassPokemon import GrassPokemon
from entities.pokemonTypes.ElectricPokemon import ElectricPokemon
from entities.pokemonTypes.IcePokemon import IcePokemon
from entities.pokemonTypes.FightingPokemon import FightingPokemon
from entities.pokemonTypes.NormalPokemon import NormalPokemon
from entities.pokemonTypes.PoisonPokemon import PoisonPokemon
from entities.pokemonTypes.GroundPokemon import GroundPokemon
from entities.pokemonTypes.FlyingPokemon import FlyingPokemon
from entities.pokemonTypes.PsychicPokemon import PsychicPokemon
from entities.pokemonTypes.RockPokemon import RockPokemon
from entities.pokemonTypes.GhostPokemon import GhostPokemon
from entities.pokemonTypes.DragonPokemon import DragonPokemon
from entities.pokemonTypes.DarkPokemon import DarkPokemon
from entities.pokemonTypes.SteelPokemon import SteelPokemon
from entities.pokemonTypes.FairyPokemon import FairyPokemon
from entities.pokemonTypes.BugPokemon import BugPokemon

class PokemonFactory():

    @classmethod
    def makePokemon(cls,id:int,name:str,types:list[str]):
        pokemon = Pokemon(id,name)
        for type in types:
            if type == "fire" :
                pokemon = FirePokemon(pokemon)
            elif type == "water" :
                pokemon = WaterPokemon(pokemon)
            elif type == "grass" :
                pokemon = GrassPokemon(pokemon)
            elif type == "electric" :
                pokemon = ElectricPokemon(pokemon)
            elif type == "ice" :
                pokemon = IcePokemon(pokemon)
            elif type == "fighting" :
                pokemon = FightingPokemon(pokemon)
            elif type == "normal" :
                pokemon = NormalPokemon(pokemon)
            elif type == "poison" :
                pokemon = PoisonPokemon(pokemon)
            elif type == "ground" :
                pokemon = GroundPokemon(pokemon)
            elif type == "flying" :
                pokemon = FlyingPokemon(pokemon)
            elif type == "psychic" :
                pokemon = PsychicPokemon(pokemon)
            elif type == "rock" :
                pokemon = RockPokemon(pokemon)
            elif type == "ghost" :
                pokemon = GhostPokemon(pokemon)
            elif type == "dragon" :
                pokemon = DragonPokemon(pokemon)
            elif type == "dark" :
                pokemon = DarkPokemon(pokemon)
            elif type == "steel" :
                pokemon = SteelPokemon(pokemon)
            elif type == "fairy" :
                pokemon = FairyPokemon(pokemon)
            elif type == "bug" :
                pokemon = BugPokemon(pokemon)
        return pokemon