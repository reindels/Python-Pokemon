'''
THIS IS THE GAME.  
'''
#imports standard library
import os, platform
import sys
from os import listdir
from os.path import isfile, join
import time
import atexit
from random import randint

#imports custom files
from constants import constants
from utilities import *
from trainer import trainer
from trainerclass import *
from inventory import *
from pokedex import pokedex
from pokemon_dicts import *
from pokemon import pokemon
from moves import *
from move_dict import *
from battle import battle
from items import *
from cmd_interface import cmd_interface
from region import room, area, feature
from save_and_restore import *
if platform.system() is "Linux":
    clear = lambda: os.system('clear')
else:#if platform.system() is "Windows":
    clear = lambda: os.system('cls')

petc = lambda: raw_input("Press Enter to Continue...")
pause = lambda: time.sleep(1)
#
#
#
cmd_console = cmd_interface()
INPUT_ERROR = "ERROR: {} is not valid input."
NEW_GAME = 'New Game'
LOAD_GAME = 'Load Game'
SAVE_GAME = 'Save Game'
PLAY = 'Play'
OPTIONS = "Options"
BACK = 'Back'
EXIT = ["Exit", "Quit", "Leave", "Done"]
NAME = "Pokemon SV"
VERSION = "0.1"
#
#
#
def load_player(playername):
    return load_trainer(playername, "players/")
#
def save_player(player):
    save_trainer(player, "players/")
#
def print_main_menu_options():
    while True:
        print OPTIONS+":"
        print BACK
        cmd = raw_input('Select an option: ')
        if cmd.lower() in BACK.lower():
            break
        else:
            print INPUT_ERROR.format(cmd)
    return BACK
def print_main_menu(player):
    print NEW_GAME
    print LOAD_GAME
    if player is not None:
        print SAVE_GAME
        print PLAY
    print OPTIONS
    print EXIT[0]

def main():
    clear()
    player = None
    while True:
        clear()
        print " --- Welcome to {} VERSION {}! --- \n".format(NAME, VERSION)
        if player is not None:
            print "Current player:"
            print player.get_from_load()
        print_main_menu(player)
        cmd = raw_input('Select an option: ')
        if cmd.lower() in NEW_GAME.lower():
            print NEW_GAME
            print "Starting game with {} .... test".format("New Player") # play_new_game(player=None)
            pause()
        elif cmd.lower() in LOAD_GAME.lower():
            print LOAD_GAME
            game_files = get_files_in_directory("players/")
            for game_file in game_files:
                game_file_name = game_file.split('.')[0]
                print "- "+game_file_name
                check_trainer(game_file_name,"players/")
                
            cmd = raw_input('Select a game file: ')
            for game_file in game_files:
                if cmd.lower() in game_file.lower():
                    fame_file_name = game_file.split('.')[0]
                    player = load_player(fame_file_name)
        elif cmd.lower() in PLAY.lower():
            print PLAY
            print "Starting game with {}.... test".format(player.name) # play_new_game(player=player)
            pause()
        elif cmd.lower() in SAVE_GAME.lower():
            print SAVE_GAME
            print "Saving Game... Do not Exit!"
            pause()
            save_player(player)
            print "Game saved!"
            pause()
        elif cmd.lower() in OPTIONS.lower():
            print OPTIONS
            option = print_main_menu_options()
            if option is BACK:
                print option
        else:
            for exit_opt in EXIT:
                if cmd.lower() in exit_opt.lower():
                    print EXIT[0]
                    sys.exit(0)
            print INPUT_ERROR.format(cmd)
#
main()
#
