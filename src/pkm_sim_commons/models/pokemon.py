from src.pkm_sim_commons import PokemonType


class Pokemon:
    def __init__(self, pokedex_num: int, name: str, types: list, base_stats: dict, abilities: list, height: float, weight: float,
                 move_list: list, img_url: str, crie_url: str=None, can_evolve: bool=None, varieties: list = None):
        self.pokedex_num = pokedex_num
        self.name = name
        self.types = [PokemonType(_type) if isinstance(_type, PokemonType) else _type for _type in types]
        self.base_stats = base_stats
        self.abilities = abilities
        self.height = height
        self.weight = weight
        self.move_list = move_list
        self.img_url = img_url
        self.crie_url = crie_url
        self.can_evolve = can_evolve
        self.varieties = varieties