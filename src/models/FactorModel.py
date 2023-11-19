class Factor():

    def __init__(self, factor_id, name, description) -> None:
        self.factor_id = factor_id
        self.name = name
        self.description = description

    def to_json(self):
        return {
            'factor_id': self.factor_id,
            'name': self.name,
            'description': self.description
        }
    
