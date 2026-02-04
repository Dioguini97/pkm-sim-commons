from enum import Enum


class MoveTarget(str, Enum):
    SPECIFIC_MOVE = 'specific-move'  # p.e. Curse, Counter
    SELECTED_POKEMON_ME_FIRST = 'selected-pokemon-me-first'  # p.e. me-first, max moves
    ALLY = 'ally'  # p.e. Helping Hand
    USERS_FIELD = 'users-field',  # p.e. Reflect, Light Screen, Tailwind
    USER_OR_ALLY = 'user-or-ally'  # p.e. acupressure (only)
    OPPONENTS_FIELD = 'opponents-field'  # p.e. Stealth Rock, Spikes
    USER = 'user'  # p.e. Swords Dance, Recover
    RANDOM_OPPONENT = 'random-opponent'  # p.e. Thrash, Outrage, Struggle
    ALL_OTHER_POKEMON = 'all-other-pokemon'  # p.e. Earthquake, Surf
    SELECTED_POKEMON = 'selected-pokemon'  # p.e. Shadow Ball, Flamethrower
    ALL_OPPONENTS = 'all-opponents'  # p.e. Blizzard, Rock Slide
    ENTIRE_FIELD = 'entire-field'  # p.e. Hail, Rain Dance, Trick Room, Grassy Terrain
    USER_AND_ALLIES = 'user-and-allies'  # p.e. life-dew, howl
    ALL_POKEMON = 'all-pokemon'  # p.e. Perish Song
    ALL_ALLIES = 'all-allies'  # p.e. Dragon Cheer
    FAINTING_POKEMON = 'fainting-pokemon'  # p.e. Revival Blessing


class MoveAilment(str, Enum):
    UNKNOWN = 'unknown'
    NONE = 'none'
    PAR = 'paralysis'
    SLP = 'sleep'
    FRZ = 'freeze'
    BRN = 'burn'
    PSN = 'poison'
    BPSN = 'badly-poison'
    CONFUSION = 'confusion'
    INFATUATION = 'infatuation'
    TRAP = 'trap'
    NIGHTMARE = 'nightmare'
    TORMENT = 'torment'
    DISABLE = 'disable'
    YAWN = 'yawn'
    HEAL_BLOCK = 'heal-block'
    NO_TYPE_IMMUNITY = 'no-type-immunity'
    LEECH_SEED = 'leech-seed'
    EMBARGO = 'embargo'
    PERISH_SONG = 'perish-song'
    INGRAIN = 'ingrain'
    SILENCE = 'silence'
    TAR_SHOT = 'tar-shot'


class ActionType(str, Enum):
    ATTACK = 'attack'
    SWITCH = 'switch'
    RUN = 'run'


class DamageClass(str, Enum):
    PHYSICAL = 'physical'
    SPECIAL = 'special'
    STATUS = 'status'

class MoveCategory(str, Enum):
    DAMAGE = "damage"
    AILMENT = "ailment"  # Spore, Perish Song, Toxic
    NET_GOOD_STATS = "net-good-stats"  # Swords Dance, Calm Mind
    HEAL = "heal"  # Recover, Soft-Boiled
    DAMAGE_AILMENT = "damage+ailment"  # Flamethrower, Poison Sting, porque dá damage e pode causar status
    SWAGGER = "swagger"  # Swagger, Flatter, raise target stats + inflict status
    DAMAGE_LOWER = "damage+lower"  # moves that deal damage and lower target's stats, e.g., Psychic, Mud-Slap
    DAMAGE_RAISE = "damage+raise"  # moves that deal damage and raise user's stats, e.g., Close Combat, Flame Charge
    DAMAGE_HEAL = "damage+heal"  # Giga Drain, Drain Punch
    OHKO = "ohko"  # Fissure, Guillotine, Horn Drill
    WHOLE_FIELD_EFFECT = "whole-field-effect"  # moves that affect the entire field, e.g., Rain Dance, Haze, Trick Room, Grassy Terrain, Gravity
    FIELD_EFFECT = "field-effect"  # moves that affect one side of the field, e.g., Stealth Rock, Light Screen, Reflect, Wide Guard
    FORCE_SWITCH = "force-switch"  # Roar, Whirlwind
    UNIQUE = "unique"  # e.g., Transform, Mimic, Sketch, Metronome, Follow Me