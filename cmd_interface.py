#
import os
import sys
import time
from constants import constants
from trainer import trainer
from trainerclass import *
from inventory import *
from trainer_pokemon_dicts import *
from utilities import *
from pokemon_dicts import *
from moves import *
from pokemon import pokemon
from pokedex import pokedex

petc = lambda: raw_input("Press Enter to Continue...")
clear = lambda: os.system('cls')

class cmd_interface():
    input_error_text = "ERROR: {} is not valid input."
    text_speed = 0.025
    #SELECTION UI
    #
    def verify_answer(self, prompt=None):
        if prompt is None:
            print "No Text in prompt to Verify Answer."
            return None
        while True:
            cmd = raw_input(prompt + " (yes/no): ")
            if 'y' in cmd.lower() or '' in cmd.lower():
                return True
            elif 'n' in cmd.lower():
                return False
            else:
                print input_error_text.format(cmd)
    #
    def choose_pokemon_from_list(self, pokemon_list=None):
        if pokemon_list is None:
            return None
        while True:
            index = 0
            for pokemon in pokemon_list:
                index += 1
                print "{}: {}".format(index, pokemon.get_pokemon_basic_stats())
            
            cmd = raw_input("Choose a pokemon (by number or name): ")
            number = get_int_from_string(cmd)
            if is_int(number):
                #print "by number: {}".format(number)
                return pokemon_list[cmd-1]
            else:
                #print "by name: {}".format(cmd)
                for pokemon in pokemon_list:
                    if cmd.lower() in pokemon.nickname.lower():
                        #print pokemon.nickname
                        return pokemon
            print cmd
            print "Input is not valud, choose a number or type the name of the pokemon."
    #BATTLE UI
    def choose_battle_option(self, trainer=None, pokemon=None, opposing_pokemon=None, options=None):#, priority_list=None):
        #
        if pokemon is None:
            print "No pokemon.  Pokemon is None."
            return None
        #if priority_list is None:
        #    print "Priority list is none."
        #    return None
        if options is None:
            options = [constants.btl_opt_attack]
        option = None
        #
        while True:
            if len(options) > 1:
                print "What will {} do?".format(pokemon.nickname)
                for opt in options:
                    print opt
                cmd = raw_input("Choose an option: ")
                #ATTACK
                if cmd.lower() in constants.btl_opt_attack.lower() and constants.btl_opt_attack in options:
                    #ATTACK PRIORITTY -7 to 8
                    move = self.choose_attack(pokemon=pokemon)
                    if move is 'back':
                        continue
                    if pokemon.has_status_effect(constants.status_bide):
                        move = move # dont use 
                    else:
                        pokemon.use_move(move)
                    return {constants.btl_opt_attack: move, 'priority': str(move.priority), 'pokemon': pokemon, 'trainer': trainer, 'target':opposing_pokemon} 
                    
                #Pokemon
                elif cmd.lower() in constants.btl_opt_pokemon.lower() and constants.btl_opt_pokemon in options:
                    #Pokemon PRIORITTY 6
                    new_pokemon = self.choose_pokemon(trainer=trainer)
                    if new_pokemon is 'back':
                        continue
                    if pokemon.has_status_effect(status_effect=constants.status_trapped): # Is Trapped
                        print "{} is trapped and cannot escape".format(pokemon.nickname)
                        continue
                    return {constants.btl_opt_switch: new_pokemon, 'priority': '6', 'pokemon': pokemon, 'trainer': trainer} 
                #Items
                elif cmd.lower() in constants.btl_opt_items.lower() and constants.btl_opt_items in options:
                    #Items PRIORITTY 6
                    item = self.choose_item(trainer=trainer)
                    if item is 'back':
                        continue
                    elif (item.type is constants.item_type_medicine or item.type is constants.item_type_berry):
                        wanted_pokemon = self.choose_pokemon_from_list(pokemon_list=trainer.party)
                        if wanted_pokemon is None or (wanted_pokemon.is_fainted() and "Revive" not in item.name):
                            print "You cannot use {} that pokemon!".format(item.name)
                            continue
                        return {constants.btl_opt_items: item, 'priority': '6', 'pokemon': wanted_pokemon, 'trainer': trainer} 
                    elif item.type is constants.item_type_poke_ball:
                        if opposing_pokemon.original_trainer is None:
                            return {constants.btl_opt_items: item, 'priority': '6', 'pokemon': pokemon, 'trainer': trainer, 'target':opposing_pokemon} 
                        else:
                            print "Dont be a theif.  Only catch WILD Pokemon."
                            continue
                    else:
                        print "You cannot use that {} now!".format(item.name)
                        continue
                #Call
                elif cmd.lower() in constants.btl_opt_call.lower() and constants.btl_opt_call in options:
                    #Call PRIORITTY 6
                    return {constants.btl_opt_call: pokemon, 'priority': '6', 'pokemon': pokemon, 'trainer': trainer} 
                #Flee
                elif cmd.lower() in constants.btl_opt_flee.lower() and constants.btl_opt_flee in options:
                    #Flee PRIORITTY 0, 
                    if cmd.lower()  is 'back':
                        continue
                    priority = 6
                    if trainer is None:
                        priority = 0
                    return {constants.btl_opt_flee: constants.btl_opt_flee, 'priority': '6', 'pokemon': pokemon, 'trainer': trainer} 
                #
                else:
                    print self.input_error_text.format(cmd)
                    continue
    #
    def choose_attack(self, pokemon=None):
        if pokemon is None:
            return None
        if pokemon.has_status_effect(constants.status_bide):
            return pokemon.get_move(move_name="Bide")
        if pokemon.has_status_effect(constants.status_encore):
            return pokemon.get_status_effect(constants.status_encore)[constants.status_encore]
        print "choose_attack\n"
        while True:
            for move in pokemon.moves:
                print str(move)
            cmd = raw_input("\nChoose move: ")
            if cmd in 'back' or cmd in 'cancel':
                return 'back'
            for move in pokemon.moves:
                if cmd.lower() in move.name.lower():
                    if move.pp > 0:
                        if not (pokemon.has_status_effect(constants.disables_move) and pokemon.get_status_effect(constants.disables_move)[constants.disables_move].name is move.name):
                            return move
                        else:
                            print "{} is disabled!".format(move.name)
                            continue
                    else:
                        print "{} has no pp left!".format(move.name)
                        continue
            print self.input_error_text.format(cmd)
    #
    def choose_pokemon(self, trainer=None):
        if trainer is None:
            return None
        #print "choose_pokemon"
        while True:
            for pokemon in trainer.party:
                print pokemon.get_from_party()
            cmd = raw_input("\nChoose Option (Switch, Summary, Cancel): \n")
            if cmd.lower() in 'back' or cmd.lower()  in 'cancel' or cmd.lower()  in 'return' or cmd.lower()  is '':
                return 'back'
            elif cmd.lower()  in "switch" or cmd.lower()  in "exchange" or cmd.lower()  in "swift" or cmd.lower()  in "trade":
                print "switch"
                cmd = raw_input("\nChoose Pokemon: \n")
                for pokemon in trainer.party:
                    if cmd.lower() in pokemon.nickname.lower():
                        print pokemon.nickname
                        if not pokemon.is_fainted():
                            return pokemon
                        else:
                            print "{} has no will to fight!".format(pokemon.name)
            elif cmd in "summary" or cmd in "look" or cmd in "see" or cmd in "inspect":
                cmd = raw_input("\nChoose Pokemon: \n")
                for pokemon in trainer.party:
                    if cmd.lower() in pokemon.nickname.lower():
                        print pokemon.get_pokemon_info()
                        return 'back'
            else:
                print self.input_error_text.format(cmd)
    #
    def choose_item(self, trainer=trainer): 
        if trainer is None:
            return None
        #print "choose_item"
        while True:
            print trainer.get_pack(pocket=constants.item_type_medicine)
            print trainer.get_pack(pocket=constants.item_type_poke_ball)
            print trainer.get_pack(pocket=constants.item_type_berry)
            cmd = raw_input("Choose Item to use: ")
            if cmd in 'back' or cmd in 'cancel':
                return 'back'
            item = trainer.get_item(cmd)
            print item
            if item is not None:
                return item
            print self.input_error_text.format(cmd)
    #Capture Pokemon
    def attempt_capture_of_pokemon(self, trainer=None, ball=None, pokemon=None):
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
    #POKEMON
    def rename_pokemon(self, pokemon=None):
        if pokemon is None:
            return
        cmd = raw_input("Want to rename your pokemon? >>>")
        if "y" in cmd.lower():
            old_name = pokemon.nickname
            print old_name
            name = raw_input("Rename {} to: ".format(old_name))
            if self.verify_answer("Are you sure you want to change {}'s name to {}?".format(old_name, name)):
                pokemon.nickname = name
                print "{} will now be called {}".format(old_name, pokemon.nickname)
                return
        else:
            return
    #AI
    def ai_choose_battle_option(self, trainer=None, pokemon=None, options=None, priority_list=None):
        self.choose_battle_option(trainer=trainer, pokemon=pokemon, options=options, priority_list=priority_list)
    #
    #
    #dialog
    def delay_print(self, s):
        for c in s:
            sys.stdout.write('%s' % c )
            sys.stdout.flush()
            time.sleep(self.text_speed)
    def actions_with_delay(self, text=None):
        if text is None:
            return   
        self.delay_print("~{0}~\n\n".format(text))
    def character_speech(self, trainer=None, text=None):
        if trainer is None:
            return
        if text is None:
            return   
        dialog_str = "{0}: \"{1}\"\n\n".format(trainer.name, text)
        print dialog_str
    def character_speech_with_delay(self, trainer=None, text=None):
        if trainer is None:
            return
        if text is None:
            return   
        #print "{0}:".format(trainer.name)
        #dialog_str = "\"{0}\"\n".format(text)
        dialog_str = "{0}: \"{1}\"\n\n".format(trainer.name, text)
        self.delay_print(dialog_str)
    def character_thoughts(self, trainer=None, text=None):
        if trainer is None:
            return
        if text is None:
            return   
        dialog_str = "\n{0}: \'{1}\'\n\n".format(trainer.name, text)
        print dialog_str    
    def character_thoughts_with_delay(self, trainer=None, text=None):
        if trainer is None:
            return
        if text is None:
            return   
        #print "{0}:".format(trainer.name)
        dialog_str = "{0}: '{1}'\n\n".format(trainer.name, text)
        self.delay_print(dialog_str)   
    #
    #
    #
    #
    #
    #
    #
#
#
#