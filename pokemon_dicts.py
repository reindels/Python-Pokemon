from random import randint
from constants import constants
from utilities import *
from abilities import *
from moves import *

# search by name or number #1, bulbasaur
######
pokemon_d = {'name': "NAME", 
'generation introduced': 1, 
'types': [constants.type_normal],
'species': "{} Pokemon".format("SPECIES"), 
'height': "{0}\'{1}\" ({2}m)".format("0","0","0"),
'weight': "{0} lbs ({1}kg)".format("0","0"),
'abilities': [],
'local numbers': {'Local': 1, 'National': 1},
'japanese name': "JAPANESE NAME", 
'ev yield': {constants.ev_hp: 0, 
constants.ev_attack: 0, 
constants.ev_defense: 0, 
constants.ev_special_attack: 0, 
constants.ev_special_defense: 0, 
constants.ev_speed: 0},
'catch rate': 255, #255 is max, min is 3
'base happiness': constants.base_happiness,
'base xp': 0,
'growth rate': constants.growthrate_medium_slow, # default
'egg types': [],
'gender varience': constants.mostly_male, 
'egg cycles': 21, # default
constants.base_hp: 0, 
constants.base_attack: 0, 
constants.base_defense: 0,
constants.base_special_attack: 0, 
constants.base_special_defense: 0, 
constants.base_speed: 0,
'evolution': [], # [{"pokemon_name": {'level':num}}] [{"pokemon_name": {'item':"stone_name"}}],
'level up moves': {
1: [tackle.copy()],
}, 
'egg moves': [splash.copy()],
'learnable moves': [flail.copy()],
'pokedex entry': {'data': "Flavor text."}
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