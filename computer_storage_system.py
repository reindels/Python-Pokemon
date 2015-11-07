

class computer_storage_system():
    def __init__(self):
        self.pokemon_storage = []
        self.item_storage = []
        self.mail_storage = []
    def add_pokemon_to_storage(self, pokemon=None):
        if pokemon is None:
            return False
        self.pokemon_storage.append(pokemon)
        return True
    def add_item_to_storage(self, item=None):
        if item is None:
            return False
        self.item_storage(item)
        return True
    def display_pokemon_storage(self, start=0, ):
        storage = ""
        index = 0
        for pokemon in self.pokemon_storage:
            index += 1
            storage += " - {}: {}\n".format(index, pokemon.nickname)