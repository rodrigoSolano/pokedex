type_strengths = {
    "bug" : ["grass", "psychic", "dark"],
    "dark" :   ["psychic", "ghost"],
    "dragon" : ["dragon"],
    "electric" : ["water", "flying"],
    "fairy" : ["fighting", "dragon", "dark"],
    "fighting" : ["normal", "ice", "rock", "dark", "steel"],
    "fire" : ["bug", "steel", "grass", "ice"],
    "flying" : ["grass", "fighting", "bug"],
    "ghost" : ["ghost", "psychic"],
    "grass" : ["water", "ground", "rock"],
    "ground" : ["fire", "electric", "poison", "rock", "steel"],
    "ice" : ["grass", "ground", "flying", "dragon"],
    "normal" : ["rock"],
    "poison" : ["grass", "fairy"],
    "psychic" : ["fighting", "poison"],
    "rock" : ["fire", "ice", "flying", "bug"],
    "steel" : ["ice", "rock", "fairy"],
    "water" : ["fire", "ground", "rock"]
}

type_weaknesses = {
    "bug" : ["Fairy", "Fighting", "Fire", "Flying", "Ghost", "Poison", "Steel"],
    "dark" : ["Dark", "Fairy", "Fighting"],
    "dragon" : ["Fairy", "Steel"],
    "electric" : ["Electric", "Dragon", "Grass", "Ground"],
    "fairy" : ["Fire", "Poison", "Steel"],
    "fighting" : ["Bug", "Ghost", "Fairy", "Flying", "Poison", "Psychic"],
    "fire" : ["Dragon", "Fire", "Rock", "Water"],
    "flying" : ["Electric", "Rock", "Steel"],
    "ghost" : ["Dark", "Normal"],
    "grass" : ["Bug", "Dragon", "Fire", "Flying", "Grass", "Poison", "Steel"],
    "ground" : ["Bug", "Flying", "Grass"],
    "ice" : ["Fire", "Ice", "Steel", "Water"],
    "normal" : ["Ghost", "Rock", "Steel" ],
    "poison" : ["Ghost", "Ground", "Poison", "Rock", "Steel"],
    "psychic" : ["Dark", "Psychic", "Steel"],
    "rock" : ["Fighting", "Ground", "Steel"],
    "steel" : ["Electric", "Fire", "Steel", "Water"],
    "water" : ["Dragon", "Grass", "Water"]

}