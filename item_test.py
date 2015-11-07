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




def main():
    clear()
    pack = inventory()
    print pack.display_inventory()
    potion = item(potion_dict)
    water_stone = item(water_stone_dict)
    print potion
    print pack.add_items(potion, 1)
    print pack.display_inventory()
    print "\n"
    print pack.add_items(potion, 1)
    print pack.add_items(item(poke_ball_dict), 5)
    print pack.add_items(item(superpotion_dict), 1)
    print pack.add_items(item(full_heal_dict), 1)
    print pack.add_items(item(full_restore_dict), 1)
    print pack.display_inventory('medicine')
    print pack.add_items(water_stone, 1)
    print pack.display_inventory()
    print "Get item {}\n".format(str(pack.get_item("Potion")))
    print "Get item {}\n".format(str(pack.get_item("Water Stone")))
    print "Get item {}\n".format(str(pack.get_item("Poke Ball")))
    print "Use item {}\n".format(str(pack.use_items("Poke Ball", 1)))
    print "Use item {}\n".format(str(pack.use_items("Super Potion", 1)))
    print "Use item {}\n".format(str(pack.use_items("Water Stone", 1)))
    print pack.display_inventory()
    print pack.display_inventory()
    #
    #
    input = "full "
    test_item = pack.get_item(input)
    if test_item is not None:
        print test_item.name
    else:
        print "RETURNED NONE\n"
    #
#
main()