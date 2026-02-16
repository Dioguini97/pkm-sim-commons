class Ability:
    def __init__(self, id: int, name: str, description: str):
        self.name = name
        self.description = description
        self.id = id

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'description': self.description}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
