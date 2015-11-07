from random import randint
from constants import constants
from utilities import *
from abilities import *
from moves import *

# search by name or number #1, bulbasaur
######
pokemon_d = {'name': "", 
'generation introduced': 1, 
'types': [constants.type_unknown],
'species': "{} Pokemon".format(""), 
'height': "{0}\'{1}\" ({2}m)".format("","",""),
'weight': "{0} lbs ({1}kg)".format("",""),
'abilities': [],
'local numbers': {'Local': 0, 'National': 0},
'japanese name': "", 
'ev yield': {constants.ev_hp: 0, 
constants.ev_attack: 0, 
constants.ev_defense: 0, 
constants.ev_special_attack: 0, 
constants.ev_special_defense: 0, 
constants.ev_speed: 0},
'catch rate': 255,
'base happiness': constants.base_happiness,
'base xp': 100,
'growth rate': constants.growthrate_medium_slow,
'egg types': ['???'],
'gender varience': constants.equal_male_female, 
'egg cycles': 21,
constants.base_hp: 0, 
constants.base_attack: 0, 
constants.base_defense: 0,
constants.base_special_attack: 0, 
constants.base_special_defense: 0, 
constants.base_speed: 0,
'evolution': None, # [{"pokemon_name": {'level':num}}] [{"pokemon_name": {'stone':"stone_name"}}],
'level up moves': {
1: [move().copy()]
}, 
'egg moves': [],'learnable moves': [],
'pokedex entry': {'data': "."}
}
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
#
#
#
#
#
#