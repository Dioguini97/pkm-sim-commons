from ..enums import PokemonType


class Pokemon:
    def __init__(self,id: int, name: str, types: list, base_stats: dict, abilities: list, height: float, weight: float,
                 move_list: list, img_url: str, crie_url: str=None, can_evolve: bool=None, varieties: list = None):
        self.id = id    
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

    def to_dict(self) -> dict:
        """
        Mapeia a instância da classe para um dicionário formatado.
        Ideal para persistência no MongoDB ou respostas de API.
        """
        return {
            "id": self.id,
            "name": self.name,
            # Convertemos o Enum para o valor (string/int) para ser serializável
            "types": [t.value for t in self.types],
            "base_stats": self.base_stats,
            "abilities": self.abilities,
            "height": self.height,
            "weight": self.weight,
            "move_list": self.move_list,
            "img_url": self.img_url,
            "crie_url": self.crie_url,
            "can_evolve": self.can_evolve,
            "varieties": self.varieties
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de Pokemon a partir de um dicionário.
        Útil quando lês dados do MongoDB ou de uma API externa.
        """
        return cls(**data)