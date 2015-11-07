'''



'''
#imports
from save_and_restore import *
import os
import time
import atexit
from random import randint
from constants import constants
from utilities import *
from trainer import trainer
from trainerclass import *
from inventory import *
from pokedex import pokedex
from pokemon_dicts import *
from pokemon_kanto_dicts import *
from pokemon_johto_dicts import *
from pokemon_hoenn_dicts import *
from pokemon_sinnoh_dicts import *
from pokemon_unova_dicts import *
from pokemon import pokemon
from moves import *
from move_dict import *
from battle import battle
from items import *
from cmd_interface import cmd_interface
clear = lambda: os.system('cls')
petc = lambda: raw_input("Press Enter to Continue...")
cmd_console = cmd_interface()

clear = lambda: os.system('cls')
petc = lambda: raw_input("Press Enter to Continue...")

def attempt_capture_of_pokemon(trainer=None, ball=None, pokemon=None):
    shake_check_count = 4
    tries = 0
    is_pokemon_captured = True
    for check in range(shake_check_count):
        tries += 1
        print " * Shake *"# try {}".format(tries)
        time.sleep(1)
        if not pokemon.shake_check(ball.ball_modifier):
            return False
    return is_pokemon_captured
def set_starters():
    starters = []
    starters.append(pokemon(gd=bulbasaur_d)._randomize_vital_statistics(set_level=5))
    starters.append(pokemon(gd=charmander_d)._randomize_vital_statistics(set_level=5))
    starters.append(pokemon(gd=squirtle_d)._randomize_vital_statistics(set_level=5))
    #starters.append(pokemon(gd=pikachuv)._randomize_vital_statistics(set_level=5))
    return starters
def set_wild_pokemon():
    wild = []
    wild.append(pokemon(gd=bulbasaur_d)._randomize_vital_statistics(min_level=2, max_level=5))
    wild.append(pokemon(gd=charmander_d)._randomize_vital_statistics(min_level=2, max_level=5))
    wild.append(pokemon(gd=squirtle_d)._randomize_vital_statistics(min_level=2, max_level=5))
    #wild.append(pokemon(gd=pikachuv)._randomize_vital_statistics(min_level=2, max_level=5, min_iv=0, max_iv=31,ev_diff_dict=None))
    return wild
def random_pokemon_from_list(pokemon_list=None):
    #print pokemon_list
    if pokemon_list is None:
        return "random_pokemon_from_list pokemon_list is None"
    if len(pokemon_list) > 0:
        return pokemon_list[randint(0,len(pokemon_list)-1)]
    else:
        return None
def set_inventory(trainer=None):
    pack = inventory()
    pack.trainer = trainer
    print pack.add_items(item(custom_ball_dict), 50)
    print pack.add_items(item(poke_ball_dict), 50)
    print pack.add_items(item(great_ball_dict), 50)
    print pack.add_items(item(ultra_ball_dict), 50)
    print pack.add_items(item(master_ball_dict), 1)
    print pack.add_items(item(superpotion_dict), 1)
    print pack.add_items(item(potion_dict), 5)
    print pack.add_items(item(superpotion_dict), 5)
    print pack.add_items(item(full_heal_dict), 5)
    print pack.add_items(item(revive_dict), 5)
    return pack
def create_trainer_1():
        tc = trainer_class(pokemon_trainer_dict)
        pokedex_dict = {'creator': "The Professor", 'version': "1.0", 'mode': "Local", 'max entries': 150, 'seen': 0, 'obtained': 0, 
        'local entries': dict(), 'national entries': dict()}
        
        player_dict = {'name': 'Stefan', 'gender': 'Male', 'age': 23, 'region': 'Orre', 'hometown': 'Gateon Port',
                       'height': "{}\'{}\"".format(5,11),'weight': "{} lbs.".format(185),
                       'trainer class': trainer_class(pokemon_trainer_dict),
                       'trainer id': generate_id(),
                       'pokedex': None,
                       'party': [],
                       'badges': {},
                       'money': 3000,
                       'is player': True,
                       'wins': 0, 'losses': 0, 'draws': 0
                       }
        player = trainer(trainer_dict=player_dict)
        player.pokedex = pokedex(dex_dict=pokedex_dict, trainer=player)
        inv = inventory(inv_dict=test_inv_dict)
        inv.set_owner(player)
        player.inventory = set_inventory(trainer=player)
        #player.capture_pokemon(pokemon(gd=charmander_d)._randomize_vital_statistics(set_level=5))
        return player
