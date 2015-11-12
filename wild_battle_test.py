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
if platform.system() is "Linux":
    clear = lambda: os.system('clear')
else:#if platform.system() is "Windows":
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
def create_trainer():
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
        player.inventory = set_inventory(player)
        return player
    # Program
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
#
def main():
    starters = set_starters()
    #starter_pokemon = starters[0]
    player = create_trainer()
    wild_pokemon_list = set_wild_pokemon()
    for pkm in wild_pokemon_list:
        print pkm.get_pokemon_full_stats()
    wild_pokemon = random_pokemon_from_list(wild_pokemon_list)

    #print "\ninventory dict:"
    #for key in test_inv_dict.keys():
    #    print "{}: {}\n".format(key, test_inv_dict[key])
    #inv = inventory(inv_dict=test_inv_dict)
    #inv.set_owner(player)
    #print "\n inventory instance:"
    #print inv.get_pocket_contents(pocket=constants.item_type_general)
    #print inv.get_pocket_contents(pocket=constants.item_type_medicine)
    #print inv.get_pocket_contents(pocket=constants.item_type_berry)
    #print inv.get_pocket_contents(pocket=constants.item_type_key_item)
    #print inv.get_pocket_contents(pocket=constants.item_type_poke_ball)
    #print inv.use_item_by_name(item_name='poke ball')
    #print inv.get_pocket_contents()
    #petc()
    clear()
    test_name = "--- Wild Pokemon Battle Using Interfaces ---\n"
    cmd_console = cmd_interface()
    wild_battle = battle()
    
    print test_name      
    
    starter_pokemon = cmd_console.choose_pokemon_from_list(starters)
    
    #cmd_console.rename_pokemon(starter_pokemon)
    #clear()
    player.capture_pokemon(starter_pokemon)
    print player.get_trainer_card()
    print player.show_party()
    print player.pokedex.get_pokedex_entries()
    #print player.get_pack()
    #
    
    print "Will Encounter {}".format(wild_pokemon.name)
    #
    print "Entering the Field"
    #petc()
    #cmd_console.enter_wild_battle(trainer_1=player, wild_pokemon=wild_pokemon)
    wild_battle.wild_pokemon_battle(trainer_1=player, wild_pokemon=wild_pokemon)
    print "Leaving the Field"
    petc()
    print player.get_trainer_card()
    print player.show_party()
    print player.pokedex.get_pokedex_entries()
#
clear()
main()
#


