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
    bulbasaur = pokemon(gd=bulbasaur_d)._randomize_vital_statistics(set_level=14).set_nickname(nickname="Saura")
    print bulbasaur.get_pokemon_full_stats()
    bulbasaur.earn_exp(bulbasaur.get_exp_to_next_level())
    print bulbasaur.get_pokemon_full_stats()
    #
    print "\n\nCan evolve by level up?: {}\n".format(bulbasaur.can_evolve_by_level_up())
    bulbasaur.earn_exp(bulbasaur.get_exp_to_next_level())
    print bulbasaur.get_pokemon_full_stats()
    #
    print "\n\nCan evolve by level up?: {}\n".format(bulbasaur.can_evolve_by_level_up())
    if bulbasaur.can_evolve_by_level_up() is not None:
        bulbasaur.evolve(bulbasaur.can_evolve_by_level_up())
    print bulbasaur.get_pokemon_full_stats()
    
    eevee = pokemon(gd=eevee_d)._randomize_vital_statistics(set_level=15).set_nickname(nickname="Maev")
    print eevee.get_pokemon_full_stats()
    print "\n\nCan evolve by level up?: {}\n".format(bulbasaur.can_evolve_by_level_up())
    

main()