def create_trainer_2():
        tc = trainer_class(pokemon_trainer_dict)
        pokedex_dict = {'creator': "The Professor", 'version': "1.0", 'mode': "Local", 'max entries': 150, 'seen': 0, 'obtained': 0, 
        'local entries': dict(), 'national entries': dict()}
        
        player_dict = {'name': 'Karl', 'gender': 'Male', 'age': 21, 'region': 'Orre', 'hometown': 'Gateon Port',
                       'height': "{}\'{}\"".format(6,1),'weight': "{} lbs.".format(175),
                       'trainer class': trainer_class(pokemon_trainer_dict),
                       'trainer id': generate_id(),
                       'pokedex': None,
                       'party': [],
                       'badges': {},
                       'money': 3000,
                       'is player': True,
                       'wins': 0, 'losses': 0, 'draws': 0
                       }
        player = trainer(trainer_dict=player_dict)
        player.pokedex = pokedex(dex_dict=pokedex_dict, trainer=player)
        inv = inventory(inv_dict=test_inv_dict)
        inv.set_owner(player)
        player.inventory = set_inventory(trainer=player)
        #player.capture_pokemon(pokemon(gd=squirtle_d)._randomize_vital_statistics(set_level=5))
        return player
    # Program
#
def main():
    player_1 = create_trainer_1()
    player_2 = create_trainer_2()
    pkm1_1 = pokemon(gd=bulbasaur_d)._randomize_vital_statistics(set_level=5, gender=constants.male).set_nickname("Bulba")
    pkm1_2 = pokemon(gd=charmander_d)._randomize_vital_statistics(set_level=5, gender=constants.female).set_nickname("Char Char")
    pkm1_3 = pokemon(gd=squirtle_d)._randomize_vital_statistics(set_level=5, gender=constants.male).set_nickname("Squirts")

    pkm2_1 = pokemon(gd=bulbasaur_d)._randomize_vital_statistics(set_level=5, gender=constants.female).set_nickname("Saura")
    pkm2_2 = pokemon(gd=charmander_d)._randomize_vital_statistics(set_level=5, gender=constants.male).set_nickname("Ander")
    pkm2_3 = pokemon(gd=squirtle_d)._randomize_vital_statistics(set_level=5, gender=constants.female).set_nickname("Turts")

    player_1.capture_pokemon(pkm1_1)
    player_1.capture_pokemon(pkm1_2)
    player_1.capture_pokemon(pkm1_3)

    player_2.capture_pokemon(pkm2_1)
    player_2.capture_pokemon(pkm2_2)
    player_2.capture_pokemon(pkm2_3)
    clear()
    test_name = "--- Trainer Battle Using Interfaces ---\n"
    cmd_console = cmd_interface()
    trainer_battle = battle()
    #
    print test_name      
    print player_1.get_trainer_card()
    print player_1.show_party()
    print player_2.get_trainer_card()
    print player_2.show_party()
    #
    print "Entering the field."
    petc()
    print trainer_battle.wild_pokemon_battle(trainer_1=player_1, wild_pokemon=random_pokemon_from_list(set_wild_pokemon()))
    print "Leaving the field."
    player_1.fully_heal_all_party_members
    print "Entering the arena."
    petc()
    print trainer_battle.trainer_pokemon_battle(trainer_1=player_1, trainer_2=player_2)
    print "Leaving the arena."
    petc()
    print player_1.get_trainer_card()
    print player_1.show_party()
    print player_2.get_trainer_card()
    print player_2.show_party()
    #
#
clear()
main()
