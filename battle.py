import os
import time
import sys
from decimal import *
from utilities import *
from random import randint
#
from constants import constants
from trainer import trainer
from pokemon import pokemon
from cmd_interface import cmd_interface
#
clear = lambda: os.system('cls')
petc = lambda: raw_input("Press Enter to Continue...")
pause_long = lambda: time.sleep(1)
pause = lambda: time.sleep(0.25)
wfu = lambda: raw_input(">|")

class battle():
    console = cmd_interface()
    def clear_battle_priority(self, battle_priority=None):
        if battle_priority is None:
            return {'8': [], '7': [], '6': [], '5': [], '4': [], '3': [], '2': [], '1': [], '0': [], '-1': [], '-2': [], '-3': [], '-4': [], '-5': [], '-6': [], '-7': []}
        #for key in constants.priority_list_keys: #for each priority
        #    for battle_move in battle_priority[key]
                
        
        del battle_priority
        battle_priority = {'8': [], '7': [], '6': [], '5': [], '4': [], '3': [], '2': [], '1': [], '0': [], '-1': [], '-2': [], '-3': [], '-4': [], '-5': [], '-6': [], '-7': []}
        return battle_priority
        
    def __init_(self):
        self.trainer_team_1 = []
        self.trainer_team_2 = []
        self.rules = "Wild Pokemon Battle"
    def wild_pokemon_battle(self, trainer_1=None, trainer_2=None, wild_pokemon=None):
        clear()
        #print "*** In Trainer (Singles) Battle ***\n"
        console = self.console
        if  trainer_1 is None:
            print "Trainer 1 is None"
            return "Trainer 1 is None"
        if  wild_pokemon is None:
            print "wild_pokemon is None"
            return "wild_pokemon is None"
        battle_participants = []
        battle_priority = None
        t1ap = None
        t2ap = wild_pokemon
        #print "\n\n{} {} would like to battle!".format(trainer_2.trainer_class.name, trainer_2.name)
        #
        print "*** In Wild Battle vs. {} ***\n\n{} Select First Pokemon:\n".format(t2ap.name, trainer_1.name)
        t1ap = console.choose_pokemon_from_list(pokemon_list=trainer_1.get_able_party_members_as_list())
        #petc()
        clear()
        #print "*** In Trainer (Singles) Battle ***\n\n{} Select First Pokemon:\n".format(trainer_2.name)
        #t2ap = console.choose_pokemon_from_list(pokemon_list=trainer_2.get_able_party_members_as_list())
        self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
        self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_2, active_pokemon=t2ap, opponent_pokemon=t1ap)

        clear()
        console.character_speech(trainer_1, "Look! A wild {}!".format(t2ap.name))
        print "A wild {} appeared!\n".format(t2ap.name)
        pause()
        print "{0} sent out {1}.  \n".format(trainer_1.name, t1ap.nickname)
        console.character_speech(trainer_1, "Go {}!".format(t1ap.nickname))
        pause()
        #print "{0} sent out {1}.  \n".format(trainer_2.name, t2ap.nickname)
        #console.character_speech(trainer_2, "Go {}!".format(t2ap.nickname))
        #pause()
        #petc()
        # return
        while True:
            del battle_priority
            battle_priority = {'8': [], '7': [], '6': [], '5': [], '4': [], '3': [], '2': [], '1': [], '0': [], '-1': [], '-2': [], '-3': [], '-4': [], '-5': [], '-6': [], '-7': []}
            print " --------------------------------------- "
            print trainer_1.name
            print t1ap.get_from_party()
            print " ------------------- "
            #print trainer_2.name
            print t2ap.get_from_party()
            print " --------------------------------------- \n"
            # { [ {constants.btl_opt_attack: move, 'priority': move.priority, 'pokemon': pokemon}, {constants.btl_opt_attack: move, 'priority': move.priority, 'pokemon': pokemon} ] }
            # { [ {constants.btl_opt_pokemon: new_pokemon, 'priority': 6, 'pokemon': pokemon}               ] }
            # { [ {constants.btl_opt_items: item, 'priority': 6, 'pokemon': pokemon}                        ] }
            # { [ {constants.btl_opt_call: pokemon, 'priority': 6, 'pokemon': pokemon}                      ] }
            # { [ {constants.btl_opt_flee: constants.btl_opt_flee, 'priority': 6 or 0, 'pokemon': pokemon}  ] }
            trainer_1_option = console.choose_battle_option(trainer=trainer_1, pokemon=t1ap, opposing_pokemon=t2ap, options=constants.encounter_options)#, priority_list=battle_priority)
            #print ""
            if trainer_1_option is not None:
                battle_priority[trainer_1_option.get('priority')].append(trainer_1_option)
                #print ""
                #for key in trainer_option.keys():
                #    print "{}: {}".format(key, trainer_option[key])
            else:
                print "trainer_1_option is: {}".format(trainer_1_option)
                return 1
            #
            print ""
            wild_pokemon_option = console.choose_battle_option(trainer=trainer_2, pokemon=t2ap, opposing_pokemon=t1ap, options=constants.wild_pokemon_options)#, priority_list=battle_priority)
            if wild_pokemon_option is not None:
                battle_priority[wild_pokemon_option.get('priority')].append(wild_pokemon_option)
                print ""
                #for key in wld_pkm_option.keys():
                #    print "{}: {}".format(key, wld_pkm_option[key])
            else:
                print "wild_pokemon_option is: {}".format(wild_pokemon_option)
                return 1
            print ""
            for key in constants.priority_list_keys: #for each priority

                if len(battle_priority[key]) > 1: # if there is more then 1 move in the priority slot
                    who_go_first = 0
                    pkm_1_speed = t1ap.get_speed()
                    pkm_2_speed = t2ap.get_speed()
                    if pkm_1_speed == pkm_2_speed:
                        who_go_first = self.break_speed_tie()
                    # Trainer Pokemon Faster
                    if pkm_1_speed+who_go_first > pkm_2_speed:
                        # Perform Actions
                        action = None
                        action_text = None
                        for battle_move in battle_priority[key]: # for each battle move in priority
                            if t1ap is battle_move.get('pokemon'):
                                action = battle_move
                                break
                        action_text = self.perform_action(action=action, trainer_1=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
                        if "SWITCH" is action_text: 
                            console.character_speech(trainer_1, "{} return!".format(t1ap.nickname))
                            print "{} withdrew {}.\n".format(trainer_1.name, t1ap.nickname)
                            t1ap = battle_move.get(constants.btl_opt_switch)
                            self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
                            print "{0} sent out {1}.\n".format(trainer_1.name, t1ap.nickname)
                            console.character_speech(trainer_1, "Go {}!".format(t1ap.nickname))
                        if action_text in "BATTLE OVER":
                            #print "FOUND BATTLE OVER!"
                            return
                        pause()
                        if not t2ap.is_fainted():
                            action = None
                            for battle_move in battle_priority[key]: # for each battle move in priority
                                #print battle_move
                                if t2ap is battle_move.get('pokemon'):
                                    action = battle_move
                                    break
                            action_text = self.perform_action(action=action, trainer_1=trainer_2, active_pokemon=t2ap, opponent_pokemon=t1ap)
                            #print "action is: {}".format(action)
                            if action_text in "BATTLE OVER":
                                #print "FOUND BATTLE OVER!"
                                return
                            petc()
                    # Opponent Pokemon Faster 
                    elif pkm_1_speed+who_go_first < pkm_2_speed:
                        #print "\nactive_pokemon.speed < wild_pokemon.speed"
                        for battle_move in battle_priority[key]: # for each battle move in priority
                             #print battle_move
                             if t2ap is battle_move.get('pokemon'):
                                action = battle_move
                                break
                        action_text = self.perform_action(action=action, trainer_1=trainer_2, active_pokemon=t2ap, opponent_pokemon=t1ap)
                        #print "action is: {}".format(action)
                        
                        if action_text in "BATTLE OVER":
                            #print "FOUND BATTLE OVER!"
                            return
                        pause()
                        if not t1ap.is_fainted():
                            action = None
                            for battle_move in battle_priority[key]: # for each battle move in priority
                                 #print battle_move
                                 if t1ap is battle_move.get('pokemon'):
                                    action = battle_move
                                    break
                            action_text = self.perform_action(action=action, trainer_1=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
                            #print "action is: {}".format(action)
                            if "SWITCH" is action_text: 
                                console.character_speech(trainer_1, "{} return!".format(t1ap.nickname))
                                print "{} withdrew {}.\n".format(trainer_1.name, t1ap.nickname)
                                t1ap = battle_move.get(constants.btl_opt_switch)
                                self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
                                print "{0} sent out {1}.\n".format(trainer_1.name, t1ap.nickname)
                                console.character_speech(trainer_1, "Go {}!".format(t1ap.nickname))
                            if action_text in "BATTLE OVER":
                                #print "FOUND BATTLE OVER!"
                                return
                            petc()
                    #Only one in priority slot, act
                else:
                    if len(battle_priority[key]) > 0:
                        #Perform Actions
                        #print battle_move
                        action = None
                        action_text = None
                        if not battle_priority[key][0].get('pokemon').is_fainted():
                            acting_trainer = battle_priority[key][0].get('trainer')
                            action = battle_priority[key][0]
                            acting_pokemon = battle_priority[key][0].get('pokemon')
                            target_pokemon = battle_priority[key][0].get('target')
                            if target_pokemon is not t1ap or target_pokemon is not t2ap:
                                if target_pokemon is not t1ap and t1ap is not acting_pokemon:
                                    target_pokemon = t1ap
                                elif target_pokemon is not t2ap and t2ap is not acting_pokemon:
                                    target_pokemon = t2ap
                            
                            action_text = self.perform_action(action=action, 
                            trainer_1=acting_trainer, 
                            active_pokemon=acting_pokemon,
                            opponent_pokemon=target_pokemon
                            )
                            print "action_text is: {}".format(action_text)
                            if "SWITCH" in action_text: 
                                #print "SWITCH"
                                if acting_pokemon is t1ap:
                                    console.character_speech(trainer_1, "{} return!".format(t1ap.nickname))
                                    print "{} withdrew {}.\n".format(trainer_1.name, t1ap.nickname)
                                    t1ap = battle_priority[key][0].get(constants.btl_opt_switch)
                                    self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
                                    print "{0} sent out {1}.\n".format(trainer_1.name, t1ap.nickname)
                                    console.character_speech(trainer_1, "Go {}!".format(t1ap.nickname))
                                #if acting_pokemon is t2ap:
                                #    console.character_speech(trainer_2, "{} return!".format(t2ap.nickname))
                                #    print "{} withdrew {}.\n".format(trainer_2.name, t2ap.nickname)
                                #    t2ap = battle_priority[key][0].get(constants.btl_opt_switch)
                                #    self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_2, active_pokemon=t2ap, opponent_pokemon=t1ap)
                                #    print "{0} sent out {1}.\n".format(trainer_2.name, t2ap.nickname)
                                #    console.character_speech(trainer_2, "Go {}!".format(t2ap.nickname))
                            if action_text in "BATTLE OVER":
                                #print "FOUND BATTLE OVER!"
                                return
                            pause()
                    else:
                        pass
                        #print battle_priority[key]
                            
                            
            # Resolve fainted pokemon
            # trainer pokemon is fainted
            if t1ap.is_fainted():
                print "{} fainted!".format(t1ap.nickname)
                console.character_speech(trainer_1, "{} return!".format(t1ap.nickname))
                pause()
                print "{} withdrew {}.".format(trainer_1.name, t1ap.nickname)
                self.award_experience_points_to_participants(fainted_pokemon=t2ap, battle_participants=battle_participants)
                pause()
                if trainer_1.able_pokemon() > 0:
                    # choose pokemon
                    new_pokemon = None
                    new_pokemon = console.choose_pokemon_from_list(pokemon_list=trainer_1.get_able_party_members_as_list())
                    t1ap = new_pokemon
                    print "{0} sent out {1}. Go {1}!".format(trainer_1.name, t1ap.nickname)
                    pause()
                else:
                    print "{} is out of pokemon!".format(trainer_1.name)
                    break
            # opponent trainer pokemon is fainted
            if t2ap.is_fainted():
                print "{} was defeated!".format(t2ap.nickname)
                #console.character_speech(trainer_2, "{} return!".format(t2ap.nickname))
                pause()
                #print "{} withdrew {}.".format(trainer_2.name, t2ap.nickname)
                self.award_experience_points_to_participants(fainted_pokemon=t2ap, battle_participants=battle_participants)
                break
            if "BATTLE OVER" in action:
                break
        return
    def trainer_pokemon_battle(self, trainer_1=None, trainer_2=None):
        clear()
        #print "*** In Trainer (Singles) Battle ***\n"
        console = self.console
        if  trainer_1 is None:
            print "Trainer 1 is None"
            return "Trainer 1 is None"
        if  trainer_2 is None:
            print "Trainer 2 is None"
            return "Trainer 2 is None"
        battle_participants = []
        battle_priority = None
        t1ap = None
        t2ap = None
        #print "\n\n{} {} would like to battle!".format(trainer_2.trainer_class.name, trainer_2.name)
        #
        print "*** In Trainer (Singles) Battle ***\n\n"
        if len(trainer_1.get_able_party_members_as_list()) > 1:
            print "{} Select First Pokemon:\n".format(trainer_1.name)
            t1ap = console.choose_pokemon_from_list(pokemon_list=trainer_1.get_able_party_members_as_list())
            petc()
        else:
            t1ap = trainer_1.get_first_able_pokemon_from_party()
        
        clear()
        print "*** In Trainer (Singles) Battle ***\n\n"
        if len(trainer_2.get_able_party_members_as_list()) > 1:
            print "{} Select First Pokemon:\n".format(trainer_2.name)
            t2ap = console.choose_pokemon_from_list(pokemon_list=trainer_2.get_able_party_members_as_list())
            petc()
        else:
            t2ap = trainer_2.get_first_able_pokemon_from_party()
        self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
        self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_2, active_pokemon=t2ap, opponent_pokemon=t1ap)

        clear()
        console.character_speech(trainer_1, "Let's battle!")
        console.character_speech(trainer_2, "You're On!")
        print "{} {} would like to battle!\n".format(trainer_2.trainer_class.name, trainer_2.name)
        pause()
        print "{0} sent out {1}.  \n".format(trainer_1.name, t1ap.nickname)
        console.character_speech(trainer_1, "Go {}!".format(t1ap.nickname))
        pause()
        print "{0} sent out {1}.  \n".format(trainer_2.name, t2ap.nickname)
        console.character_speech(trainer_2, "Go {}!".format(t2ap.nickname))
        pause()
        #petc()
        # return
        while True:
            battle_priority = self.clear_battle_priority(battle_priority=battle_priority)
            print " --------------------------------------- "
            print trainer_1.name
            print t1ap.get_from_party()
            print " ------------------- "
            print trainer_2.name
            print t2ap.get_from_party()
            print " --------------------------------------- \n"
            # { [ {constants.btl_opt_attack: move, 'priority': move.priority, 'pokemon': pokemon}, {constants.btl_opt_attack: move, 'priority': move.priority, 'pokemon': pokemon} ] }
            # { [ {constants.btl_opt_pokemon: new_pokemon, 'priority': 6, 'pokemon': pokemon}               ] }
            # { [ {constants.btl_opt_items: item, 'priority': 6, 'pokemon': pokemon}                        ] }
            # { [ {constants.btl_opt_call: pokemon, 'priority': 6, 'pokemon': pokemon}                      ] }
            # { [ {constants.btl_opt_flee: constants.btl_opt_flee, 'priority': 6 or 0, 'pokemon': pokemon}  ] }
            trainer_1_option = console.choose_battle_option(trainer=trainer_1, pokemon=t1ap, opposing_pokemon=t2ap, options=constants.encounter_options)#, priority_list=battle_priority)
            trainer_2_option = console.choose_battle_option(trainer=trainer_2, pokemon=t2ap, opposing_pokemon=t1ap, options=constants.encounter_options)#, priority_list=battle_priority)
            # PUT PURSUIT CODE HERE
            
            #print ""
            if trainer_1_option is not None:
                battle_priority[trainer_1_option.get('priority')].append(trainer_1_option)
                #print ""
                #for key in trainer_option.keys():
                #    print "{}: {}".format(key, trainer_option[key])
            else:
                print "trainer_1_option is: {}".format(trainer_1_option)
                return 1
            #
            print ""
            trainer_2_option = console.choose_battle_option(trainer=trainer_2, pokemon=t2ap, opposing_pokemon=t1ap, options=constants.encounter_options)#, priority_list=battle_priority)
            if trainer_2_option is not None:
                battle_priority[trainer_2_option.get('priority')].append(trainer_2_option)
                print ""
                #for key in wld_pkm_option.keys():
                #    print "{}: {}".format(key, wld_pkm_option[key])
            else:
                print "trainer_2_option is: {}".format(trainer_2_option)
                return 1
            print ""
            for key in constants.priority_list_keys: #for each priority

                if len(battle_priority[key]) > 1: # if there is more then 1 move in the priority slot
                    who_go_first = 0
                    pkm_1_speed = t1ap.get_speed()
                    pkm_2_speed = t2ap.get_speed()
                    if pkm_1_speed == pkm_2_speed:
                        who_go_first = self.break_speed_tie()
                    # Trainer Pokemon Faster
                    if pkm_1_speed+who_go_first > pkm_2_speed:
                        # Perform Actions
                        action = None
                        action_text = None
                        for battle_move in battle_priority[key]: # for each battle move in priority
                            if t1ap is battle_move.get('pokemon'):
                                action = battle_move
                                break
                        action_text = self.perform_action(action=action, trainer_1=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
                        if "SWITCH" is action_text: 
                            console.character_speech(trainer_1, "{} return!".format(t1ap.nickname))
                            print "{} withdrew {}.\n".format(trainer_1.name, t1ap.nickname)
                            t1ap = battle_move.get(constants.btl_opt_switch)
                            self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
                            print "{0} sent out {1}.\n".format(trainer_1.name, t1ap.nickname)
                            console.character_speech(trainer_1, "Go {}!".format(t1ap.nickname))
                        if "BATTLE OVER" in action_text:
                            break
                        pause()
                        if not t2ap.is_fainted():
                            action = None
                            for battle_move in battle_priority[key]: # for each battle move in priority
                                #print battle_move
                                if t2ap is battle_move.get('pokemon'):
                                    action = battle_move
                                    break
                            action_text = self.perform_action(action=action, trainer_1=trainer_2, active_pokemon=t2ap, opponent_pokemon=t1ap)
                            #print "action is: {}".format(action)
                            if "SWITCH" is action_text: 
                                console.character_speech(trainer_2, "{} return!".format(t2ap.nickname))
                                print "{} withdrew {}.\n".format(trainer_2.name, t2ap.nickname)
                                t2ap = battle_move.get(constants.btl_opt_switch)
                                self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_2, active_pokemon=t2ap, opponent_pokemon=t1ap)
                                print "{0} sent out {1}.\n".format(trainer_2.name, t2ap.nickname)
                                console.character_speech(trainer_2, "Go {}!".format(t2ap.nickname))
                            if "BATTLE OVER" in action_text:
                                break
                    # Opponent Pokemon Faster 
                    elif pkm_1_speed+who_go_first < pkm_2_speed:
                        #print "\nactive_pokemon.speed < wild_pokemon.speed"
                        for battle_move in battle_priority[key]: # for each battle move in priority
                             #print battle_move
                             if t2ap is battle_move.get('pokemon'):
                                action = battle_move
                                break
                        action = self.perform_action(action=action, trainer_1=trainer_2, active_pokemon=t2ap, opponent_pokemon=t1ap)
                        #print "action is: {}".format(action)
                        if "SWITCH".lower() is action.lower(): 
                            console.character_speech(trainer_2, "{} return!".format(t2ap.nickname))
                            print "{} withdrew {}.\n".format(trainer_2.name, t2ap.nickname)
                            t2ap = battle_move.get(constants.btl_opt_switch)
                            self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_2, active_pokemon=t2ap, opponent_pokemon=t1ap)
                            print "{0} sent out {1}.\n".format(trainer_2.name, t2ap.nickname)
                            console.character_speech(trainer_2, "Go {}!".format(t2ap.nickname))
                        
                        if "BATTLE OVER".lower() in action.lower():
                            break
                        pause()
                        if not t1ap.is_fainted():
                            action = None
                            for battle_move in battle_priority[key]: # for each battle move in priority
                                 #print battle_move
                                 if t1ap is battle_move.get('pokemon'):
                                    action = battle_move
                                    break
                            action_text = self.perform_action(action=action, trainer_1=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
                            #print "action is: {}".format(action)
                            if "SWITCH" is action_text: 
                                console.character_speech(trainer_1, "{} return!".format(t1ap.nickname))
                                print "{} withdrew {}.\n".format(trainer_1.name, t1ap.nickname)
                                t1ap = battle_move.get(constants.btl_opt_switch)
                                self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
                                print "{0} sent out {1}.\n".format(trainer_1.name, t1ap.nickname)
                                console.character_speech(trainer_1, "Go {}!".format(t1ap.nickname))
                            if "BATTLE OVER" in action_text:
                                break
                    #Only one in priority slot, act
                else:
                    if len(battle_priority[key]) > 0:
                        #Perform Actions
                        #print battle_move
                        action = None
                        action_text = None
                        if not battle_priority[key][0].get('pokemon').is_fainted():
                            acting_trainer = battle_priority[key][0].get('trainer')
                            action = battle_priority[key][0]
                            acting_pokemon = battle_priority[key][0].get('pokemon')
                            target_pokemon = battle_priority[key][0].get('target')
                            if target_pokemon is not t1ap or target_pokemon is not t2ap:
                                if target_pokemon is not t1ap and t1ap is not acting_pokemon:
                                    target_pokemon = t1ap
                                elif target_pokemon is not t2ap and t2ap is not acting_pokemon:
                                    target_pokemon = t2ap
                            
                            action_text = self.perform_action(action=action, 
                            trainer_1=acting_trainer, 
                            active_pokemon=acting_pokemon,
                            opponent_pokemon=target_pokemon
                            )
                            #print "action_text is: {}".format(action_text)
                            if "SWITCH" in action_text: 
                                #print "SWITCH"
                                if acting_pokemon is t1ap:
                                    console.character_speech(trainer_1, "{} return!".format(t1ap.nickname))
                                    print "{} withdrew {}.\n".format(trainer_1.name, t1ap.nickname)
                                    t1ap = battle_priority[key][0].get(constants.btl_opt_switch)
                                    self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_1, active_pokemon=t1ap, opponent_pokemon=t2ap)
                                    print "{0} sent out {1}.\n".format(trainer_1.name, t1ap.nickname)
                                    console.character_speech(trainer_1, "Go {}!".format(t1ap.nickname))
                                if acting_pokemon is t2ap:
                                    console.character_speech(trainer_2, "{} return!".format(t2ap.nickname))
                                    print "{} withdrew {}.\n".format(trainer_2.name, t2ap.nickname)
                                    t2ap = battle_priority[key][0].get(constants.btl_opt_switch)
                                    self.add_pokemon_to_participants(battle_participants=battle_participants, trainer=trainer_2, active_pokemon=t2ap, opponent_pokemon=t1ap)
                                    print "{0} sent out {1}.\n".format(trainer_2.name, t2ap.nickname)
                                    console.character_speech(trainer_2, "Go {}!".format(t2ap.nickname))
                            if "BATTLE OVER" in action:
                                break
                            pause()
                    else:
                        pass
                        #print battle_priority[key]
                            
            # Resolve Persisting status effects
            self.resolve_persisting_effects(pokemon=t1ap)
            self.resolve_persisting_effects(pokemon=t2ap)
            petc()
            # Resolve fainted pokemon
            # trainer pokemon is fainted
            if t1ap.is_fainted():
                print "{} fainted!".format(t1ap.nickname)
                console.character_speech(trainer_1, "{} return!".format(t1ap.nickname))
                pause()
                print "{} withdrew {}.".format(trainer_1.name, t1ap.nickname)
                self.award_experience_points_to_participants(fainted_pokemon=t2ap, battle_participants=battle_participants)
                pause()
                if trainer_1.able_pokemon() > 0:
                    # choose pokemon
                    new_pokemon = None
                    new_pokemon = console.choose_pokemon_from_list(pokemon_list=trainer_1.get_able_party_members_as_list())
                    t1ap = new_pokemon
                    print "{0} sent out {1}. Go {1}!".format(trainer_1.name, t1ap.nickname)
                    pause()
                else:
                    print "{} is out of pokemon!".format(trainer_1.name)
                    break
            # opponent trainer pokemon is fainted
            if t2ap.is_fainted():
                print "{} fainted!".format(t2ap.nickname)
                console.character_speech(trainer_2, "{} return!".format(t2ap.nickname))
                pause()
                print "{} withdrew {}.".format(trainer_2.name, t2ap.nickname)
                self.award_experience_points_to_participants(fainted_pokemon=t2ap, battle_participants=battle_participants)
                pause()
                if trainer_2.able_pokemon() > 0:
                    # choose pokemon
                    new_pokemon = None
                    new_pokemon = console.choose_pokemon_from_list(pokemon_list=trainer_2.get_able_party_members_as_list())
                    t2ap = new_pokemon
                    print "{0} sent out {1}. Go {1}!".format(trainer_2.name, t2ap.nickname)
                    pause()
                else:
                    print "{} is out of pokemon!".format(trainer_2.name)
                    break
            if "BATTLE OVER" in action:
                break
        return   
    def is_crit(self, attacker, move):
        max = 10000
        min = 00001
        roll = randint(min, max)
        #print "Roll {}%, Percentage {}%".format(roll/100.0, (10000 - crit_s1)/100.0)
        if roll >= max - int(attacker.get_crit_stage()*100):
            return True
        return False
    def does_hit(self, attacker, defender, move):
        #return True
        min = 1
        max = 100
        roll = randint(min,max)
        if (move.type.name is 'Ground' and defender.ability.name is 'Levitate'):
            return False
        if (move.name is "Sleep Talk" or move.name is "Snore") and not attacker.has_status_effect(constants.status_sleep):
            return False
        if move.accuracy is None:
            return True
        print "roll {}".format(roll)
        if move.has_effect(constants.one_hit_ko):
            chance = attacker.level - defender.level + 30
            print "chance {}".format(chance)
            if roll <= chance:
                print "One-Hit-KO Hits"
                return True
            else:
                print "One-Hit-KO misses"
                return False
        probability = int(move.accuracy * (attacker.get_accuracy_stage() / defender.get_evasion_stage()))
        print "probability {}".format(probability)
        if roll >= max - int(round(probability)):
            print "DOES HIT"
            return True
        return False
    def calculate_damage(self, attacker=None, defender=None, move=None, guaranteed_hit=False, team=None):
        #Damage = ((((2 * Level / 5 + 2) * AttackStat * AttackPower / DefenseStat) / 50) + 2) * STAB * Weakness/Resistance * RandomNumber / 100
        #Let me explain all the variables first. Damage is, well, damage, the output number. 
        #Level is your pokemon's current level. 
        #AttackStat is your pokemon's Attack/Special Attack stat, whichever one is being used at the moment. 
        #DefenseStat is your opponents Defense/SpecialDefense stat, depending on the attack your pokemon is using. 
        #AttackPower is the power of the specific move you're using. For example, if you were to have been using Thunderbolt, 
        #you would have a 95 for this variable seeing as in the status screen, there's a 95 clearly marked in the move description 
        #when you select it. 
        #STAB is the same type attack bonus. If you're using a move that coordinates with your own type, you get a 1.5 bonus here. 
        #Otherwise, this variable is equal to 1. 
        #Weakness/Resistance depends on if your move was super-effective or otherwise. This variable could be 
        #0.25, 0.5, 1, 2, or 4 depending on how effective your attack was. 
        #RandomNumber is simply a Random Number between 85 and 100.
        dmg = 0
        wri = defender.get_weakness_resistance_or_immunity(move)
        STAB = attacker.get_STAB(move)
        power = move.power
        user_attack = attacker.get_attack()
        user_special_attack = attacker.get_special_attack()
        defender_defense = defender.get_defense()
        defender_special_defense = defender.get_special_defense()
        # Has no power
        if move.has_effect(move_effect=constants.one_hit_ko):
            print "Its a One-Hit-KO!"
            return int(dmg)
        if move.name is "Endeavor":
            dmg = defender.hp - attacker.hp
            if dmg < 0:
                return 0
            return int(dmg)
        #Has Power
        
        if wri == 0:
            print "{} does not affect {}!".format(move.name, defender.nickname)
            return 0
        elif wri > 1:
            print "It's Super-effective!"
        elif wri < 1:
            print "It's not very effective..."
        #
        if move.name is "Acrobatics" and attacker.hold_item is None:
            power *= 2
        if move.name is "Brine" and defender.hp < int(float(defender.get_max_hp()) / 2.0):
            power *= 2
        if move.name is "Crush Claw" and defender.hp < int(float(defender.get_max_hp()) / 2.0):
            power = int(120.0 * float(defender.hp) / float(defender.get_max_hp()))
        if move.name is "Flail":
            N = int(48.0 * float(attacker.hp) / float(attacker.get_max_hp()))
            if 0 <= N and N < 2:
                power = 200
            if 2 <= N and N < 4:
                power = 150
            if 5 <= N and N < 9:
                power = 100
            if 10 <= N and N < 16:
                power = 80
            if 17 <= N and N < 32:
                power = 40
            else:
                power = 20
        if move.name is "Reversal":
            percentage = int(float(attacker.hp) / float(attacker.get_max_hp()) * 100.0)
            if 100 >= percentage and percentage > 70:
                power = 20
            elif 70 >= percentage and percentage > 35:
                power = 40
            elif 35 >= percentage and percentage > 20:
                power = 80
            elif 20 >= percentage and percentage > 10:
                power = 100
            elif 10 >= percentage and percentage > 4:
                power = 150
            else:
                power = 200
        if move.name is "Smelling Salts" and defender.has_status_effect(constants.status_paralysis):
            power = 140
        if move.name is "Wake-Up Slap" and defender.has_status_effect(constants.status_sleep):
            power = 140
        if move.name is "Facade" and (
        attacker.has_status_effect(constants.status_paralysis) 
        or attacker.has_status_effect(constants.status_paralysis) 
        or attacker.has_status_effect(constants.status_poison) 
        or attacker.has_status_effect(constants.status_burn) 
        or attacker.has_status_effect(constants.status_badly_poison) 
        ):
            power = 140
        if move.name is "Hex" and (
        attacker.has_status_effect(constants.status_paralysis) 
        or attacker.has_status_effect(constants.status_paralysis) 
        or attacker.has_status_effect(constants.status_poison) 
        or attacker.has_status_effect(constants.status_burn) 
        or attacker.has_status_effect(constants.status_badly_poison) 
        or attacker.has_status_effect(constants.status_sleep) 
        or attacker.has_status_effect(constants.status_frozen) 
        ):
            power = 130
        
        if move.name is "Punishment":
            total = 0
            if defender.stage_attack > 0: total += defender.stage_attack
            if defender.stage_defense > 0: total += defender.stage_defense
            if defender.stage_special_attack > 0: total += defender.stage_special_attack
            if defender.stage_special_defense > 0: total += defender.stage_special_defense
            if defender.stage_speed > 0: total += defender.stage_speed
            if defender.stage_critical_hit > 0: total += defender.stage_critical_hit
            if defender.stage_accuracy > 0: total += defender.stage_accuracy
            if defender.stage_evasion > 0: total += defender.stage_evasion
            power = 20 * total + 60
        if move.name is "Stored Power":
            total = 0
            if attacker.stage_attack > 0: total += attacker.stage_attack
            if attacker.stage_defense > 0: total += attacker.stage_defense
            if attacker.stage_special_attack > 0: total += attacker.stage_special_attack
            if attacker.stage_special_defense > 0: total += attacker.stage_special_defense
            if attacker.stage_speed > 0: total += attacker.stage_speed
            if attacker.stage_critical_hit > 0: total += attacker.stage_critical_hit
            if attacker.stage_accuracy > 0: total += attacker.stage_accuracy
            if attacker.stage_evasion > 0: total += attacker.stage_evasion
            power = 20 * total + 20
        if move.name is "Foul Play":
            user_attack = defender.get_attack()
        if move.name is "Psyshock" or move.name is "Psystrike" or move.name is "Secret Sword":
            defender_special_defense = defender_defense
        if move.name is "Frustration":
            power = int(float(constants.max_happiness - attacker.happiness) / 2.5)
        if move.name is "Return":
            power = int(float(attacker.happiness) / 2.5)
        if move.name is "Low Kick": # TO DO FIX ME
            power = 60 # 120
        if move.name is "Eruption" or move.name is "Water Spout":
            power = int(150.0 * float(attacker.hp) / float(attacker.get_max_hp()))
        if move.name is "Crush Grip" or move.name is "Wring Out":
            power = int(150.0 * float(defender.hp) / float(defender.get_max_hp()))
        if move.name is "Night Shade" or move.name is "Seismic Toss":
            power = attacker.level 
        if move.name is "Psywave":
            multiplier = randint(0.50,1.50)
            power = int(float(attacker.level) * multiplier)
        if move.name is "Magnitude":
            roll = randint(1,100)
            if roll >= 1 and roll <= 5:
                power = 10
            elif roll >= 6 and roll <= 15:
                power = 30
            elif roll >= 16 and roll <= 35:
                power = 50
            elif roll >= 36 and roll <= 65:
                power = 70
            elif roll >= 66 and roll <= 85:
                power = 90
            elif roll >= 86 and roll <= 95:
                power = 110
            else:
                power = 150
        if move.name is "Gyro Ball":
            if defender.get_speed() >= attacker.get_speed()*2:
                power = 50
            else:
                power = int(25.0 * float(defender.get_speed()) / float(attacker.get_speed()))
        if move.name is "Trump Card":
            if move.pp == 0: 
                power = 40
            elif move.pp == 1: 
                power = 80
            elif move.pp == 2: 
                power = 60
            elif move.pp == 3: 
                power = 50
            else: 
                power = 40
        #
        if move.power < 1 or move.power is None:
            return 0
        random_damage_number = randint(85,100)
        if move.category == constants.move_category_physical:
            dmg = ((((2 * attacker.level / 5.0 + 2) * user_attack * power / defender_defense) / 50.0) + 2)
            dmg = Decimal(dmg) * Decimal(STAB) * Decimal(wri) * Decimal(random_damage_number / 100.0)
        elif move.category == constants.move_category_special:
            dmg = ((((2 * attacker.level / 5.0 + 2) * user_special_attack * power / defender_special_defense) / 50.0) + 2)
            dmg = Decimal(dmg) * Decimal(STAB) * Decimal(wri) * Decimal(random_damage_number / 100.0)
        if self.is_crit(attacker, move) and not guaranteed_hit and dmg > 0:
            dmg *= Decimal(constants.crit_damage_multiplier)
            print "Critical Hit!"
        if move.name is "False Swipe" or move.name is "Hold Back":
            if dmg > defender.hp:
                dmg = defender.hp - 1
        if move.name is "Super Fang":
            dmg = int(float(defender.hp) / 2.0)
        if move.name is "Venoshock" and (defender.has_status_effect(constants.status_poison) or defender.has_status_effect(constants.status_badly_poison)):
            dmg *= 2
        return int(int(dmg))
    def add_pokemon_to_participants(self, battle_participants=None, trainer=None, active_pokemon=None, opponent_pokemon=None):
    #   [{'defeated':t2ap, 'assisted': [{'pokemon':t1ap, 'trainer': trainer_1}, 
    #                                   {'pokemon':pm1, 'trainer': trainer_1}, 
    #                                   {'pokemon':pm2, 'trainer': trainer_1}
    #                                  ]
    #    }
    #    {'defeated':t1ap, 'assisted': [{'pokemon':t2ap, 'trainer': trainer_2}, 
    #                                   {'pokemon':opm1, 'trainer': trainer_2}
    #                                  ]
    #    }
    #   ]
        if battle_participants is None:
            return
        if trainer is None:
            return
        if active_pokemon is None:
            return
        if opponent_pokemon is None:
            return
        for pkm in battle_participants: # list
            if opponent_pokemon is pkm['defeated']: # dict
                already_present = False
                for assisting_pokemon in pkm['assisted']:# list
                    if active_pokemon is assisting_pokemon['pokemon']: # dict
                        already_present = True
                        return "{} already in participants for opponent {}".format(active_pokemon.nickname, opponent_pokemon.nickname)
                if not already_present:
                    pkm['assisted'].append({'pokemon':active_pokemon, 'trainer': trainer})
                    return "{} added to participants against {}".format(active_pokemon.nickname, opponent_pokemon.nickname)
        battle_participants.append({'defeated':opponent_pokemon, 'assisted': [{'pokemon':active_pokemon, 'trainer': trainer}]})
        return "added opponent slot {}, added {} to participants".format(opponent_pokemon.nickname, active_pokemon.nickname)
    def remove_pokemon_participants(self, fainted_pokemon=None, battle_participants=None):
        if fainted_pokemon is None:
            print "battle.award_experience_points_to_participants :  No fainted_pokemon"
        if battle_participants is None:
            print "battle.award_experience_points_to_participants :  No battle_participants"
        for assisted_dict in battle_participants: # list  getting dicts
            if assisted_dict['defeated'] is fainted_pokemon: # dict
                battle_participants.remove(assisted_dict)
    def award_experience_points_to_participants(self, fainted_pokemon=None, battle_participants=None):
    #   [{'defeated':t2ap, 'assisted': [{'pokemon':t1ap, 'trainer': trainer_1}, {'pokemon':pm1, 'trainer': trainer_1}, {'pokemon':pm2, 'trainer': trainer_1}]}
    #    {'defeated':t1ap, 'assisted': [{'pokemon':t2ap, 'trainer': trainer_2}, {'pokemon':opm1, 'trainer': trainer_2}]}
    #   ]
    #   t1ap, pm1, and pm2 all split exp when t2ap
        if fainted_pokemon is None:
            print "battle.award_experience_points_to_participants :  No fainted_pokemon"
        if battle_participants is None:
            print "battle.award_experience_points_to_participants :  No battle_participants"
        # for each pokemon that participated
        for assisted_dict in battle_participants: # list  getting dicts
            if assisted_dict['defeated'] is fainted_pokemon: # dict
                self.remove_pokemon_participants(fainted_pokemon=fainted_pokemon, battle_participants=battle_participants)
                exp = battle().calculate_raw_exp_yeild(fainted_pokemon)
                print " *** Total Exp: {} *** ".format(exp)
                assisted = assisted_dict['assisted'] # getting list
                
                pkm_able_to_earn_exp = 0
                for pkm in assisted: # list getting dicts
                    participant = pkm.get('pokemon')
                    pkm_trainer = pkm.get('trainer')
                    if not participant.is_fainted():
                        #print " *** {} is able to earn exp".format(participant.nickname)
                        pkm_able_to_earn_exp += 1
                    #else:
                    #    print " *** {} is fainted and unable to earn exp".format(participant.nickname)
                #print " *** There are {} pokemon that can earn exp".format(pkm_able_to_earn_exp)
                if pkm_able_to_earn_exp is not 0:
                    exp_per_pokemon = int(exp/pkm_able_to_earn_exp)
                    #print " *** each pokemon gets {} exp.".format(exp_per_pokemon)
                    for pkm in assisted: # list getting dicts
                        participant = pkm.get('pokemon')
                        pkm_trainer = pkm.get('trainer')
                        print participant.earn_exp(exp_per_pokemon, pkm_trainer)
                else:
                    print "there are no pokemon that can gain exp from {}'s defeat".format(fainted_pokemon.nickname)
                    return False
                
        return True
    #PERFORM ACTION
    def perform_action(self, action=None, trainer_1=None, active_pokemon=None, opponent_pokemon=None, battle_participants=None):
       
        console = self.console
        #print action
        action_str = ""
        if active_pokemon is None:
            return 'active_pokemon is none in perform_action'
        if action is None:
            return 'action is none in perform_action called by {}'.format(str(active_pokemon))
        #ATTACK
        if action.get(constants.btl_opt_attack) is not None and active_pokemon.compare(action.get('pokemon')) and opponent_pokemon is not None:
            #print "ATTACKING"
            action_str += "ATTACK"
            move = action.get(constants.btl_opt_attack)
            if trainer_1 is not None: 
                console.character_speech(trainer_1, "{} use {}!".format(active_pokemon.nickname, move.name))
            # STATUS CONDITIONS
            #print "\nLooking at status conditions: \n"
            # SLEEP
            if active_pokemon.has_status_effect(constants.status_sleep):
                print "is {}".format(constants.status_sleep)
                condition = active_pokemon.get_status_effect(constants.status_sleep)
                condition[constants.status_sleep] = condition[constants.status_sleep] - 1
                if condition[constants.status_sleep] > 0:
                    print condition[constants.status_sleep]
                    print "{} is fast asleep.\n".format(active_pokemon.nickname)
                    print "Zzz..."
                    pause()
                    print "Zzz..."
                    pause()
                    print "Zzz..."
                    pause()
                    if move.name is "Sleep Talk":
                        pass
                    if move.name is "Snore":
                        if self.does_hit(attacker=active_pokemon, defender=opponent_pokemon, move=move):
                            print "calculating damage"
                            dmg = self.calculate_damage(attacker=active_pokemon, defender=opponent_pokemon, move=move)
                            print dmg
                            if dmg > 0:
                                opponent_pokemon.take_damage(dmg)
                                print "{} took {} damage!\n".format(opponent_pokemon.nickname, dmg)
                        else:
                            print "The attack missed!"
                    return action_str
                else:
                    print "{} is woke up!.\n".format(active_pokemon.nickname)
                    active_pokemon.remove_status_effect(constants.status_sleep)
                    #active_pokemon.conditions.append({constants.status_normal: None})
            # FROZEN
            if active_pokemon.has_status_effect(constants.status_freeze):
                print "is {}".format(constants.status_freeze)
                roll = randint(1,100)
                print "roll: {}".format(roll)
                if roll > constants.status_freeze_chance:
                    print "{} is completely frozen!\n".format(active_pokemon.nickname)
                    return action_str
                else: # thaw out
                    active_pokemon.remove_status_effect(constants.status_freeze)
                    active_pokemon.conditions.append({constants.status_normal: None})
                    print "{} thawed out!\n".format(active_pokemon.nickname)
            # FLINTCH
            if active_pokemon.has_status_effect(constants.status_flinch):
                print "{} flinched!\n".format(active_pokemon.nickname)
                active_pokemon.remove_status_effect(constants.status_flinch)
                return action_str
            # PARALISYS
            if active_pokemon.has_status_effect(constants.status_paralysis):
                print "is {}".format(constants.status_paralysis)
                roll = randint(1,100)
                print "roll: {}".format(roll)
                if roll < constants.status_paralysis_chance:
                    print "{} is Paralyzed and cannot move!\n".format(active_pokemon.nickname)
                    return action_str
            # CONFUSION
            if active_pokemon.has_status_effect(constants.status_confusion):
                print "{} is Confused!\n".format(active_pokemon.nickname)
                roll = randint(1,100)
                print "roll: {}".format(roll)
                if roll < constants.status_confusion_chance:
                    print "{} hurts itself in its confusion!\n".format(active_pokemon.nickname)
                    dmg = self.calculate_damage(attacker=active_pokemon, defender=active_pokemon, move=hit_self_in_confusion.copy(), guaranteed_hit=True)
                    active_pokemon.take_damage(dmg)
                    return action_str
            # ATTRACTION
            if active_pokemon.has_status_effect(constants.status_attracted):
                print "{} is infatuated!\n".format(active_pokemon.nickname)
                roll = randint(1,100)
                print "roll: {}".format(roll)
                if roll < constants.status_attracted_chance:
                    print "{} too infatuated to move!\n".format(active_pokemon.nickname)
                    return action_str
            # Can Attack!
            # Bide status_bide
            if active_pokemon.has_status_effect(constants.status_bide):
                for condition in active_pokemon.conditions:
                    if condition.get(constants.status_bide) is not None:
                        condition['turns'] -= 1
                        if condition['turns'] <= 0:
                            print "{} released its stored energy!\n".format(active_pokemon.nickname)
                            dmg = condition[constants.status_bide] * 2
                            if dmg > 0:
                                opponent_pokemon.take_damage(dmg)
                                print "{} took {} damage!\n".format(opponent_pokemon.nickname, dmg)
                            else:
                                print "{}'s energy dissapated without doing any damage!\n".format(opponent_pokemon.nickname)
                            #self.apply_effects(attacker=active_pokemon, defender=opponent_pokemon, ally=None, move=move)
                            active_pokemon.remove_status_effect(constants.status_bide)
                        else:
                            print "{} is storing energy...\n".format(active_pokemon.nickname)
                            
                            print "Bide turns left: {}".format(condition['turns'])
                return "Bide"
            # Regular attacks
            print "{} used {}!\n".format(active_pokemon.nickname, move.name)
            num_hits = randint(move.multi_hit[0], move.multi_hit[1])
                
            for hit in range(num_hits):
                if self.does_hit(attacker=active_pokemon, defender=opponent_pokemon, move=move):
                    print "calculating damage"
                    dmg = self.calculate_damage(attacker=active_pokemon, defender=opponent_pokemon, move=move)
                    print dmg
                    if dmg > 0:
                        opponent_pokemon.take_damage(dmg)
                        print "{} took {} damage!\n".format(opponent_pokemon.nickname, dmg)
                    
                    for effect in move.effects:
                        if constants.damage_delt in effect and constants.recovers in effect:
                            healing_effect = effect.split(constants.damage_delt)[0]
                            healing_effect = healing_effect + " " + str(dmg)
                            if constants.pkm_self in healing_effect and active_pokemon is not None:
                                print active_pokemon.apply_effect_on_pokemon(effect=healing_effect, move=move.name)
                            if constants.pkm_foe in healing_effect and opponent_pokemon is not None:
                                if not opponent_pokemon.get_weakness_resistance_or_immunity(move) == 0:
                                    print opponent_pokemon.apply_effect_on_pokemon(effect=healing_effect, move=move.name)
                        #
                        if constants.status_recoil_damage in effect and constants.damage_delt in effect:
                            damage_effect = effect.split(constants.damage_delt)[0]
                            damage_effect = damage_effect + " " + str(dmg)
                            if constants.pkm_self in damage_effect and active_pokemon is not None:
                                print active_pokemon.apply_effect_on_pokemon(effect=damage_effect, move=move.name)
                    self.apply_effects(attacker=active_pokemon, defender=opponent_pokemon, ally=None, move=move)
                    if num_hits > 1:
                        print "{} hit {} times".format(active_pokemon.nickname, num_hits)
                else:
                    if move.type is constants.move_category_status:
                        print "{} evaded the attack!".format(opponent_pokemon.nickname)
                    else:
                        print "The attack missed!"
                    if move.name is "High Jump Kick":
                        print "{} came crashing down hard!".format(active_pokemon.nickname)
                        dmg = int(float(active_pokemon.get_max_hp()) / 2.0)
                        print "{} took {} damage!\n".format(active_pokemon.nickname, dmg)
                        active_pokemon.take_damage(dmg)
                    if move.name is "Jump Kick":
                        print "{} came crashing down hard!".format(active_pokemon.nickname)
                        dmg = int(float(active_pokemon.get_max_hp()) / 2.0)
                        print "{} took {} damage!\n".format(active_pokemon.nickname, dmg)
                        active_pokemon.take_damage(dmg)   
                # action_str +=  
        # SWITCH
        elif action.get(constants.btl_opt_switch) is not None and active_pokemon.compare(action.get('pokemon')):
            #print "SWITCHING"
            action_str += "SWITCH"
            if trainer_1 is None:
                return 'error no trainer'
        # USE ITEM
        elif action.get(constants.btl_opt_items) is not None and active_pokemon.compare(action.get('pokemon')):
            action_str += "USE ITEM"
            if trainer_1 is None:
                return 'error no trainer'
            item = action.get(constants.btl_opt_items)
            print "{} is using a {}!\n".format(trainer_1.name, item.name)
            trainer_1.use_item(item.name)
            # trainer_1.use_item(item) # item count --
            if item.type is constants.item_type_poke_ball:
                if trainer_1 is not None: console.character_speech(trainer_1, "I got you now!  {} go!".format(item.name))
                print "{} threw a {}!\n".format(trainer_1.name, item.name)
                print "{} went into the {}!\n".format(opponent_pokemon.nickname, item.name)
                
                if self.attempt_capture_of_pokemon(trainer=trainer_1, ball=item, pokemon=opponent_pokemon):
                    if trainer_1 is not None: console.character_speech(trainer_1, "Gotcha! {} was caught!".format(opponent_pokemon.nickname))
                    console.rename_pokemon(opponent_pokemon)
                    trainer_1.capture_pokemon(opponent_pokemon)
                    return 'BATTLE OVER'
                else:
                    print "{} escaped the {}!\n".format(opponent_pokemon.nickname, item.name)
                #
            else:
                print "{} used a {} on {}\n".format(trainer_1.name, item.name, active_pokemon.nickname)
                self.apply_effects(attacker=active_pokemon, ally=None, item=item)
            #
        # CALL
        elif action.get(constants.btl_opt_call) is not None and active_pokemon.compare(action.get('pokemon')):
            action_str += "CALL"
            if trainer_1 is None:
                return 'error no trainer'
            pkm = action.get(constants.btl_opt_call)
            if not pkm.has_status_effect(constants.status_freeze):
                pkm.remove_non_volitile_status_effect(constants.status_sleep)
                pkm.remove_status_effect(constants.status_confusion)
                pkm.remove_status_effect(constants.status_attracted)
                # May not be cannon, but fun and makes sense
                pkm.remove_status_effect(constants.status_taunted)
                pkm.remove_status_effect(constants.status_torment)
                #
                print "{} responded to {}'s call!\n".format(pkm.nickname, trainer_1.name)
                
            else:
                print "{} won't respond to {}'s call!\n".format(pkm.nickname, trainer_1.name)
        # FLEE
        elif action.get(constants.btl_opt_flee) is not None and active_pokemon.compare(action.get('pokemon')):
            action_str += "{} attempted to flee!\n"
            if self.attempt_flee():
                print "Got away safely!\n"
                return 'BATTLE OVER'
            else:
                print "Can't escape!\n"
        #else: # HUH???
        #    print "\nSomething happened that should not be possible: \n{}\n".format(action)
        #    print "going back to top"
        return action_str
    def resolve_persisting_effects(self, pokemon=None):
        if pokemon is None:
            return None
        # Healing effects  
        if pokemon.has_status_effect(status_effect=constants.status_rooted):
            amount = int(Decimal(pokemon.get_max_hp()) * Decimal(0.0625))# heal amount
            print "{} recovers {} from its roots!".format(pokemon.nickname, amount)
            pokemon.heal(amount)
        if pokemon.has_status_effect(status_effect=constants.status_aqua_ring):
            amount = int(Decimal(pokemon.get_max_hp()) * Decimal(0.0625))# heal amount
            print "{} recovers {} from the {}!".format(pokemon.nickname, amount, constants.status_aqua_ring)
            pokemon.heal(amount)
        # Damaging effects
        if pokemon.has_status_effect(status_effect=constants.status_burn):
            status_effect = pokemon.get_status_effect(status_effect=constants.status_burn)
            dmg = int(Decimal(pokemon.get_max_hp()) * Decimal(0.125))# Burn damage
            print "{} takes {} damage from its burn!".format(pokemon.nickname, dmg)
            pokemon.take_damage(dmg)
        if pokemon.has_status_effect(status_effect=constants.status_poison):
            status_effect = pokemon.get_status_effect(status_effect=constants.status_poison)
            dmg = int(Decimal(pokemon.get_max_hp()) * Decimal(1.0/8.0))# poison damage
            print "{} takes {} damage from its poison!".format(pokemon.nickname, dmg)
            pokemon.take_damage(dmg)
        if pokemon.has_status_effect(status_effect=constants.status_badly_poison):
            status_effect = pokemon.get_status_effect(status_effect=constants.status_badly_poison)
            dmg = int(Decimal(pokemon.get_max_hp()) * Decimal(status_effect.get(constants.status_badly_poison)/8.0))# Burn damage
            print "{} takes {} damage from its poison!".format(pokemon.nickname, dmg)
            for condition in pokemon.conditions:
                if condition.get(constants.status_badly_poison) is not None:
                    condition[constants.status_badly_poison] += 1
            pokemon.take_damage(dmg)
            print "{} poisoning is getting worse!".format(pokemon.nickname, dmg)
            
        remove_dict = {}
        if pokemon.has_status_effect(status_effect=constants.status_partially_trapped):
            print constants.status_partially_trapped
            dmg = int(Decimal(pokemon.get_max_hp()) * Decimal(0.0625))# trapped damage
            for condition in pokemon.conditions:
                if condition.get(constants.status_partially_trapped) is not None:
                    condition[constants.status_partially_trapped] -= 1
                    if condition[constants.status_partially_trapped] >= 0:
                        print "{} takes {} damage from the {}!".format(pokemon.nickname, dmg, condition['move'])
                        pokemon.take_damage(dmg)
                    else:
                        print "{} was freed from the {}".format(pokemon.nickname, condition.get('move'))
                        remove_dict[condition.get('move')] =  constants.status_partially_trapped
        #
        if pokemon.has_status_effect(status_effect=constants.disables_move):
            print constants.disables_move
            for condition in pokemon.conditions:
                if condition.get(constants.disables_move) is not None:
                    condition['turns'] -= 1
                    if condition['turns'] <= 0:
                        print "{}'s {} is no longer disabled!".format(pokemon.nickname, condition.get('move'))
                        remove_dict[constants.disables_move] = constants.status_partially_trapped
        if pokemon.has_status_effect(status_effect=constants.status_encore):
            print constants.status_encore
            for condition in pokemon.conditions:
                if condition.get(constants.status_encore) is not None:
                    condition['turns'] -= 1
                    if condition['turns'] <= 0:
                        print "{}'s {} ended!".format(pokemon.nickname, constants.status_encore)
                        remove_dict[constants.status_encore] = None
        if remove_dict.keys() > 0:
            for key in remove_dict.keys():
                print "{} {}".format(key, remove_dict[key])
                pokemon.remove_status_effect(remove_dict[key], key)
        #
        if pokemon.has_status_effect(status_effect=constants.status_cursed):   
            status_effect = pokemon.get_status_effect(status_effect=constants.status_cursed)
            dmg = int(Decimal(pokemon.get_max_hp()) * Decimal(0.25))# Curse damage
            print "{} takes {} damage from the curse!".format(pokemon.nickname, dmg)
            pokemon.take_damage(dmg)
        #
    def apply_effects(self, attacker=None, defender=None, ally=None, move=None, item=None):
        if attacker is None:
            print "in battle.apply_effects attacker is None"
            return None
        if move is not None and move.effects is not None:
            for effect in move.effects:
                print effect
                effect_success = True
                if "%" in effect:
                    roll = randint(1,100)
                    chance = get_int_from_string(effect)
                    print "roll {}".format(roll)
                    print "chance {}%".format(chance)
                    if roll > chance:
                        print "Failure"
                        effect_success = False
                    else:
                        print "Success"
                print "effecting..."
                if constants.pkm_self in effect and attacker is not None and effect_success:
                    #
                    print attacker.apply_effect_on_pokemon(effect=effect, move=move.name)
                #
                elif constants.pkm_foe in effect and defender is not None and effect_success or constants.pkm_all_other in effect:
                    #print "Foe"
                    if not defender.get_weakness_resistance_or_immunity(move) == 0:
                        print defender.apply_effect_on_pokemon(effect=effect, move=move.name)
                #
                elif constants.pkm_ally in effect and ally is not None and effect_success or constants.pkm_all_other in effect:
                    #
                    print ally.apply_effect_on_pokemon(effect=effect, move=move.name)
        if item is not None and item.effects is not None:
            print "Number of effects: {}".format(len(item.effects))
            for effect in item.effects:
                print "Item Effect: {}".format(effect)
                print attacker.apply_effect_on_pokemon(effect=effect)
        return
    #
    def attempt_flee(self):
        max = 100
        min = 1
        roll = randint(min,max)
        if roll >= max/5:
            return True
        return False
    #Capture Pokemon
    def attempt_capture_of_pokemon(self, trainer=None, ball=None, pokemon=None):
        console = self.console
        if pokemon is None:
            print "battle.attempt_capture_of_pokemon: pokemon is None"
            return False
        if ball is None:
            print "battle.attempt_capture_of_pokemon: ball is None"
            return False
        if trainer is None:
            print "battle.attempt_capture_of_pokemon: trainer is None"
            return False
        if pokemon.original_trainer is not None:
            return False
        shake_check_count = 4
        tries = 0
        for check in range(shake_check_count):
            tries += 1
            time.sleep(1)
            #print ball
            #print ball.ball_modifier
            attempt_success = pokemon.shake_check(ball_modifier=ball.ball_modifier)
            if not attempt_success:
                print " * Sha-"
                if tries is 1: 
                    console.character_speech(trainer, "Oh no! The Pokemon broke free!")
                if tries is 2: 
                    console.character_speech(trainer, "Aw! It appeared to be caught!")
                if tries is 3: 
                    console.character_speech(trainer, "Aargh! Almost had it!")
                if tries is 4: 
                    console.character_speech(trainer, "Gah! It was so close too!")
                return False
            print " * Shake * "# try {}".format(tries)
        return True
    #AI
    def ai_choose_move(self, pokemon=None):
        roll = 0
        if pokemon is None:
            return None
        if pokemon.moves is None:
            return None
        max = len(pokemon.moves) - 1
        if max == -1:
            return None
        if max == 0:
            return pokemon.moves[0]
        roll = randint(0, max)
        return pokemon.moves[roll]
    #
    def calculate_raw_exp_yeild(self, opponent_pokemon=None, battle_type='Wild'):
        b = opponent_pokemon.base_exp # opponent base exp
        L = opponent_pokemon.level # opponent Level
        battle_type_bonus = 1
        if battle_type is 'Trainer':
            battle_type_bonus = 1.5
        elif battle_type is 'League':
            battle_type_bonus = 2
        #s = 1 # EXP SHARE
        exp = int(((b*L) / (7)) * battle_type_bonus)
        return exp
    def break_speed_tie(self):
        roll = randint(0,1)
        #print "Coin Flip = {}".format(roll)
        if roll is 1:
            return 1
        return -1
    
#
#
#
#
#
#