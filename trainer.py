from constants import constants
from computer_storage_system import computer_storage_system
from random import randint
from pokedex import pokedex
from inventory import inventory
#
class trainer():
    def __init__(self, trainer_dict=None):
        
        self.name = ''
        self.region_of_origin = ''
        self.hometown = ''
        self.gender = ''
        self.age = ''
        self.height = ''
        self.weight = ''
        self.party = []
        self.temperary_party = []
        self.trainer_class = None
        #trainer_class.name
        #trainer_class.base_prize_money
        self.pokedex = None
        self.trainer_id = '0000-0000-0000'
        self.money = 000000
        self.badges = {}
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.is_player = True
        self.inventory = None
        self.storage = computer_storage_system()
        if trainer_dict is not None:
            self.set_trainer_from_dict(trainer_dict)
            return
    def set_trainer_from_dict(self,trainer_dict=None):
        if trainer_dict is None:
            return False
        # mandatory information
        self.name = trainer_dict.get('name')
        self.trainer_class = trainer_dict.get('trainer class')
        self.trainer_id = trainer_dict.get('trainer id')
        self.money = trainer_dict.get('money')
        # safe to assume information
        if trainer_dict.get('gender') is not None: 
            self.gender = trainer_dict.get('gender')
        else: # RANDOM GENDER
            roll = randint(0,1)
            if roll == 0:
                self.gender = constants.male
            else:
                self.gender = constants.female
        if trainer_dict.get('is player') is not None:
            self.is_player = True
        else: # ELSE ASSUME IS NPC
            self.is_player = False
        if trainer_dict.get('party') is not None:
            self.party = trainer_dict.get('party')
        else:   # SET AS EMPTY
            self.party = []
        if trainer_dict.get('inventory') is not  None:
            self.inventory = trainer_dict.get('inventory')
        else:   # SET AS NEW
            self.inventory = inventory()
            self.inventory.set_owner(self)
        if trainer_dict.get('pokedex') is not None: 
            self.pokedex = trainer_dict.get('pokedex')
            self.pokedex.set_license(self)
        else: # SET AS NEW
            self.pokedex = pokedex()
            self.pokedex.set_license(self)
        if trainer_dict.get('storage') is not  None:
            self.storage = trainer_dict.get('storage')
        else:   # SET AS NEW
            self.storage = inventory()     
        # Non key information
        if trainer_dict.get('region') is not None: 
            self.region_of_origin = trainer_dict.get('region')
        else: 
            self.region_of_origin = ""
        if trainer_dict.get('hometown') is not None: 
            self.hometown = trainer_dict.get('hometown')
        else: 
            self.hometown = None
        if trainer_dict.get('age') is not None: 
            self.age = trainer_dict.get('age')
        else: 
            self.age = randint(10,30)
        if trainer_dict.get('height') is not None: self.height = trainer_dict.get('height')
        else: self.height = ""
        if trainer_dict.get('weight') is not None: self.weight = trainer_dict.get('weight')
        else: self.weight = ""
        if trainer_dict.get('badges') is not None: self.badges = trainer_dict.get('badges')
        else: self.badges = {1:None}
        if trainer_dict.get('wins') is not None: self.wins = trainer_dict.get('wins')
        else: self.wins = 0
        if trainer_dict.get('losses') is not None: self.losses = trainer_dict.get('losses')
        else: self.losses = 0
        if trainer_dict.get('draws') is not None: self.draws = trainer_dict.get('draws')
        else: self.draws = 0
    def __str__(self):
        return '{} {} ({})'.format(self.trainer_class.name, self.name, self.get_short_gender())
    def get_from_load(self):
        ret_str = '{0:20}{1:20}\n'.format('NAME',str(self.name + " (" + self.get_short_gender()+")"))
        ret_str += '{0:20}{1:20}\n'.format('IDNo.',str(self.trainer_id))
        ret_str += '{0:20}{1:20}\n'.format('Pokedex: ',self.pokedex.version)
        ret_str += '{0:20}{1:20}\n'.format('Seen: ',str(self.pokedex.pokemon_seen))
        ret_str += '{0:20}{1:20}\n'.format('Obtained: ',str(self.pokedex.pokemon_obtained))
        ret_str += '{0:20}{1:20}\n'.format('Badges: ',str(len(self.badges)))
        return ret_str
    def _randomize_vital_statistics(self, age='Young'):
        if age is 'Young':
            base_height = 48
        if age is 'Middle Age':
            base_height = 48
    def get_short_gender(self):
        if str(self.gender).lower() is 'male':
            return 'M'
        elif str(self.gender).lower() is 'female':
            return 'F'
        else:
            return '-'
    def display(self):
        ret_str = self.get_trainer_card() + "\n"
        ret_str += self.show_party() + "\n"
        if pokedex is not None:
            ret_str += self.pokedex.get_pokedex_metadata() + "\n"
        return ret_str
    def get_short_trainer(self):
        trainer_card = '{0:20}{1:20}\n'.format('NAME', str(self.name + " (" + self.get_short_gender()+")"))
        trainer_card += '{0:20}{1:20}\n'.format('TRAINER CLASS',str(self.trainer_class.name))
        trainer_card += '{0:20}{1:20}\n'.format('MONEY','$'+str(self.money))
        return trainer_card
    def get_trainer_card(self):
        trainer_card = ""
        trainer_card += constants.divider_large
        trainer_card += '|    {0:20}{1:20}  |\n'.format('IDNo.',str(self.trainer_id))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('NAME',str(self.name + " (" + self.get_short_gender()+")"))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('AGE',str(self.age))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('HOMETOWN',str(self.hometown))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('REGION',str(self.region_of_origin))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('TRAINER CLASS',str(self.trainer_class.name))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('POKEDEX SEEN',str(self.pokedex.pokemon_obtained))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('POKEDEX OBTAINED',str(self.pokedex.pokemon_obtained))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('','')
        trainer_card += '|    {0:20}{1:20}  |\n'.format('MONEY','$'+str(self.money))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('','')
        trainer_card += '|    {0:20}{1:20}  |\n'.format('WINS',str(self.wins))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('LOSSES',str(self.losses))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('DRAWS',str(self.draws))
        trainer_card += '|    {0:20}{1:20}  |\n'.format('LEAGUE BADGES:',str(len(self.badges)))
        for badge in self.badges.keys():
            trainer_card += '|    {0:10}{1:10}{2:20}  |\n'.format('', str(badge)+'.', self.badges.get(badge))
        trainer_card += constants.divider_large
        return trainer_card
    def generate_id():
        id = ""
        for i in range(4):
            id += str(randint(0,9))
        id += "-"
        for i in range(4):
            id += str(randint(0,9))
        id += "-"
        for i in range(4):
            id += str(randint(0,9))
        return id
    def add_pokemon_to_party(self, pokemon=None):
        if pokemon is None:
            print "Pokemon is None\n"
            return False
        if len(self.party) >= constants.max_party_size:
            print "Could not add {}. Party size is {}.  Already full!\n".format(pokemon.nickname, constants.max_party_size)
            return False
        self.party.append(pokemon)
        return True
    def show_party(self):
        party_str = "{}'s Party: \n".format(self.name)
        index = 0
        if len(self.party) is 0:
            return party_str + "There are no Pokemon in the party!\n"
        for pkm in self.party:
            index += 1
            party_str += "{0}. {1}\n".format(index, pkm.get_from_party())
        return party_str
    def get_able_party_members_as_list(self):
        able_list = []
        for pkm in self.party:
            if not pkm.is_fainted():
                able_list.append(pkm)
        return able_list
    #Money Methods
    def add_money(self, amount):
        print self.money
        print amount
        self.money += amount
        print self.money
        return self.money
    def remove_money(self, amount):
        print self.money
        print amount
        self.money -= amount
        print self.money
        return amount
    def give_winnings(self):
        winnings = self.get_highest_level_pokemon() * self.trainer_class.base_prize_money
        self.remove_money(winnings)
        print "Giving ${} to winner...".format(winnings)
        return winnings
    # Battle Methods
    def able_pokemon(self):
        able_pokemon = len(self.party)
        for pkm in self.party:
            if pkm.is_fainted():
                able_pokemon -= 1
        print "Able Pokemon: {} / {}".format(able_pokemon, len(self.party))
        return able_pokemon
    def get_first_able_pokemon_from_party(self):
        for pkm in self.party:
            if constants.status_fainted not in pkm.condition:
                return pkm
        return None
    def get_highest_level_pokemon(self):
        if self.party is None or len(self.party) is 0:
            return 0
        highest_level = 0
        for pkm in self.party:
            if pkm.level > highest_level:
                highest_level = pkm.level
        return highest_level
    #Capture Pokemon
    def capture_pokemon(self, pokemon=None):
        capture_string = ""
        if pokemon is None:
            print "Pokemon is None\n"
            return False
        pokemon.set_pokemon_original_trainer(trainer=self)
        if not self.add_obtained_entry(pokemon):
            return "ERROR: trainer.capture_pokemon, pokedex.add_obtained_entry"
        added_to_party = True
        if not self.add_pokemon_to_party(pokemon):
            self.storage.add_pokemon_to_storage(pokemon)
            added_to_party = False
        capture_string = "{} was added to the pokedex!\n".format(pokemon.nickname)
        if added_to_party:
            capture_string = "{} was added to the party!\n".format(pokemon.nickname)
        else:
            capture_string = "{} was added to the pokemon storage.\n".format(pokemon.nickname)
        return capture_string
    #Pokedex
    def add_pokemon_to_seen(self, pokemon=None):
        if self.pokedex is None:
            print "This trainer does not have a pokedex\n"
            return False
        if pokemon is None:
            print "Pokemon is None\n"
            return False
        self.pokedex.add_seen_entry(pokemon)
        return True
    def add_obtained_entry(self,pokemon=None):
        if self.pokedex is None:
            print "This trainer does not have a pokedex\n"
            return False
        if pokemon is None:
            print "Pokemon is None\n"
            return False
        self.pokedex.add_obtained_entry(pokemon)
        return True
    def show_pokedex_entries(self, search_by='seen'):
        if self.pokedex is None:
            return "This trainer does not have a pokedex\n"
        return self.pokedex.get_pokedex_entries(search_by=search_by) + "\n"
    #Fully revive pokemon
    def fully_heal_all_party_members(self):
        for pkm in self.party:
            pkm.fully_heal()
    # Temp Party
    
    #Items
    def add_items(self, item=None, count=1):
        if item is None:
            return None
        if self.inventory is not None:
            return self.inventory.add_items(item=item, count=count)
        return "Item not added to inventory"
    def get_pack(self, pocket='all'):
        if self.inventory is not None:
            return self.inventory.display_inventory(pocket=pocket)
        else:
            return "No Inventory attached to this player"
    def use_item(self, item_name=None, count=1):
        if item_name is None:
            return None
        if self.inventory is not None:
            item = self.inventory.use_items(item_name=item_name, count=count)
            if item is None:
                print "Item {} is not in the inventory!".format(item_name)
        return item
    def get_item(self, item_name=None):
        if item_name is None:
            return None
        if self.inventory is not None:
            item = self.inventory.get_item(item_name=item_name)
            if item is None:
                print "Item {} is not in the inventory!".format(item_name)
        return item
    #
    
    #
    #
#







