from constants import constants
from utilities import *
from save_and_restore import *
from abilities import *
from types import *
from moves import *
from random import randint
from math import *
from decimal import *

class pokemon():
    def __init__(self, gd=None):
        self.default_move = move()
        # Personal Data
        self.name = 'MissingNo.'
        self.nickname = 'MissingNo.'
        self.gender = constants.male
        self.affection_hearts = 1
        self.original_trainer = None
        self.level = 5
        self.hp = 0
        self.conditions = [{constants.status_normal: None}]
        self.exp = 0
        self.nature = None#self.get_random_nature()
        self.pokeball = None
        # Pokedex Data
        self.dex_number = 0
        self.generation_introducted = 1
        self.types = []
        self.species = ''
        self.height = "" # measured in kg
        self.weight = '' # measured in meters
        self.abilities = [None]
        self.ability = None
        self.local_numbers = dict({'National': 0, 'Local': 0, 'Kanto': 0, 'Johto': 0, 'Kalos': 0})
        self.japanese_name = 'MissingNo.'
        # where to find the pokemon
        self.places_found = ['abusing bugs']
        # Training Data
        self.ev_yield = {}
        self.catch_rate = 255 # 3 (near impossible) - 255 (almost garunteeed)
        self.happiness = constants.base_happiness
        self.base_exp = 1
        self.growth_rate = constants.growthrate_medium_slow
        # Breeding Data
        self.egg_types = list()
        self.gender_varience = list(constants.equal_male_female)
        self.egg_cycles = 0
        #self.stats = dict(constants.all_stat_format)
        self.pokedex_entry = dict(constants.pokedex_entries)
        self.evolution = None
        # Moves
        self.moves = list()
        self.previous_moves = list()
        self.moves_learned_by_level_up = dict()
        self.moves_learned_by_egg = list()
        self.moves_learned_by_move_tutors = list()
        self.moves_learned_by_machines = list()
        self.moves_learned_by_transfer = list()
        # icons
        self.sprite_icon = None
        self.sprite_front = None
        self.sprite_back = None
        self.sprite_front_shiny = None
        self.sprite_back_shiny = None
        # Base stats
        self.base_hp = 100
        self.base_attack = 100
        self.base_defense = 100
        self.base_special_attack = 100
        self.base_special_defense = 100
        self.base_speed = 100
        # IV
        self.iv_hp = 1
        self.iv_attack = 1
        self.iv_defense = 1
        self.iv_special_attack = 1
        self.iv_special_defense = 1
        self.iv_speed = 1
        # EV
        self.ev_hp = 0
        self.ev_attack = 0
        self.ev_defense = 0
        self.ev_special_attack = 0
        self.ev_special_defense = 0
        self.ev_speed = 0
        # Stages variences 
        # 0 is normal, max, min 6,-6
        self.stage_attack = 0
        self.stage_defense = 0
        self.stage_special_attack = 0
        self.stage_special_defense = 0
        self.stage_speed = 0
        self.stage_critical_hit = 0
        self.stage_accuracy = 0
        self.stage_evasion = 0
        # Natures variences 
        self.nature_speed = 1.0
        self.nature_special_defense = 1.0
        self.nature_special_attack = 1.0
        self.nature_defense = 1.0
        self.nature_attack = 1.0
        
        self.hold_item = self.give_pokemon_random_item_from_item_list()
        #
        if gd is not None:
            self._set(gd=gd)
        # Natures variences 
        # 1.0 normal, 1.1 positive predisposition, 0.9 negative predisposition
        self.set_nature_stat_impact()
        self.fully_heal()
    def _set(self, gd=None):
        if gd is None:
            print "ERROR: GENERAL INFORMATION OR SPECIFIC INFO IS NONE"
            return False
        self.name = gd.get('name')
        self.nickname = self.name
        self.level = 5
        self.generation_introducted = gd.get('generation introduced')
        self.types = list(gd.get('types'))
        self.species = gd.get('species')
        self.height = gd.get('height')
        self.weight = gd.get('weight')
        self.abilities = list(gd.get('abilities'))
        self.local_numbers = dict(gd.get('local numbers'))
        self.japanese_name = gd.get('japanese name')
        self.places_found = list(gd.get('place found'))
        self.ev_yield = dict(gd.get('ev yield'))
        self.catch_rate = gd.get('catch rate') 
        self.base_exp = gd.get('base xp')
        self.happiness = gd.get('happiness')
        self.growth_rate = gd.get('growth rate')
        self.gender_varience = list(gd.get('gender varience'))
        self.egg_cycles = gd.get('egg cycles')
        self.pokedex_entry = dict(gd.get('pokedex entry'))
        self.evolution = gd.get('evolution')
        self.moves_learned_by_level_up = dict(gd.get('level up moves'))# dict
        self.moves_learned_by_egg = list(gd.get('egg moves'))# list
        self.moves_learned_by_move_tutors = list(gd.get('tutor moves'))# list
        self.moves_learned_by_machines = list(gd.get('machine moves'))# list
        self.moves_learned_by_transfer = list(gd.get('transfer moves'))# list
        self.sprite_icon = gd.get('icon')
        self.sprite_front = gd.get('front sprite')
        self.sprite_back = gd.get('back sprite')
        self.sprite_front_shiny = gd.get('front shiny sprite')
        self.sprite_back_shiny = gd.get('back shiny sprite')
        #
        self.base_hp = gd.get(constants.base_hp)
        self.base_attack = gd.get(constants.base_attack)
        self.base_defense = gd.get(constants.base_defense)
        self.base_special_attack = gd.get(constants.base_special_attack)
        self.base_special_defense = gd.get(constants.base_special_defense)
        self.base_speed = gd.get(constants.base_speed)
        #
        self.moves = []
        self.set_random_gender()
        self.nature = self.get_random_nature()
        self.ability = None
        self.choose_random_ability()
        self.exp = self.get_previous_level_exp()
        self.original_trainer = None
        self.condition = [{constants.status_normal: None}]
        self.happiness = constants.base_happiness
        # IV
        self.iv_hp = 0
        self.iv_attack = 0
        self.iv_defense = 0
        self.iv_special_attack = 0
        self.iv_special_defense = 0
        self.iv_speed = 0
        # EV
        self.ev_hp = 0
        self.ev_attack = 0
        self.ev_defense = 0
        self.ev_special_attack = 0
        self.ev_special_defense = 0
        self.ev_speed = 0
        return self
    def _randomize_vital_statistics(self, min_level=None, max_level=None, set_level=None, min_iv=None, max_iv=None, ev_diff_dict=None, gender=None, nature=None, pokeball=None):
        #
        self.pokeball = pokeball
        # SET LEVEL
        if min_level is not None and max_level is not None:
            self.level = randint(min_level, max_level)
        elif set_level is not None:
            self.level = set_level
        else:
            self.level = randint(2, 100)
        # SET IV LEVELS
        if min_iv is None:
            min_iv = 0
        if max_iv is None:
            max_iv = 31
        self.iv_hp = randint(min_iv, max_iv)
        self.iv_attack = randint(min_iv, max_iv)
        self.iv_defense = randint(min_iv, max_iv)
        self.iv_special_attack = randint(min_iv, max_iv)
        self.iv_special_defense = randint(min_iv, max_iv)
        self.iv_speed = randint(min_iv, max_iv)
        # SET EV LEVELS 
        if ev_diff_dict is not None:
            self.ev_hp = ev_diff_dict.get(constants.ev_hp)
            self.ev_attack = ev_diff_dict.get(constants.ev_attack)
            self.ev_defense = ev_diff_dict.get(constants.ev_defense)
            self.ev_special_attack = ev_diff_dict.get(constants.ev_special_attack)
            self.ev_special_defense = ev_diff_dict.get(constants.ev_special_defense)
            self.ev_speed = ev_diff_dict.get(constants.ev_speed)
        else:
            self.ev_hp = 0
            self.ev_attack = 0
            self.ev_defense = 0
            self.ev_special_attack = 0
            self.ev_special_defense = 0
            self.ev_speed = 0
        #
        if nature is None:
            self.nature = self.get_random_nature()
        else:
            self.nature = nature
        if gender is None:
            self.set_random_gender()
        else:
            self.gender = gender
        self.choose_random_ability()
        self.exp = self.get_previous_level_exp()
        #
        self.set_nature_stat_impact()
        self.learn_all_moves_up_to_level()
        self.fully_heal()
        return self
    #Text based getters
    def __str__(self):
        return str(self.nickname) + " (" + str(self.name) + ") ID: " + str(self.original_trainer)
    def get_conditions(self):
        ret_str = "Status: "
        for condition in self.conditions:
            for key in condition.keys():
                if key is 'move':
                    ret_str += "({}) ".format(condition.get('move'))
                else:
                    ret_str += "{} ".format(key)
                    if condition[key] is not None:
                        ret_str += "[{}] ".format(condition[key])
        return ret_str + "\n"
    def battle_summary(self):
        ret_str = "{0} ({1}) Lv. {2} {3}\n".format(self.nickname, self.name, self.level, self.get_short_gender())
        ret_str += self.get_conditions()
        ret_str += "HP:  {0:6} {1:4} / {2:4}\n".format(self.get_hit_bar(), self.hp, self.get_max_hp())
        ret_str += "EXP: {0:6}\n".format(self.get_exp_bar())
        ret_str += self.buffs()
        return ret_str
    def summary(self, with_header=True):
        ret_str = ""
        if with_header: 
            ret_str += "{0} ({1}) Lv. {2} {3}\n".format(self.nickname, self.name, self.level, self.get_short_gender())
        ret_str += "HP:  {0:6} {1:4} / {2:4}\n".format(self.get_hit_bar(), self.hp, self.get_max_hp())
        ret_str += self.get_conditions()
        index = 0
        for type in self.types:
            index += 1
            ret_str += "Type {0}: {1}\n".format(index, type.name)
        if self.pokeball is not None:
            ret_str += "Pokeball: {}".format(self.pokeball.name)
        ret_str += "OT: {0}\n".format(self.original_trainer)
        ret_str += "EXP: {0}\n".format(self.exp)
        ret_str += "EXP to level: {0}\n".format(self.get_exp_for_level_up())
        ret_str += "EXP until level: {0}\n".format(self.get_exp_to_next_level())
        ret_str += "OT: {0}\n".format(self.original_trainer)
        ret_str += "NAT: {0}\n".format(self.nature)
        return ret_str
    def summary_stats(self, with_header=True):
        ret_str = ""
        if with_header: 
            ret_str += "{0} ({1}) Lv. {2} {3}\n".format(self.nickname, self.name, self.level, self.get_short_gender())
        ret_str += "Base Stats: {0}\n".format('')
        ret_str += "HP: {0} / {1}\n".format(self.hp, self.get_max_hp())
        ret_str += "Att: {0}\n".format(self.get_attack())
        ret_str += "Def: {0}\n".format(self.get_defense())
        ret_str += "SA: {0}\n".format(self.get_special_attack())
        ret_str += "SD: {0}\n".format(self.get_special_defense())
        ret_str += "Spd: {0}\n".format(self.get_speed())
        return ret_str
    def summary_stats_ev(self, with_header=True):
        ret_str = ""
        if with_header: 
            ret_str += "{0} ({1}) Lv. {2} {3}\n".format(self.nickname, self.name, self.level, self.get_short_gender())
        #IV
        ret_str += "IV:  {0}\n".format('')
        ret_str += "HP:  {0}\n".format(self.iv_hp)
        ret_str += "Att: {0}\n".format(self.iv_attack)
        ret_str += "Def: {0}\n".format(self.iv_defense)
        ret_str += "SA:  {0}\n".format(self.iv_special_attack)
        ret_str += "SD:  {0}\n".format(self.iv_special_defense)
        ret_str += "Spd: {0}\n".format(self.iv_speed)
        return ret_str
    def summary_stats_iv(self, with_header=True):
        ret_str = ""
        if with_header: 
            ret_str += "{0} ({1}) Lv. {2} {3}\n".format(self.nickname, self.name, self.level, self.get_short_gender())
        #EV
        ret_str += "EV:  {0}\n".format('')
        ret_str += "HP:  {0}\n".format(self.ev_hp)
        ret_str += "Att: {0}\n".format(self.ev_attack)
        ret_str += "Def: {0}\n".format(self.ev_defense)
        ret_str += "SA:  {0}\n".format(self.ev_special_attack)
        ret_str += "SD:  {0}\n".format(self.ev_special_defense)
        ret_str += "Spd: {0}\n".format(self.ev_speed)
        return ret_str
    def summary_stats_full(self, with_header=True):
        ret_str = ""
        if with_header: 
            ret_str += "{0} ({1}) Lv. {2} {3}\n".format(self.nickname, self.name, self.level, self.get_short_gender())
        ret_str += "{}\n{}\n{}\n".format(self.summary_stats(with_header=False), self.summary_stats_iv(with_header=False), self.summary_stats_ev(with_header=False))
        return ret_str
    def summary_moves(self, with_header=True):
        ret_str = ""
        if with_header: 
            ret_str += "{0} ({1}) Lv. {2} {3}\n".format(self.nickname, self.name, self.level, self.get_short_gender())
        for move in self.moves:
            ret_str += "- {0}\n".format(str(move))
        return ret_str
    def summary_evolutions(self, with_header=True):
        ret_str = ""
        if with_header: 
            ret_str += "{0} ({1}) Lv. {2} {3}\n".format(self.nickname, self.name, self.level, self.get_short_gender())
        ret_str += "Evolution(s): {0}\n".format('')
        if self.evolution is not None:
            for pkm in self.evolution:
                for key in pkm.keys():
                    for subkey in pkm[key].keys():
                        ret_str += "- {0} by {1}: {2}\n".format(key, subkey, pkm[key][subkey])
        return ret_str
    def summary_condition(self, with_header=True):
        ret_str = ""
        if with_header: 
            ret_str += "{0} ({1}) Lv. {2} {3}\n".format(self.nickname, self.name, self.level, self.get_short_gender())
        ret_str += "CONDITION NOT IMPLEMENTED.\N"
        return ret_str
    def summary_full(self):
        ret_str = "{0} ({1}) Lv. {2} {3}\n".format(self.nickname, self.name, self.level, self.get_short_gender())
        ret_str += self.summary(with_header=False) + "\n"
        ret_str += self.summary_stats_full(with_header=False) + "\n"
        ret_str += self.summary_moves(with_header=False) + "\n"
        ret_str += self.summary_evolutions(with_header=False) + "\n"
        # ret_str += self.summary_condition(with_header=False) + "\n"
        return ret_str
    def get_from_party(self):
        return self.battle_summary()
    def buffs(self):
        stat_string = ""
        if self.stage_attack > 0:
            stat_string += "Attack Buffed {}\n".format(self.stage_attack)
        if self.stage_attack < 0:
            stat_string += "Attack Debuffed {}\n".format(self.stage_attack)
            
        if self.stage_defense > 0:
            stat_string += "Defense Buffed {}\n".format(self.stage_defense)
        if self.stage_defense < 0:
            stat_string += "Defense Debuffed {}\n".format(self.stage_defense)
            
        if self.stage_special_attack > 0:
            stat_string += "Special Attack Buffed {}\n".format(self.stage_special_attack)
        if self.stage_special_attack < 0:
            stat_string += "Special Attack Debuffed {}\n".format(self.stage_special_attack)
            
        if self.stage_special_defense > 0:
            stat_string += "Special Defense Buffed {}\n".format(self.stage_special_defense)
        if self.stage_special_defense < 0:
            stat_string += "Special Defense Debuffed {}\n".format(self.stage_special_defense)
            
        if self.stage_speed > 0:
            stat_string += "Speed Buffed {}\n".format(self.stage_speed)
        if self.stage_speed < 0:
            stat_string += "Speed Debuffed {}\n".format(self.stage_speed)
            
        if self.stage_critical_hit > 0:
            stat_string += "Critical Hit Ratio Increased {}\n".format(self.stage_critical_hit)
            
        if self.stage_accuracy > 0:
            stat_string += "Accuracy Buffed {}\n".format(self.stage_accuracy)
        if self.stage_accuracy < 0:
            stat_string += "Accuracy Debuffed {}\n".format(self.stage_accuracy)
        
        if self.stage_evasion > 0:
            stat_string += "Evasion Buffed {}\n".format(self.stage_evasion)
        if self.stage_evasion < 0:
            stat_string += "Evasion Debuffed {}\n".format(self.stage_evasion)
            
        return stat_string
    def get_pokemon_info(self):
        ret_str = ""
        ret_str += self.summary()
        ret_str += self.summary_moves(with_header=False)
        ret_str += self.summary_stats_full(with_header=False)
        return ret_str
    def get_pokemon_full_stats(self):
        return self.summary_full()
    def get_pokemon_basic_stats(self):
        return self.summary()
    def get_short_gender(self):
        #print self.gender
        if  constants.male is self.gender:
            #print "found M"
            return 'M'
        elif constants.female is self.gender:
            #print "found F"
            return 'F'
        elif constants.neutor is self.gender:
            #print "found N"
            return 'N'
        else:
            #print "found None"
            return "-"
    #
    def get_exp_to_next_level(self):
        return self.get_exp_for_level_up() - self.exp
    def get_exp_for_level_up(self, level=None):
        if level is None:
            ##print "Level is None"
            level = self.level
        ##print level
        level_cubed = int(level*level*level)
        level_squared = int(level*level)
        ##print level_squared
        ##print level_cubed
        exp = 0
        ##print "calculating for level {}".format(level)
        if self.growth_rate is constants.growthrate_fast:
            exp =  int(0.8 * level_cubed)
            
        elif self.growth_rate is constants.growthrate_medium_fast:
            exp =  int(level_cubed)
            
        elif self.growth_rate is constants.growthrate_medium_slow:
            ##print  "{}".format((1.2*level_cubed) - (15*level_squared) + (100*level) - 140)
            exp =  int((1.2*level_cubed) - (15*level_squared) + (100*level) - 140)
            
        elif self.growth_rate is constants.growthrate_slow:
            exp =  int(1.25 * level_cubed)

        elif self.growth_rate is constants.growthrate_erratic:
            exp =  int(0.6 * level_cubed)
            
        else: # constants.growthrate_fluctuating or some bad value
            exp =  int(1.64 * level_cubed)
        if int(exp) < 0:
            return 0
        return int(exp)      
    def get_flee_chance(self):
        return 120
    def set_dex_number(self, setting='National'):
        self.dex_number = self.local_numbers.get(setting)
    def get_dex_number(self, setting='National'):
        return self.local_numbers.get(setting)
    def get_national_dex_number(self):
        return self.local_numbers['National']
    def set_pokemon_original_trainer(self, trainer=None):
        if trainer is None:
            return "Trainer is None."
        self.original_trainer = trainer.name + ": ID "+ trainer.trainer_id
        return "{}'s original trainer is {}.".format(self.nickname, self.original_trainer)
    def nickname_pokemon(self,nickname=None):
        if nickname is None:
            return "could not nickname {}".format(self.nickname)
        old_name = self.nickname
        self.nickname = nickname
        return "{} was renamed to {}.".format(old_name, self.nickname)
    def set_nickname(self, nickname=None):
        if nickname is None:
            return "could not nickname {}".format(self.nickname)
        self.nickname = nickname
        return self
    def set_level(self, level=None):
        if level is None or not isinstance(level, int) or level < 1 or level > constants.max_level:
            return False
        self.level = level
        return self.level
    def set_nature_stat_impact(self):
        #boosts
        if self.nature == 'Lonely' or self.nature == 'Brave' or self.nature == 'Adamant' or self.nature == 'Naughty':
            self.nature_attack = 1.1
        elif self.nature == 'Bold' or self.nature == 'Relaxed' or self.nature == 'Impish' or self.nature == 'Lax':
            self.nature_defense = 1.1
        elif self.nature == 'Modest' or self.nature == 'Mild' or self.nature == 'Quiet' or self.nature == 'Rash':
            self.nature_special_attack = 1.1
        elif self.nature == 'Calm' or self.nature == 'Gentle' or self.nature == 'Sassy' or self.nature == 'Careful':
            self.nature_special_defense = 1.1
        elif self.nature == 'Timid' or self.nature == 'Hasty' or self.nature == 'Jolly' or self.nature == 'Naive':
            self.nature_speed = 1.1
        #reductions
        if self.nature == 'Bold' or self.nature == 'Timid' or self.nature == 'Modest' or self.nature == 'Calm':
            self.nature_attack = 0.9
        elif self.nature == 'Lonely' or self.nature == 'Hasty' or self.nature == 'Mild' or self.nature == 'Gentle':
            self.nature_defense = 0.9
        elif self.nature == 'Adamant' or self.nature == 'Impish' or self.nature == 'Jolly' or self.nature == 'Careful':
            self.nature_special_attack = 0.9
        elif self.nature == 'Rash' or self.nature == 'Naive' or self.nature == 'Lax' or self.nature == 'Naughty':
            self.nature_special_defense = 0.9
        elif self.nature == 'Brave' or self.nature == 'Relaxed' or self.nature == 'Quiet' or self.nature == 'Sassy':
            self.nature_speed = 0.9
        return self
    def choose_random_ability(self):
        if self.ability is None and self.abilities is not None:
            max = len(self.abilities)-1
            if max < 0:
                return False
            roll = randint(0,max)
            self.ability = self.abilities[roll]
            return self
        return self
    def set_difficulty(iv_dict=None, ev_dict=None):
        # IV
        self.iv_hp = iv_dict.get(constants.iv_hp)
        self.iv_attack = iv_dict.get(constants.iv_attack)
        self.iv_defense = iv_dict.get(constants.iv_defense)
        self.iv_special_attack = iv_dict.get(constants.iv_special_attack)
        self.iv_special_defense = iv_dict.get(constants.iv_special_defense)
        self.iv_speed = iv_dict.get(constants.iv_speed)
        # EV
        self.ev_hp = ev_dict.get(constants.ev_hp)
        self.ev_attack = ev_dict.get(constants.ev_attack)
        self.ev_defense = ev_dict.get(constants.ev_defense)
        self.ev_special_attack = ev_dict.get(constants.ev_special_attack)
        self.ev_special_defense = ev_dict.get(constants.ev_special_defense)
        self.ev_speed = ev_dict.get(constants.ev_speed)
        return self
    def learn_all_moves_up_to_level(self):
        self.moves = []
        for level in range(self.level):
            if self.moves_learned_by_level_up.get(level) is not None:
                for move in self.moves_learned_by_level_up[level]:
                    self.learn_move(move)
        while self.are_move_slots_full():
            self.forget_move(self.moves[0])   
    def _set_move_set(self, move_set=None):
        if move_set is not None:
            self.moves = move_set
        return self
    def compare(self, pokemon=None):
        if pokemon is None:
            return False
        if (self.name is pokemon.name and 
        self.nickname is pokemon.nickname and 
        self.original_trainer is pokemon.original_trainer and 
        self.level is pokemon.level and 
        self.nature is pokemon.nature ):
            return True
        return False
    def get_affection_hearts(self):
        return int(self.happiness / 5.0)
    #Move based getters
    def use_move(self, move=None):
        if move is None:
            return self
        for pkm_move in self.moves:
            if move.name in pkm_move.name  and move.name.lower()[0] in pkm_move.name.lower()[0]:
                pkm_move.pp -= 1
        return self
    def get_move_from_index(self, index=0, send_info=False):
        if index >= len(self.moves):
            return "index out of range: {}".format(index)
        if send_info is True:
            return self.moves[index].get_move()
        else:
            return self.moves[index]
        return "Cannot find move[{}]".format(index)
    def get_move(self, move_name=None):
        for move in self.moves:
            if move_name.lower() in move.name.lower() and move_name.lower()[0] in move.name.lower()[0]:
                return move
        return None
    def can_learn_move(self):
        if self.moves_learned_by_level_up.get(self.level) is None:
            return []
        return self.moves_learned_by_level_up.get(self.level)
    def are_move_slots_full(self):
        if len(self.moves) > 4:
            return True
        return False
    def learn_move(self, move=None):
        if move is None:
            return False
        if not self.are_move_slots_full():
            self.moves.append(move)
            is_prev_move = False
            for prev_move in self.previous_moves:
                if move.name is prev_move.name:
                    is_prev_move = True
            if not is_prev_move:
                self.previous_moves.append(move)
            return True
        else:
            return False
    def forget_move(self, move=None):
        if move is None:
            return
        self.moves.remove(move)
        return True
