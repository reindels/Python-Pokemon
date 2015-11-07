from constants import constants

class trainer_class():
    def __init__(self, class_dict=None):
        if class_dict is not None:
            self.set_class(class_dict=class_dict)
        self.name = 'Pokemon Trainer'
        self.base_prize_money = 100
    def __str__(self):
        return self.name

    def set_class(self, class_dict=None):
        if class_dict is None:
            return False
        self.name = class_dict.get('name')
        self.base_prize_money = class_dict.get(constants.base_prize_money)

    def get_class(self):
        return "CLASS: " +self.name + "\nPRIZE MONEY: $" + str(self.base_prize_money)




#Trainer class Dicts
pokemon_trainer_dict = {'name': 'Pokemon Trainer', constants.base_prize_money: 100}
rival_dict = {'name': 'Rival', constants.base_prize_money: 100}
professor_dict = {'name': 'Professor', constants.base_prize_money: 100}
gym_leader_dict = {'name': 'Gym Leader', constants.base_prize_money: 100}
elite_four_dict = {'name': 'Elite Four', constants.base_prize_money: 100}
champion_dict = {'name': 'Champion', constants.base_prize_money: 200}
# GEN 1 TRAINERS
beauty_dict = {'name': 'Beauty', constants.base_prize_money: 80}
biker_dict = {'name': 'Biker', constants.base_prize_money: 20}
bird_keeper_dict = {'name': 'Bird Keeper', constants.base_prize_money: 40}
black_belt_dict = {'name': 'Black Belt', constants.base_prize_money: 48}
bug_catcher_dict = {'name': 'Bug Catcher', constants.base_prize_money: 16}
burglar_dict = {'name': 'Burglar', constants.base_prize_money: 90}
channeler_dict = {'name': 'Channeler', constants.base_prize_money: 32}
cool_trainer_dict = {'name': 'Cool Trainer', constants.base_prize_money: 100}
rouchneck_dict = {'name': 'Roughneck', constants.base_prize_money: 32}
engineer_dict = {'name': 'Engineer', constants.base_prize_money: 50}
fisherman_dict = {'name': 'Fisherman', constants.base_prize_money: 56}
gambler_dict = {'name': 'Gambler', constants.base_prize_money: 120}
gentleman_dict = {'name': 'Gentleman', constants.base_prize_money: 200}
lady_dict = {'name': 'Lady', constants.base_prize_money: 200}
rocket_grunt_dict = {'name': 'Rocket Grunt', constants.base_prize_money: 40}
rocket_executive_dict = {'name': 'Rocket Executive', constants.base_prize_money: 80}
rocket_boss_dict = {'name': 'Rocket Boss', constants.base_prize_money: 200}
hiker_dict = {'name': 'Hiker', constants.base_prize_money: 56}
camper_dict = {'name': 'Camper', constants.base_prize_money: 20}
picknicker_dict = {'name': 'Picknicker', constants.base_prize_money: 20}
juggler_dict = {'name': 'Juggler', constants.base_prize_money: 40}
lass_dict = {'name': 'Lass', constants.base_prize_money: 24}
poke_maniac_dict = {'name': 'Poke Maniac', constants.base_prize_money: 64}
psychic_dict = {'name': 'Psychic', constants.base_prize_money: 56}
rocker_dict = {'name': 'Rocker', constants.base_prize_money: 25}
super_nerd_dict = {'name': 'Super Nerd', constants.base_prize_money: 32}
swimmer_dict = {'name': 'Swimmer', constants.base_prize_money: 16}
sailor_dict = {'name': 'Sailor', constants.base_prize_money: 16}
scientist_dict = {'name': 'Scientist', constants.base_prize_money: 100}
tamer_dict = {'name': 'Tamer', constants.base_prize_money: 40}
youngster_dict = {'name': 'Youngster', constants.base_prize_money: 24}
#
#_dict = {'name': '', constants.base_prize_money: }



