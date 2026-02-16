from ..enums import ItemCategory, ItemAttribute


class Item:
    def __init__(self, id: int, name: str, img_url: str, attributes: list[str], category: str, fling_power: int, fling_effect: str, description: str):
        self.id = id
        self.name = name
        self.img_url = img_url
        self.fling_power = fling_power
        self.fling_effect = fling_effect
        self.description = description
        if isinstance(category, ItemCategory):
            self.category = category
        else:
            self.category = ItemCategory(category)

        self.attributes = [ItemAttribute(att) if isinstance(att, ItemAttribute) else att for att in attributes]

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'img_url': self.img_url,
            'fling_power': self.fling_power,
            'fling_effect': self.fling_effect,
            'category': self.category,
            'attributes': [attribute for attribute in self.attributes],
            'description': self.description
        }

    @classmethod
    def from_dict(cls, data: dict):
        """
        Cria uma instância de Move a partir de um dicionário.
        Substitui a necessidade de uma função externa de mapping.
        """
        return cls(**data)