from enum import Enum

class PokemonType(str, Enum):
    WATER = 'water'
    FIRE = 'fire'
    GRASS = 'grass'
    ELECTRIC = 'electric'
    FIGHTING = 'fighting'
    ROCK = 'rock'
    GROUND = 'ground'
    ICE = 'ice'
    STEEL = 'steel'
    DARK = 'dark'
    FAIRY = 'fairy'
    PSYCHIC = 'psychic'
    BUG = 'bug'
    FLYING = 'flying'
    POISON = 'poison'
    NORMAL = 'normal'
    GHOST = 'ghost'
    DRAGON = 'dragon'
    STELLAR = 'stellar'

class Transformation(str, Enum):
    MEGA = 'mega'
    DYNAMAX = 'dynamax'
    TERA = 'tera'