#Stat related getters
    def get_max_hp(self, level=None):
        #print level
        if level is None:
            level = self.level
        #print level
        return int(int(((self.iv_hp + 2 * self.base_hp + (self.ev_hp/4) ) * level/100 ) + 10 + level))
    def get_attack(self, level=None, account_for_status=False, ignore_stat_changes=False):
        if level is None or not isinstance(level, int) or level < 1:
            level = self.level
        if self.has_status_effect(constants.status_burn) and account_for_status:
            return int(int((((self.iv_attack + 2 * self.base_attack + (self.ev_attack/4) ) * level/100 ) + 5) * self.nature_attack * self.get_main_stat_stage(self.stage_attack) / 2.0))
        else:
            return int(int((((self.iv_attack + 2 * self.base_attack + (self.ev_attack/4) ) * level/100 ) + 5) * self.nature_attack * self.get_main_stat_stage(self.stage_attack)))
    def get_defense(self, level=None, account_for_status=False, ignore_stat_changes=False):
        if level is None or not isinstance(level, int) or level < 1:
            level = self.level
        return int(int((((self.iv_defense + 2 * self.base_defense + (self.ev_defense/4) ) * level/100 ) + 5) * self.nature_defense * self.get_main_stat_stage(self.nature_defense)))
    def get_special_attack(self, level=None, account_for_status=False, ignore_stat_changes=False):
        if level is None or not isinstance(level, int) or level < 1:
            level = self.level
        return int(int((((self.iv_special_attack + 2 * self.base_special_attack + (self.ev_special_attack/4) ) * level/100 ) + 5) * self.nature_special_attack * self.get_main_stat_stage(self.nature_special_attack)))
    def get_special_defense(self, level=None, account_for_status=False, ignore_stat_changes=False):
        if level is None or not isinstance(level, int) or level < 1:
            level = self.level
        return int(int((((self.iv_special_defense + 2 * self.base_special_defense + (self.ev_special_defense/4) ) * level/100 ) + 5) * self.nature_special_defense * self.get_main_stat_stage(self.nature_special_defense)))
    def get_speed(self, level=None, account_for_status=False, ignore_stat_changes=False):
        if level is None or not isinstance(level, int) or level < 1:
            level = self.level
        if self.has_status_effect(constants.status_paralysis) and account_for_status:
            return int((((self.iv_speed + 2 * self.base_speed + (self.ev_speed/4) ) * level/100 ) + 5) * self.nature_attack * self.get_main_stat_stage(self.stage_speed) * 25/100)
        else:
            return int((((self.iv_speed + 2 * self.base_speed + (self.ev_speed/4) ) * level/100 ) + 5) * self.nature_attack * self.get_main_stat_stage(self.stage_speed))
    def get_hit_bar(self):
        hit_bar = "["
        perc = float(self.hp) / float(self.get_max_hp())
        perc = int(int(perc * constants.hit_bar))
        empty_bar = int(constants.hit_bar) - perc 
        for i in range(perc):
            hit_bar += "|"
        for i in range(empty_bar):
            hit_bar += " "
        return hit_bar + "]"
    def get_exp_bar(self):
        exp_bar = "["
        perc = float(Decimal(self.exp) - Decimal(self.get_previous_level_exp())) / float(Decimal(self.get_exp_for_level_up()) - (self.get_previous_level_exp()))
        perc = int(int(perc * constants.hit_bar))
        empty_bar = int(constants.hit_bar) - perc 
        for i in range(perc):
            exp_bar += "|"
        for i in range(empty_bar):
            exp_bar += " "
        return exp_bar + "]"
    def get_main_stat_stage(self, stage):
        if stage == 1: return 1.5
        elif stage == 2: return 2.0
        elif stage == 3: return 2.5
        elif stage == 4: return 3.0
        elif stage == 5: return 3.5
        elif stage == 6: return 4.0
        elif stage == -1: return 0.66
        elif stage == -2: return 0.5
        elif stage == -3: return 0.4
        elif stage == -4: return 0.33
        elif stage == -5: return 0.285
        elif stage == -6: return 0.25
        else: return 1
    def get_accuracy_stage(self):
        if self.stage_accuracy == 1: return 1.33
        elif self.stage_accuracy == 2: return 1.66
        elif self.stage_accuracy == 3: return 2.0
        elif self.stage_accuracy == 4: return 2.33
        elif self.stage_accuracy == 5: return 2.66
        elif self.stage_accuracy == 6: return 3.0
        elif self.stage_accuracy == -1: return 0.75
        elif self.stage_accuracy == -2: return 0.6
        elif self.stage_accuracy == -3: return 0.5
        elif self.stage_accuracy == -4: return 0.428
        elif self.stage_accuracy == -5: return 0.375
        elif self.stage_accuracy == -6: return 0.33
        else: return 1.0
    def get_evasion_stage(self):
        if self.stage_evasion == -1: return 1.33
        elif self.stage_evasion == -2: return 1.66
        elif self.stage_evasion == -3: return 2.0
        elif self.stage_evasion == -4: return 2.33
        elif self.stage_evasion == -5: return 2.66
        elif self.stage_evasion == -6: return 3.0
        elif self.stage_evasion == 1: return 0.75
        elif self.stage_evasion == 2: return 0.6
        elif self.stage_evasion == 3: return 0.5
        elif self.stage_evasion == 4: return 0.428
        elif self.stage_evasion == 5: return 0.375
        elif self.stage_evasion == 6: return 0.33
        else: return 1.0
    def get_crit_stage(self):
        if self.stage_critical_hit == 1: return 12.5
        elif self.stage_critical_hit == 2: return 25
        elif self.stage_critical_hit == 3: return 50
        elif self.stage_critical_hit == 4: return 100
        elif self.stage_critical_hit == 5: return 100
        elif self.stage_critical_hit == 6: return 100
        else: return 06.25
    def get_previous_level_exp(self, level=None):
        if level is None:
            level = self.level-1
        ##print "current {}, level = {}".format(self.level, level)
        return self.get_exp_for_level_up(level)
    def get_random_nature(self):
        nature = randint(1,24)
        if nature == 1: return constants.nat_lonely
        elif nature == 2: return constants.nat_brave 
        elif nature == 3: return constants.nat_adament 
        elif nature == 4: return constants.nat_naughty
        elif nature == 5: return constants.nat_bold
        elif nature == 6: return constants.nat_relaxed 
        elif nature == 7: return constants.nat_docile#
        elif nature == 8: return constants.nat_impish 
        elif nature == 9: return constants.nat_lax
        elif nature == 10: return constants.nat_modest
        elif nature == 11: return constants.nat_mild 
        elif nature == 12: return constants.nat_quiet
        elif nature == 13: return constants.nat_rash
        elif nature == 14: return constants.nat_quirky#
        elif nature == 15: return constants.nat_timid 
        elif nature == 16: return constants.nat_hasty 
        elif nature == 17: return constants.nat_jolly 
        elif nature == 18: return constants.nat_naive
        elif nature == 19: return constants.nat_calm 
        elif nature == 20: return constants.nat_bashful#
        elif nature == 21: return constants.nat_gentle 
        elif nature == 22: return constants.nat_sassy 
        elif nature == 23: return constants.nat_carful
        else: return constants.nat_hardy#
    def give_pokemon_random_item_from_item_list(self, item_list=None): # must be list of items
        if item_list is None:
            return None
        return item_list[randint(0,len(item_list)-1)]
    def set_random_gender(self):
        is_male = True
        is_female = True
        is_neutor = True
        if self.gender_varience[0] is 0:
            is_male = False
        if self.gender_varience[1] is 0:
            is_female = False
        if self.gender_varience[0] is not 0 or self.gender_varience[1] is not 0:
            is_neutor = False
        
        if not is_male and not is_female and is_neutor:
            self.gender =  constants.neutor
        if  (is_male or is_female) and not is_neutor:
            roll = randint(0,100)
            if roll >= int(self.gender_varience[0]):
                self.gender = constants.male
            else:
                self.gender =  constants.female
        else:
            self.gender = "???"
        return self
#Methods
    def has_type(self, type=None):
        for t in self.types:
            if t.name is type:
                return True
        return False
    def fully_heal(self):
        #print "IN HEAL"
        self.hp = self.get_max_hp()
        self.condition = [{constants.status_normal: None}]
        if len(self.moves) > 0:
            #print "\nmoves are greater then 0\n"
            for move in self.moves:
                if move is not None:
                    ##print str(move)
                    ##print move
                    move.pp = move.pp_max
        return self
    def add_move_to_pokemon(self, new_move=None):
        if new_move is None:
            return " Move is None."
        if len(self.moves) >= constants.max_moves:
            return constants.must_delete_move_first
        if isinstance(new_move, move):
            self.moves.append(new_move)
            return "{0} learned {1}!".format(self.nickname, new_move.name)
        else:
            return "{} is not of type \"class move()\", but of {}".format(new_move, type(new_move))
    def copy(self):
        pkm_to_copy = pokemon()
        # Personal Data
        pkm_to_copy.name = self.name
        pkm_to_copy.nickname = self.nickname
        pkm_to_copy.gender = self.gender
        pkm_to_copy.original_trainer = self.original_trainer
        pkm_to_copy.level = self.level 
        pkm_to_copy.hp = self.hp
        pkm_to_copy.condition = list(self.condition)
        pkm_to_copy.exp = self.exp 
        # Pokedex Data
        pkm_to_copy.generation_introducted = self.generation_introducted
        pkm_to_copy.types = list(self.types)
        pkm_to_copy.species = self.species
        pkm_to_copy.height = self.height
        pkm_to_copy.weight = self.weight
        pkm_to_copy.abilities = list(self.abilities)
        pkm_to_copy.ability = self.ability
        pkm_to_copy.local_numbers = dict(self.local_numbers)
        pkm_to_copy.japanese_name = self.japanese_name
        # where to find the pokemon
        pkm_to_copy.places_found = list(self.places_found)
        # Training Data
        pkm_to_copy.ev_yield = dict(self.ev_yield)
        pkm_to_copy.catch_rate = self.catch_rate # 3 (near impossible) - 255 (almost garunteeed)
        pkm_to_copy.happiness = self.happiness
        pkm_to_copy.base_exp = self.base_exp
        pkm_to_copy.growth_rate = self.growth_rate
        # Breeding Data
        pkm_to_copy.egg_types = list(self.egg_types)
        pkm_to_copy.gender_varience = list(self.gender_varience)
        pkm_to_copy.egg_cycles = self.egg_cycles
        pkm_to_copy.pokedex_entry = dict(self.pokedex_entry)
        pkm_to_copy.evolution = self.evolution
        # Moves
        pkm_to_copy.moves = list(self.moves)
        pkm_to_copy.moves_learned_by_level_up = dict(self.moves_learned_by_level_up)
        pkm_to_copy.moves_learned_by_egg = list(self.moves_learned_by_egg)
        pkm_to_copy.moves_learned_by_move_tutors = list(self.moves_learned_by_move_tutors)
        pkm_to_copy.moves_learned_by_machines = list(self.moves_learned_by_machines)
        pkm_to_copy.moves_learned_by_transfer = list(self.moves_learned_by_transfer)
        # icons
        self.sprite_icon = self.sprite_icon
        self.sprite_front = self.sprite_front
        self.sprite_back = self.sprite_back
        self.sprite_front_shiny = self.sprite_front_shiny
        self.sprite_back_shiny = self.sprite_back_shiny
        # Base stats
        pkm_to_copy.base_hp = self.base_hp
        pkm_to_copy.base_attack = self.base_attack
        pkm_to_copy.base_defense = self.base_defense
        pkm_to_copy.base_special_attack = self.base_special_attack
        pkm_to_copy.base_special_defense = self.base_special_defense
        pkm_to_copy.base_speed = self.base_speed
        # IV
        pkm_to_copy.iv_hp = self.iv_hp
        pkm_to_copy.iv_attack = self.iv_attack
        pkm_to_copy.iv_defense = self.iv_defense
        pkm_to_copy.iv_special_attack = self.iv_special_attack
        pkm_to_copy.iv_special_defense = self.iv_special_defense
        pkm_to_copy.iv_speed = self.iv_speed
        # EV
        pkm_to_copy.ev_hp = self.ev_hp
        pkm_to_copy.ev_attack = self.ev_attack
        pkm_to_copy.ev_defense = self.ev_defense
        pkm_to_copy.ev_special_attack = self.ev_special_attack
        pkm_to_copy.ev_special_defense = self.ev_special_defense
        pkm_to_copy.ev_speed = self.ev_speed
        # Stages variences 
        # 0 is normal, max, min 6,-6
        pkm_to_copy.stage_accuracy = self.stage_accuracy
        pkm_to_copy.stage_evasion = self.stage_evasion
        pkm_to_copy.stage_attack = self.stage_attack 
        pkm_to_copy.stage_defense = self.stage_defense
        pkm_to_copy.stage_special_attack = self.stage_special_attack
        pkm_to_copy.stage_special_defense = self.stage_special_defense
        pkm_to_copy.stage_speed = self.stage_speed
        # Natures variences 
        # 1.0 normal, 1.1 positive predisposition, 0.9 negative predisposition
        pkm_to_copy.nature_attack = self.nature_attack
        pkm_to_copy.nature_defense = self.nature_defense
        pkm_to_copy.nature_special_attack = self.nature_special_attack
        pkm_to_copy.nature_special_defense = self.nature_special_defense
        pkm_to_copy.nature_speed = self.nature_speed
        pkm_to_copy.hold_item = self.hold_item
        return pkm_to_copy
    def difference_between_stats_since_level_up(self):
        diff = "STATS:\n"
        ##print self.get_max_hp()
        ##print self.get_max_hp(level=self.level-1)
        hp_diff = self.get_max_hp() - self.get_max_hp(self.level-1)
        attack_diff = self.get_attack()-self.get_attack(self.level-1)
        defense_diff = self.get_defense()-self.get_defense(self.level-1)
        sp_att_diff = self.get_special_attack()-self.get_special_attack(self.level-1)
        sp_def_diff = self.get_special_defense()-self.get_special_defense(self.level-1)
        speed_diff = self.get_speed()-self.get_speed(self.level-1)
        diff += "{0:4}{1:5} + {2} = {3}\n".format('HP', self.get_max_hp(self.level-1), hp_diff, self.get_max_hp())
        diff += "{0:4}{1:5} + {2} = {3}\n".format('Att', self.get_attack(self.level-1), attack_diff, self.get_attack(),)
        diff += "{0:4}{1:5} + {2} = {3}\n".format('Def', self.get_defense(self.level-1), defense_diff, self.get_defense())
        diff += "{0:4}{1:5} + {2} = {3}\n".format('SA', self.get_special_attack(self.level-1), sp_att_diff, self.get_special_attack())
        diff += "{0:4}{1:5} + {2} = {3}\n".format('SD', self.get_special_defense(self.level-1), sp_def_diff, self.get_special_defense())
        diff += "{0:4}{1:5} + {2} = {3}\n".format('Spd', self.get_speed(self.level-1), speed_diff, self.get_speed())
        return diff
    def gain_level(self):
        if self.level < constants.max_level:
            self.level += 1
            self.next_level_exp = self.get_exp_for_level_up()
            self.hp += self.get_max_hp() - self.get_max_hp(self.level-1)
            return "{} grew to level {}!".format(self.nickname, self.level)
        return ""
    def earn_exp(self, exp=0, trainer=None):
        if self.is_fainted():
            return "{} is fainted and did not gain experience points.".format(self.nickname)
        magnitude_of_growth = 'grew'
        exp_string = ""
        if not isinstance(exp,int):
            return "exp is not an int"
        # Exp Modifiers
        if trainer is not None:
            if trainer.trainer_id not in self.original_trainer:
                print "trainer.trainer_id {} not in self.original_trainer {}".format(trainer.trainer_id, self.original_trainer)
                exp = int(exp * 1.5)
                magnitude_of_growth = 'boosted'
        #if self.get_affection_hearts() > 2:
        #    exp = int(exp * 1.2)
        #exp = exp * e = 1 # holding exp boost item
        #exp = exp * p = 1 # consumable exp boost item in effect
        #exp = exp * v = 1 # Above level of evolution
        #
        self.exp += exp
        exp_string += "{0} {1} by {2} Expience points!\n".format(self.nickname, magnitude_of_growth, exp)
        if self.exp >= self.get_exp_for_level_up():
            exp_string += self.gain_level() + "\n"
            exp_string += self.difference_between_stats_since_level_up()
        return exp_string
    def create_quick_new_custom_pokemon(full_dict=None, part_dict=None):
        if full_dict is None:
            #print "full_dict is None."
            return None
        if full_dict is None:
            #print "part_dict is None."
            return None
        return self
    def can_evolve_by_level_up(self):
        # self.evolution = [{"Ivysaur":{'level':16}}]
        if self.evolution is not None:
            for pkm in self.evolution:
                for key in pkm.keys():
                    level = pkm[key].get('level')
                    if level is not None:
                        if self.level is level:
                            return key
        return None
    def can_evolve_by_happiness(self):
        return None
    def can_evolve_with_item(self, item=None):
        if item is None:
            return None
        # self.evolution = [{"Ivysaur":{'level':16}}]
        if self.evolution is not None:
            for pkm in self.evolution:
                for key in pkm.keys():
                    item_name = pkm[key].get('item')
                    if item_name is not None:
                        if item.name is item_name:
                            return key
        return None        
    def evolve(self, pokemon_name=None):
        if pokemon_name is None:
            return self
        #print "{} evolving into {}".format(self.name, pokemon_name)
        evolution_pokemon = get_pokemon_for_evolution(pokemon_name=pokemon_name)
        #print evolution_pokemon
        print "{} evolving into {}".format(self.name, evolution_pokemon.name)
        #
        self.name = evolution_pokemon.name
        # Pokedex Data
        self.generation_introducted = evolution_pokemon.generation_introducted
        self.types = evolution_pokemon.types
        self.species = evolution_pokemon.species
        self.height = evolution_pokemon.height
        self.weight = evolution_pokemon.weight
        #
        found_ability = False
        for evolution_ability in evolution_pokemon.abilities:
            if self.ability.name is evolution_ability.name:
                found_ability = True
                # keeping ability
                break
        if not found_ability:
            self.abilities = evolution_pokemon.abilities
            self.choose_random_ability()
            self.ability = None
        #
        self.local_numbers = evolution_pokemon.local_numbers
        self.japanese_name = evolution_pokemon.japanese_name
        # where to find the pokemon
        self.places_found = evolution_pokemon.places_found
        # Training Data
        self.ev_yield = evolution_pokemon.ev_yield
        self.catch_rate = evolution_pokemon.catch_rate # 3 (near impossible) - 255 (almost garunteeed)
        self.base_exp = evolution_pokemon.base_exp
        self.growth_rate = evolution_pokemon.growth_rate
        # Breeding Data
        self.egg_types = evolution_pokemon.egg_types
        self.gender_varience = evolution_pokemon.gender_varience
        self.egg_cycles = evolution_pokemon.egg_cycles
        #self.stats = dict(constants.all_stat_format)
        self.pokedex_entry = evolution_pokemon.pokedex_entry
        self.evolution = evolution_pokemon.evolution
        # Moves

        self.moves_learned_by_level_up = evolution_pokemon.moves_learned_by_level_up
        self.moves_learned_by_egg = evolution_pokemon.moves_learned_by_egg
        self.moves_learned_by_move_tutors = evolution_pokemon.moves_learned_by_move_tutors
        self.moves_learned_by_machines = evolution_pokemon.moves_learned_by_machines
        self.moves_learned_by_transfer = evolution_pokemon.moves_learned_by_transfer
        # icons
        self.sprite_icon = evolution_pokemon.sprite_icon
        self.sprite_front = evolution_pokemon.sprite_front
        self.sprite_back = evolution_pokemon.sprite_back
        self.sprite_front_shiny = evolution_pokemon.sprite_front_shiny
        self.sprite_back_shiny = evolution_pokemon.sprite_back_shiny
        # Base stats
        current_max_hp = self.get_max_hp()
        self.base_hp =evolution_pokemon.base_hp
        evolution_max_hp = self.get_max_hp()
        difference = evolution_max_hp - current_max_hp
        self.hp += difference
        #
        #
        self.base_attack = evolution_pokemon.base_attack
        self.base_defense = evolution_pokemon.base_defense
        self.base_special_attack = evolution_pokemon.base_special_attack
        self.base_special_defense = evolution_pokemon.base_special_defense
        self.base_speed = evolution_pokemon.base_speed

        #
        return self
    
    # Battle and Encounter Methods
    def get_STAB(self, move=None):
        if move is None:
            return None
        move_type = move.type.name
        if self.ability.name is "Aerilate":
            move_type = constants.type_flying
        for type in self.types:
            if move_type is type.name:
                if self.ability.name is "Adaptability":
                    return 2.0
                return 1.5
        return 1
    def get_weakness_resistance_or_immunity(self, move=None):
        multiplier = 1
        if move is None:
            return None
        for type in self.types:
            #Weakness
            for weakness in type.weaknesses:
                if move.type.name is weakness: multiplier *= 2
            #Resistance
            for resistance in type.resistances:
                if move.type.name is resistance: multiplier *= 0.5
            #Immunity
            for immunity in type.immunities:
                if move.type.name is immunity: multiplier *= 0
            
        return multiplier
    def heal(self, amount=None):
        if amount is None:
            return self
        self.hp += amount
        if self.hp > self.get_max_hp():
            self.hp = self.get_max_hp()
        return self
    def take_damage(self, damage=None):
        if damage is None:
            return None
        self.hp -= damage
        if self.has_status_effect(constants.status_bide):
            for condition in self.conditions:
                if condition.get(constants.status_bide) is not None or condition.get('turns') is not None:
                    condition[constants.status_bide] += damage
                    #print "{} stored {} energy...".format(self.nickname, damage)
                if condition.get(constants.status_bracing):
                    if self.hp < 1:
                        self.hp = 1
        if self.hp < 1:
            print ""
            self.hp = 0
            self.conditions.append({constants.status_fainted: None})
            for condition in self.conditions: # []
            for condition_key in condition.keys(): # {}
                if constants.status_fainted in not condition_key or constants.status_destiny_bond in not condition_key:
                    self.conditions.remove(condition)
        return self
    def is_fainted(self):
            return self.has_status_effect(constants.status_fainted)
    # Capture methods
    def modified_catch_rate(self, ball_modifier=None):
        if ball_modifier is None:
            return 0
        if ball_modifier is constants.empty:
            # #print "     *** Master Ball *** "
            return 255
        status_mod = 1
        for condition in self.conditions:
            for key in condition.keys():
                if (constants.status_freeze in key or constants.status_sleep in key):
                    ##print "     *** affected by major status *** "
                    status_mod =  2
                elif (constants.status_paralysis in key or constants.status_burn in key or constants.status_poison in key or constants.status_badly_poison in key):
                    ##print "     *** affected by minor status *** "
                    status_mod =  1.5
        status_mod = Decimal(status_mod)
        max_hp = Decimal(self.get_max_hp())
        hp = Decimal(self.hp)
        catch_rate = Decimal(self.catch_rate)
        ball_modifier = Decimal(ball_modifier)
        # catch_value = ( (top_left - top_right) / bottom ) * catch_rate * ball_modifier * status_mod
        catch_value = Decimal(Decimal( (Decimal(3 * max_hp) - Decimal(2 * hp)) / Decimal(3 * max_hp) )* catch_rate * ball_modifier * status_mod)
        # #print "     *** modified_catch_rate = {} *** ".format(catch_value)
        return Decimal(catch_value) # int(int())
    def shake_probability(self, ball_modifier=None):
        if ball_modifier is None:
            return 0
        # returns between 0 and 65535 (inclusive)
        mod_catch_rate = Decimal(self.modified_catch_rate(ball_modifier))
        if mod_catch_rate is 0:
            mod_catch_rate += 1
        sqrt_sqrt_mod_catch_rate = Decimal(sqrt( sqrt( 16711680 /  mod_catch_rate)))
        if sqrt_sqrt_mod_catch_rate is 0:
            sqrt_sqrt_mod_catch_rate += 1
        shake = 1048560 / Decimal(sqrt_sqrt_mod_catch_rate)
        
        return  int(int(shake))
    def shake_check(self, ball_modifier=None):
        #print "\n*** must roll less then shake_proabability to succeed ***\n"
        success = False
        if ball_modifier is None:
            print "pokemon.shake_check ball_modifier is {}".format(ball_modifier)
            return False 
        # roll is between 0 and 65535 (inclusive)
        roll = randint(0,65535)
        shake_prob = self.shake_probability(ball_modifier)
        #print "     *** shake_proabability = {} *** ".format(shake_prob)
        
        #print "     *** roll = {} *** ".format(roll)
        if roll < shake_prob:
            #print "     *** Shake Check Succeeded *** "
            success = True
        #else:
            #print "     *** Shake Check Failed *** "
        return success
    #STATUS EFFECTS
    def has_status_effect(self, status_effect=None, move=None):
        if status_effect is None:
            return False
        for condition in self.conditions: # []
            for condition_key in condition.keys(): # {}
                if status_effect.lower() in condition_key.lower() and status_effect[0].lower() == condition_key[0].lower():
                    if condition.get('move') is not None and move is not None:
                        if move.lower()[0] == condition.get('move').lower()[0] and move.lower() in condition.get('move').lower():
                            return True
                    else:
                        return True
        return False
    def has_non_volitile_status_effect(self):
        if (self.has_status_effect(status_effect=constants.status_paralysis) 
        or self.has_status_effect(status_effect=constants.status_poison)
        or self.has_status_effect(status_effect=constants.status_badly_poison) 
        or self.has_status_effect(status_effect=constants.status_sleep) 
        or self.has_status_effect(status_effect=constants.status_burn) 
        or self.has_status_effect(status_effect=constants.status_freeze) 
        ):
            return True
        return False
    def get_status_effect(self, status_effect=None):
        if status_effect is None:
            return None
        for condition in self.conditions: # []
            for condition_key in condition.keys(): # {}
                if status_effect.lower() in condition_key.lower() and status_effect.lower()[0] == condition_key.lower()[0]:
                    return condition
        return None
    def return_pokemon(self):
        self.remove_status_effect(status_name=constants.status_flinch)
        return self
    def remove_status_effect(self, status_name=None, move=None):
        if status_name is None:
            return None
        for condition in self.conditions: # []
            for condition_key in condition.keys(): # {}
                if status_name in condition_key:
                    if condition.get('move') is not None and condition.get('move') is move:
                        self.conditions.remove(condition)
                    elif condition.get('move') is not None and condition.get('move') is not move:
                        continue
                    else:
                        self.conditions.remove(condition)
                    return True
        return False
    def remove_non_volitile_status_effect(self, status_name=None):
        if status_name is None:
            return None
        if (status_name is constants.status_paralysis 
            or status_name is constants.status_badly_poison 
            or status_name is constants.status_poison 
            or status_name is constants.status_sleep 
            or status_name is constants.status_freeze 
            or status_name is constants.status_burn):
            self.remove_status_effect(status_name)
            self.conditions.append({constants.status_normal: None})
            return True
        return False
    def can_be_affected(self,status=None):
        if status is None:
            return True
        if status is constants.status_paralysis:
            if self.ability.name is "Limber" or self.has_type(type="Electric"):
                return False
        if status is constants.status_poison or status is constants.status_badly_poison:
            if self.ability.name is "Immunity" or self.has_type(type="Steel") or self.has_type(type="Poison"):
                return False
        if status is constants.status_burn:
            if self.ability.name is "Water Veil" or self.has_type(type="Fire"):
                return False
        if status is constants.status_freeze:
            if self.has_type(type="Fire"):
                return False
        return True
    def clear_stat_changes(self):
        self.stage_attack = 0
        self.stage_defense = 0
        self.stage_special_attack = 0
        self.stage_special_defense = 0
        self.stage_speed = 0
        self.stage_critical_hit = 0
        self.stage_accuracy = 0
        self.stage_evasion = 0
        return self
    def apply_effect_on_pokemon(self, effect=None, move=None):
        if self is None:
            print "in battle.move_effect_on_pokemon self is None"
            return None
        if effect is None:
            print "in battle.move_effect_on_pokemon effect is None"
            return None
        #print effect
        ret_str = ""
        # lowers users hp from fierce attack
        if constants.status_recoil_damage in effect: # lowers users hp from fierce attack
            damage = get_int_from_string(text=effect)
            if damage is not None:
                multiplier = 1
                if constants.three_quarters in effect:
                    multiplier = .75
                if constants.two_thirds in effect:
                    multiplier = .67
                if constants.half in effect:
                    multiplier = .5
                if constants.third in effect:
                    multiplier = .33
                if constants.quarter in effect:
                    multiplier = .25
                if constants.eighth in effect:
                    multiplier = .125
                if constants.sixteenth in effect:
                    multiplier = .0625
                damage = float(damage) * multiplier
                damage = int(damage)
                amount = 0
                hp_before = 0
                self.take_damage(damage)
                amount = hp_before - self.hp
                ret_str += "{} took {} damage in recoil!\n".format(self.nickname, amount)
        # removes status condition
        elif constants.status_hurt_self in effect: # removes status condition
            print constants.reset_status
        # decreases Stat stage
        elif constants.reduces in effect: # decreases Stat stage
            print constants.reduces
            if constants.attack in effect:
                print constants.attack
                if constants.by_1_stage in effect:
                    self.stage_attack -= 1
                    ret_str += "{}'s attack fell!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_attack -= 2
                    ret_str += "{}'s attack fell sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_attack -= 3
                    ret_str += "{}'s attack fell drastically!\n".format(self.nickname)
                if self.stage_attack < -6:
                    self.stage_attack = -6
            if constants.defense in effect:
                print constants.defense
                if constants.by_1_stage in effect:
                    self.stage_defense -= 1
                    ret_str += "{}'s defense sharply!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_defense -= 2
                    ret_str += "{}'s defense fell sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_defense -= 3
                    ret_str += "{}'s defense fell drastically!\n".format(self.nickname)
                if self.stage_defense < -6:
                    self.stage_defense = -6
            if constants.speed in effect:
                print constants.speed
                if constants.by_1_stage in effect:
                    self.stage_speed -= 1
                    ret_str += "{}'s speed sharply!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_speed -= 2
                    ret_str += "{}'s speed fell sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_speed -= 3
                    ret_str += "{}'s speed fell drastically!\n".format(self.nickname)
                if self.stage_speed < -6:
                    self.stage_speed = -6
            if constants.special_attack in effect:
                print constants.special_attack
                if constants.by_1_stage in effect:
                    self.stage_special_attack -= 1
                    ret_str += "{}'s special attack fell!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_special_attack -= 2
                    ret_str += "{}'s special attack fell sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_special_attack -= 3
                    ret_str += "{}'s special attack fell drastically!\n".format(self.nickname)
                if self.stage_special_attack < -6:
                    self.stage_special_attack = -6
            if constants.special_defense in effect:
                print constants.special_defense
                if constants.by_1_stage in effect:
                    self.stage_special_defense -= 1
                    ret_str += "{}'s special defense fell!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_special_defense -= 2
                    ret_str += "{}'s special defense fell sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_special_defense -= 3
                    ret_str += "{}'s special defense fell drastically!\n".format(self.nickname)
                if self.stage_special_defense < -6:
                    self.stage_special_defense = -6
            if constants.accuracy in effect:
                print constants.accuracy
                if constants.by_1_stage in effect:
                    self.stage_accuracy -= 1
                    ret_str += "{}'s accuracy fell!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_accuracy -= 2
                    ret_str += "{}'s accuracy fell sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_accuracy -= 3
                    ret_str += "{}'s accuracy fell drastically!\n".format(self.nickname)
                if self.stage_accuracy < -6:
                    self.stage_accuracy = -6
            if constants.critical_hit in effect:
                print constants.critical_hit
                if constants.by_1_stage in effect:
                    self.stage_critical_hit -= 1
                    ret_str += "{}'s critical hit ratio fell!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_critical_hit -= 2
                    ret_str += "{}'s critical hit ratio fell sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_critical_hit -= 3
                    ret_str += "{}'s critical hit ratio fell drastically!\n".format(self.nickname)
                if self.stage_critical_hit < 0:
                    self.stage_critical_hit = 0
            if constants.evasion in effect:
                print constants.evasion
                if constants.by_1_stage in effect:
                    self.stage_evasion -= 1
                    ret_str += "{}'s evasion fell!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_evasion -= 2
                    ret_str += "{}'s evasion fell sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_evasion -= 3
                    ret_str += "{}'s evasion fell drastically!\n".format(self.nickname)
                if self.stage_evasion < -6:
                    self.stage_evasion = -6
        elif constants.remove_stat_changes in effect:
            print constants.remove_stat_changes
            if constants.all_stat in effect:
                self.clear_stat_changes()
            if constants.attack in effect:
                self.stage_attack = 0
            if constants.defense in effect:
                self.stage_defense = 0
            if constants.speed in effect:
                self.stage_speed = 0
            if constants.special_attack in effect:
                self.stage_special_attack = 0
            if constants.special_defense in effect:
                self.stage_special_defense = 0
            if constants.accuracy in effect:
                self.stage_accuracy = 0
            if constants.evasion in effect:
                self.stage_evasion = 0
            if constants.critical_hit in effect:
                self.stage_critical_hit = 0
            
        # increases Stat stage
        elif constants.increases in effect: # increases Stat stage
            print constants.increases
            if constants.random_stat in effect:
                roll = randint(1,7)
                if roll == 1:
                    print "stat change {} becomes {}".format(constants.random_stat, constants.attack)
                    effect = effect.replace(constants.random_stat, constants.attack)
                elif roll == 2:
                    print "stat change {} becomes {}".format(constants.random_stat, constants.defense)
                    effect = effect.replace(constants.random_stat, constants.defense)
                elif roll == 3:
                    print "stat change {} becomes {}".format(constants.random_stat, constants.speed)
                    effect = effect.replace(constants.random_stat, constants.speed)
                elif roll == 4:
                    print "stat change {} becomes {}".format(constants.random_stat, constants.special_attack)
                    effect = effect.replace(constants.random_stat, constants.special_attack)
                elif roll == 5:
                    print "stat change {} becomes {}".format(constants.random_stat, constants.special_defense)
                    effect = effect.replace(constants.random_stat, constants.special_defense)
                elif roll == 6:
                    print "stat change {} becomes {}".format(constants.random_stat, constants.accuracy)
                    effect = effect.replace(constants.random_stat, constants.accuracy)
                else:
                    print "stat change {} becomes {}".format(constants.random_stat, constants.evasion)
                    effect = effect.replace(constants.random_stat, constants.evasion)
            if constants.all_stat in effect:
                print constants.all_stat
                all_stats = "{} {} {} {} {}".format(constants.attack, constants.defense, constants.special_attack, constants.special_defense, constants.speed)
                effect = effect.replace(constants.all_stat, all_stats)
            if constants.attack in effect:
                print constants.attack
                if constants.by_1_stage in effect:
                    self.stage_attack += 1
                    ret_str += "{}'s attack increased!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_attack += 2
                    ret_str += "{}'s attack increased sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_attack += 3
                    ret_str += "{}'s attack increased drastically!\n".format(self.nickname)
                if self.stage_attack > 6:
                    self.stage_attack = 6
            if constants.defense in effect:
                print constants.defense
                if constants.by_1_stage in effect:
                    self.stage_defense += 1
                    ret_str += "{}'s defense increased!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_defense += 2
                    ret_str += "{}'s defense increased sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_defense += 3
                    ret_str += "{}'s defense increased drastically!\n".format(self.nickname)
                if self.stage_defense > 6:
                    self.stage_defense = 6
            if constants.speed in effect:
                print constants.speed
                if constants.by_1_stage in effect:
                    self.stage_speed += 1
                    ret_str += "{}'s speed increased!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_speed += 2
                    ret_str += "{}'s speed increased sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_speed += 3
                    ret_str += "{}'s speed increased drastically!\n".format(self.nickname)
                if self.stage_speed > 6:
                    self.stage_speed = 6
            if constants.special_attack in effect:
                print constants.special_attack
                if constants.by_1_stage in effect:
                    self.stage_special_attack += 1
                    ret_str += "{}'s special attack increased!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_special_attack += 2
                    ret_str += "{}'s special attack increased sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_special_attack += 3
                    ret_str += "{}'s special attack increased drastically!\n".format(self.nickname)
                if self.stage_special_attack > 6:
                    self.stage_special_attack = 6
            if constants.special_defense in effect:
                print constants.special_defense
                if constants.by_1_stage in effect:
                    self.stage_special_defense += 1
                    ret_str += "{}'s special defense increased!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_special_defense += 2
                    ret_str += "{}'s special defense increased sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_special_defense += 3
                    ret_str += "{}'s special defense increased drastically!\n".format(self.nickname)
                if self.stage_special_defense > 6:
                    self.stage_special_defense = 6
            if constants.accuracy in effect:
                print constants.accuracy
                if constants.by_1_stage in effect:
                    self.stage_accuracy += 1
                    ret_str += "{}'s accuracy increased!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_accuracy += 2
                    ret_str += "{}'s accuracy increased sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_accuracy += 3
                    ret_str += "{}'s accuracy increased drastically!\n".format(self.nickname)
                if self.stage_accuracy > 6:
                    self.stage_accuracy = 6
            if constants.crit_ratio in effect:
                print constants.crit_ratio
                if constants.by_1_stage in effect:
                    self.stage_critical_hit += 1
                    ret_str += "{}'s critical hit ratio increased!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_critical_hit += 2
                    ret_str += "{}'s critical hit ratio increased sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_accuracy += 3
                    ret_str += "{}'s accuracy increased drastically!\n".format(self.nickname)
                if self.stage_critical_hit > 6:
                    self.stage_critical_hit = 6
            if constants.evasion in effect:
                print constants.evasion
                if constants.by_1_stage in effect:
                    self.stage_evasion += 1
                    ret_str += "{}'s evasion increased!\n".format(self.nickname)
                if constants.by_2_stages in effect:
                    self.stage_evasion += 2
                    ret_str += "{}'s evasion increased sharply!\n".format(self.nickname)
                if constants.by_3_stages in effect:
                    self.stage_evasion += 3
                    ret_str += "{}'s evasion increased drastically!\n".format(self.nickname)
                if self.stage_evasion > 6:
                    self.stage_evasion = 6
        # inflicts Status condition
        elif constants.inflict in effect: # inflicts Status condition
            print constants.inflict
            if constants.set_amount_of_damage in effect:
                dmg = get_int_from_string(text=effect)
                self.take_damage(dmg)
                ret_str += "{} took {} damage!\n".format(self.nickname, dmg)
            if constants.status_user_faints in effect:
                self.take_damage(self.hp)
            #
            # Status Infliction
            #
            if constants.status_paralysis in effect and not self.has_non_volitile_status_effect():
                #print constants.status_paralysis
                #for condition in self.conditions:
                #    if constants.status_normal in condition.keys() and self.can_be_affected(status=constants.status_paralysis):
                if self.has_status_effect(constants.status_normal):
                    self.conditions.remove({constants.status_normal:None})
                    self.conditions.append({constants.status_paralysis: '25% chance to Fail Attack'})
                    ret_str += "{} became paralyzed!\n".format(self.nickname)
            #
            elif constants.status_poison in effect and constants.status_badly_poison not in effect and not self.has_non_volitile_status_effect():
                #print constants.status_poison
                #for condition in self.conditions:
                #    if constants.status_normal in condition.keys():
                if self.has_status_effect(constants.status_normal):
                    self.conditions.remove({constants.status_normal:None})
                    self.conditions.append({constants.status_poison: None})
                    ret_str += "{} was poisoned!\n".format(self.nickname)
            elif constants.status_badly_poison in effect and not self.has_non_volitile_status_effect():
                #print constants.status_badly_poison
                if self.has_status_effect(constants.status_normal):
                    self.conditions.remove({constants.status_normal:None})
                    self.conditions.append({constants.status_badly_poison: 1})
                    ret_str += "{} was badly poisoned!\n".format(self.nickname)
            #
            elif constants.status_sleep in effect and not self.has_non_volitile_status_effect():
                #print constants.status_sleep
                #for condition in self.conditions:
                if self.has_status_effect(constants.status_normal):
                    self.remove_status_effect(constants.status_normal)
                    turns_to_sleep = randint(1,4)
                    print "Will sleep {} turns.\n".format(turns_to_sleep)
                    self.conditions.append({constants.status_sleep: randint(1,4)})
                    ret_str += "{} fell asleep!\n".format(self.nickname)
            #
            elif constants.status_burn in effect and not self.has_non_volitile_status_effect():
                #print constants.status_burn
                #for condition in self.conditions:
                if self.has_status_effect(constants.status_normal):
                    self.conditions.remove({constants.status_normal:None})
                    self.conditions.append({constants.status_burn: None})
                    ret_str += "{} was burned!\n".format(self.nickname)
            #
            elif constants.status_freeze in effect and not self.has_non_volitile_status_effect():
                #print constants.status_freeze
                #for condition in self.conditions:
                if self.has_status_effect(constants.status_normal):
                    self.conditions.remove({constants.status_normal:None})
                    self.conditions.append({constants.status_freeze: '20% chance to Remove'})
                    ret_str += "{} became encased in ice! It's frozen solid!\n".format(self.nickname)
            #
            # volitile status inflictions
            #
            elif constants.status_flinch in effect and not self.has_status_effect(status_effect=constants.status_flinch):
                self.conditions.append({constants.status_flinch: None})
                ret_str += ""#"{} became confused!".format(self.nickname)
            elif constants.status_confusion in effect and not self.has_status_effect(status_effect=constants.status_confusion):
                self.conditions.append({constants.status_confusion: '25% chance to Hurt Self'})
                ret_str += "{} became confused!\n".format(self.nickname)
            elif constants.status_cursed in effect and not self.has_status_effect(status_effect=constants.status_cursed):
                #print constants.status_cursed
                self.conditions.append({constants.status_cursed : None})
                ret_str += "{} was cursed!\n".format(self.nickname)
            elif constants.status_attracted in effect and not self.has_status_effect(status_effect=constants.status_attracted):
                #print constants.status_attracted
                print "{} Added to Status condition so {}".format(constants.status_attracted, self.nickname)
                self.conditions.append({constants.status_attracted: None})
                ret_str += "{} became infatuated!\n".format(self.nickname)
            elif constants.status_partially_trapped in effect:
                print constants.status_partially_trapped
                self.conditions.append({constants.status_partially_trapped: randint(4,5), 'move': move})
                ret_str += "{} was trapped by {}!\n".format(self.nickname, move)
            elif constants.status_trapped in effect and not self.has_status_effect(status_effect=constants.status_trapped):
                #print constants.status_trapped
                self.conditions.append({constants.status_trapped: None})
                ret_str += "{} was trapped!\n".format(self.nickname)
            elif constants.status_perish_song in effect and not self.has_status_effect(status_effect=constants.status_perish_song):
                #print constants.status_perish_song
                self.conditions.append({constants.status_perish_song: 4} )
            elif constants.status_heal_block in effect and not self.has_status_effect(status_effect=constants.status_heal_block):
                #print constants.status_heal_block
                self.conditions.append({constants.status_heal_block: None})
                ret_str += "{} was blocked from getting healed!\n".format(self.nickname)
            elif constants.status_leech_seed in effect and not self.has_status_effect(status_effect=constants.status_leech_seed):
                #print constants.status_leech_seed
                self.conditions.append({constants.status_leech_seed : None})
                ret_str += "{} was seeded!\n".format(self.nickname)
            elif constants.status_taunted in effect and not self.has_status_effect(status_effect=constants.status_taunted):
                #print constants.status_taunted
                self.conditions.append({constants.status_taunted: None})
                ret_str += "{} was tauned!\n".format(self.nickname)
            elif constants.status_levitation in effect and not self.has_status_effect(status_effect=constants.status_levitation):
                #print constants.status_levitation
                self.conditions.append({constants.status_levitation: None})
                ret_str += "{} started to levitate!\n".format(self.nickname)
            elif constants.status_torment in effect and not self.has_status_effect(status_effect=constants.status_torment):
                #print constants.status_torment
                self.conditions.append({constants.status_torment: None} )
                ret_str += "{} was subjected to torment!\n".format(self.nickname)  
            elif constants.disables_move in effect and not self.has_status_effect(status_effect=constants.disables_move):
                print constants.disables_move
                if len(self.moves) > 1:
                    roll = randint(0,len(self.moves)-1)
                    selected_move = self.moves[roll]
                    print selected_move
                    self.conditions.append({constants.disables_move: selected_move, 'turns': randint(1,8)} )
                    ret_str += "{}'s {} was Disabled!\n".format(self.nickname, selected_move.name)  
                else:
                    ret_str += "{} could not be disabled!".format(self.nickname)
        #
        elif constants.bestow in effect: # bestow Status condition
            print constants.bestow
            
            # Bide
            if constants.status_bide in effect:
                print constants.status_bide
                self.conditions.append({constants.status_bide: 0, 'turns': 2})
                ret_str += "{} started to store energy!\n".format(self.nickname)
            # Status Conditions
            #
            if constants.status_aqua_ring in effect:
                print constants.status_aqua_ring
                self.conditions.append({constants.status_aqua_ring: None})
                ret_str += "{} was subjected to torment!\n".format(self.nickname)
            #
            if constants.status_bracing in effect:
                print constants.status_bracing
                self.conditions.append({constants.status_bracing: None})
                ret_str += "{} braced itself!\n".format(self.nickname)
            #
            if constants.status_focusing in effect:
                print constants.status_focusing
                self.conditions.append({constants.status_focusing: None})
                ret_str += "{} tightened its focus!\n".format(self.nickname)
            #
            if constants.status_rooted in effect:
                print constants.status_rooted
                self.conditions.append({constants.status_rooted: None})
                ret_str += "{} planted roots!\n".format(self.nickname)
            #
            if constants.status_reflect in effect:
                print constants.status_reflect
                self.conditions.append({constants.status_reflect: 5})
                ret_str += "{} protected by a physical screen!\n".format(self.nickname)
            #
            if constants.status_light_screen in effect:
                print constants.status_light_screen
                self.conditions.append({constants.status_light_screen: 5})
                ret_str += "{} protected by a shimmering screen!\n".format(self.nickname)
            #
            if constants.status_magic_coat in effect:
                print constants.status_magic_coat
                self.conditions.append({constants.status_magic_coat: None})
                ret_str += "{} shrowded with a Magic Coat!\n".format(self.nickname)
            #
            if constants.status_magnetic_levitation in effect:
                print constants.status_magnetic_levitation
                self.conditions.append({constants.status_magnetic_levitation : None})
                ret_str += "{} started to levitate!\n".format(self.nickname)
            #
            if constants.status_minimized in effect:
                print constants.status_minimized
                self.conditions.append({constants.status_minimized: None})
                ret_str += "{} shrunk to a smaller size!\n".format(self.nickname)
            #
            if constants.status_recharging in effect:
                print constants.status_recharging
                self.conditions.append({constants.status_recharging: None})
                ret_str += "{} is recharging!\n".format(self.nickname)
            #
            if constants.status_semi_invulnerable in effect:
                print constants.status_semi_invulnerable
                self.conditions.append({constants.status_semi_invulnerable: None} )
                
            #
            if constants.status_substituted in effect:
                print constants.status_substituted
                self.conditions.append({constants.status_substituted: None})
                ret_str += "{} is hiding behind a substitute!\n".format(self.nickname)
            #
            if constants.status_taking_aim in effect:
                print constants.status_taking_aim
                self.conditions.append({constants.status_taking_aim: None})
                ret_str += "{} took aim!\n".format(self.nickname)
            #
            if constants.status_withdrawing in effect:
                print constants.status_withdrawing
                self.conditions.append({constants.status_withdrawing: None})
                ret_str += "{} has withdrawn!\n".format(self.nickname)
        #
        elif constants.remove in effect: # Remove Status condition
            #print constants.remove
            ret_str = ""
            if constants.status_all_negative in effect:
                if self.has_status_effect(constants.status_paralysis):
                    self.remove_status_effect(constants.status_paralysis)
                    self.conditions.append({constants.status_normal: None})
                    ret_str += "{} {} {}!\n".format(self.nickname, "was cured of its", constants.status_paralysis)
                
                if self.has_status_effect(constants.status_badly_poison):
                    self.remove_status_effect(constants.status_badly_poison)
                    self.conditions.append({constants.status_normal: None})
                    ret_str += "{} {} {}!\n".format(self.nickname, "is no longed", constants.status_badly_poison)
                
                if self.has_status_effect(constants.status_poison):
                    self.remove_status_effect(constants.status_poison)
                    self.conditions.append({constants.status_normal: None})
                    ret_str += "{} {} {}!\n".format(self.nickname, "was cured of its", constants.status_poison)
                
                if self.has_status_effect(constants.status_sleep):
                    self.remove_status_effect(constants.status_sleep)
                    self.conditions.append({constants.status_normal: None})
                    ret_str += "{} {} {}!\n".format(self.nickname, "woke up from its", constants.status_sleep)
                
                if self.has_status_effect(constants.status_burn):
                    self.remove_status_effect(constants.status_burn)
                    self.conditions.append({constants.status_normal: None})
                    ret_str += "{} {} {}!\n".format(self.nickname, "was cured of its", constants.status_burn)
                
                if self.has_status_effect(constants.status_freeze):
                    self.remove_status_effect(constants.status_freeze)
                    self.conditions.append({constants.status_normal: None})
                    ret_str += "{} {}!".format(self.nickname, "thawed out")
                
                if self.has_status_effect(constants.status_confusion):
                    self.remove_status_effect(constants.status_confusion)
                    ret_str += "{} {} {}!\n".format(self.nickname, "is no longed", constants.status_confusion)
                
                if self.has_status_effect(constants.status_attracted):
                    self.remove_status_effect(constants.status_attracted)
                    ret_str += "{} {} {}!\n".format(self.nickname, "was cured of its", constants.status_attracted)
                
                if self.has_status_effect(constants.status_cursed):
                    self.remove_status_effect(constants.status_cursed)
                    ret_str += "{} {} {}!\n".format(self.nickname, "was cured of its", constants.status_cursed)
                
            #
            elif self.has_status_effect(constants.status_paralysis):
                self.remove_status_effect(constants.status_paralysis)
                self.conditions.append({constants.status_normal: None})
                ret_str += "{} {} {}!\n".format(self.nickname, "was cured of its", constants.status_paralysis)
            
            elif self.has_status_effect(constants.status_badly_poison):
                self.remove_status_effect(constants.status_badly_poison)
                self.conditions.append({constants.status_normal: None})
                ret_str += "{} {} {}!\n".format(self.nickname, "is no longed", constants.status_badly_poison)
            
            elif self.has_status_effect(constants.status_poison):
                self.remove_status_effect(constants.status_poison)
                self.conditions.append({constants.status_normal: None})
                ret_str += "{} {} {}!\n".format(self.nickname, "was cured of its", constants.status_poison)
            
            elif self.has_status_effect(constants.status_sleep):
                self.remove_status_effect(constants.status_sleep)
                self.conditions.append({constants.status_normal: None})
                ret_str += "{} {} {}!\n".format(self.nickname, "woke up from its", constants.status_sleep)
            
            elif self.has_status_effect(constants.status_burn):
                self.remove_status_effect(constants.status_burn)
                self.conditions.append({constants.status_normal: None})
                ret_str += "{} {} {}!\n".format(self.nickname, "was cured of its", constants.status_burn)
            
            elif self.has_status_effect(constants.status_freeze):
                self.remove_status_effect(constants.status_freeze)
                self.conditions.append({constants.status_normal: None})
                ret_str += "{} {}!\n".format(self.nickname, "thawed out")
            
            elif self.has_status_effect(constants.status_confusion):
                self.remove_status_effect(constants.status_confusion)
                ret_str += "{} {} {}!\n".format(self.nickname, "is no longed", constants.status_confusion)
            
            elif self.has_status_effect(constants.status_attracted):
                self.remove_status_effect(constants.status_attracted)
                ret_str += "{} {} {}!\n".format(self.nickname, "was cured of its", constants.status_attracted)
            
            elif self.has_status_effect(constants.status_cursed):
                self.remove_status_effect(constants.status_cursed)
                ret_str += "{} {} {}!\n".format(self.nickname, "was cured of its", constants.status_cursed)
        #
        elif constants.recovers in effect:  # recovers HP
            print constants.recovers
            
            if constants.health in effect:
                heal_amount = self.get_max_hp()
            else:
                heal_amount = get_int_from_string(text=effect)
            multiplier = 1
            if constants.three_quarters in effect:
                multiplier = .75
            if constants.two_thirds in effect:
                multiplier = .67
            if constants.half in effect:
                multiplier = .5
            if constants.third in effect:
                multiplier = .33
            if constants.quarter in effect:
                multiplier = .25
            heal_amount = int (heal_amount * multiplier)
            print "heal: {}".format(heal_amount)
            amount = 0
            hp_before = 0
            if heal_amount > 0:
                hp_before = self.hp
                self.hp += heal_amount
                if self.hp > self.get_max_hp():
                    self.hp = self.get_max_hp()
            amount = self.hp - hp_before
            ret_str += "{} recovered {} HP!\n".format(self.nickname, amount)   
            #if constants.status_sleep in effect:
            #    print constants.status_sleep
            #    for condition in self.conditions: # []
            #        for condition_key in condition.keys(): # {}
            #            if constants.status_sleep in condition_key
            #                self.conditions.remove(condition)
            #
            #if constants.status_burn in effect:
            #    print constants.status_burn
            #    for condition in self.conditions: # []
            #        for condition_key in condition.keys(): # {}
            #            if constants.status_burn in condition_key
            #                self.conditions.remove(condition)
            # 
            #
            #if constants.status_freeze in effect:
            #    print constants.status_freeze
            #    for condition in self.conditions: # []
            #        for condition_key in condition.keys(): # {}
            #            if constants.status_freeze in condition_key
            #                self.conditions.remove(condition)
            #
        #
        return ret_str
    #
#
#
#
#