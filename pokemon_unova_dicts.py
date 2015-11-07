from random import randint
from constants import constants
from utilities import *
from abilities import *
from moves import *

# search by name or number #1, bulbasaur
######
#
pokemon_d = {'name': "Victini", 
'generation introduced': 5, 
'types': [constants.type_grass, constants.type_poison],
'species': "{} Pokemon".format("Victory"), 
'height': 1.0,
'weight': 1.0,
'abilities': [victory_star],
'local numbers': {'Local': 494, 'National': 494},
'japanese name': "Victini", 
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
'egg types': ['Grass'],
'gender varience': constants.equal_male_female, 
'egg cycles': 21,
constants.base_hp: 0, 
constants.base_attack: 0, 
constants.base_defense: 0,
constants.base_special_attack: 0, 
constants.base_special_defense: 0, 
constants.base_speed: 0,
'evolution': None, # [{"pokemon_name": {'level':num}}] [{"pokemon_name": {'item':"stone_name"}}],
'level up moves': {
1: [tackle.copy()]
}, 
'egg moves': [],
'learnable moves': [],
'pokedex entry': {'data': "."}
}
#
#
#
#
#
#
#
# 602
tynamo_d = {'name': "Tynamo", 
'generation introduced': 5, 
'types': [constants.type_electric],
'species': "{} Pokemon".format("EleFish"), 
'height': .2,
'weight': .3,
'abilities': [levitate],
'local numbers': {'Local': 602, 'National': 602},
'japanese name': "Shibishirasu", 
'ev yield': {constants.ev_hp: 0, 
constants.ev_attack: 0, 
constants.ev_defense: 0, 
constants.ev_special_attack: 0, 
constants.ev_special_defense: 0, 
constants.ev_speed: 1},
'catch rate': 190,
'base happiness': constants.base_happiness,
'base xp': 55,
'growth rate': constants.growthrate_slow,
'egg types': ['Amorphous'],
'gender varience': constants.equal_male_female, 
'egg cycles': 21,
constants.base_hp: 35, 
constants.base_attack: 55, 
constants.base_defense: 40,
constants.base_special_attack: 45, 
constants.base_special_defense: 40, 
constants.base_speed: 60,
'evolution': [{"Eelektrik":{'level':39}}], # [{"pokemon_name": {'level':num}}] [{"pokemon_name": {'item':"stone_name"}}],
'level up moves': {
1: [charge_beam.copy(), spark.copy(), tackle.copy(), thunder_wave.copy()]
}, 
'egg moves': [],
'learnable moves': [magnet_rise.copy(), charge_beam.copy(), spark.copy(), tackle.copy(), thunder_wave.copy()],
'pokedex entry': {'data': "One alone can emit only a trickle of electricity, so a group of them gathers to unleash a powerful electric shock."}
}
# 603
eelektrik_d = {'name': "Eelektrik", 
'generation introduced': 5, 
'types': [constants.type_electric],
'species': "{} Pokemon".format("EleFish"), 
'height': 1.19,
'weight': 22.0,
'abilities': [levitate],
'local numbers': {'Local': 603, 'National': 603},
'japanese name': "Shibibiiru", 
'ev yield': {constants.ev_hp: 0, 
constants.ev_attack: 2, 
constants.ev_defense: 0, 
constants.ev_special_attack: 0, 
constants.ev_special_defense: 0, 
constants.ev_speed: 0},
'catch rate': 60,
'base happiness': constants.base_happiness,
'base xp': 142,
'growth rate': constants.growthrate_slow,
'egg types': ['Amorphous'],
'gender varience': constants.equal_male_female, 
'egg cycles': 21,
constants.base_hp: 65, 
constants.base_attack: 85, 
constants.base_defense: 70,
constants.base_special_attack: 75, 
constants.base_special_defense: 70, 
constants.base_speed: 40,
'evolution': [{"Eelektross":{'item':"Thunder Stone"}}], # [{"pokemon_name": {'level':num}}] [{"pokemon_name": {'item':"stone_name"}}],
'level up moves': {
1: [charge_beam.copy(), spark.copy(), tackle.copy(), thunder_wave.copy()],
9: [bind.copy()],
19: [acid.copy()],
29: [discharge.copy()],
39: [crunch.copy()],
44: [thunderbolt.copy()],
49: [acid_spray.copy()],
54: [coil.copy()],
59: [wild_charge.copy()],
64: [gastro_acid.copy()],
69: [zap_cannon.copy()],
74: [thrash.copy()]
}, 
'egg moves': [],
'learnable moves': [magnet_rise.copy(), charge_beam.copy(), spark.copy(), tackle.copy(), thunder_wave.copy(), aqua_tail.copy(), bind.copy(), 
bounce.copy(), endure.copy(), gastro_acid.copy(), giga_drain.copy(), iron_tail.copy(), knock_off.copy(), shock_wave.copy(), signal_beam.copy(), 
snore.copy(), super_fang.copy(), tackle.copy(), toxic.copy(), hidden_power.copy(), light_screen.copy(), protect.copy(), rain_dance.copy(), 
frustration.copy(), thunderbolt.copy(), thunder.copy(), return_.copy(), double_team.copy(), facade.copy(), rest.copy(), attract.copy(), 
round.copy(), acrobatics.copy(), flash.copy(), volt_switch.copy(), thunder_wave.copy(), swagger.copy(), sleep_talk.copy(), u_turn.copy(), 
substitute.copy(), flash_cannon.copy(), wild_charge.copy(), secret_power.copy(), confide.copy(), ],
'pokedex entry': {'data': "One alone can emit only a trickle of electricity, so a group of them gathers to unleash a powerful electric shock."}
}
# 604
eelektross_d = {'name': "Eelektross", 
'generation introduced': 5, 
'types': [constants.type_electric],
'species': "{} Pokemon".format("EleFish"), 
'height': 2.11,
'weight': 80.5,
'abilities': [levitate],
'local numbers': {'Local': 604, 'National': 604},
'japanese name': "Shibirudon", 
'ev yield': {constants.ev_hp: 0, 
constants.ev_attack: 3, 
constants.ev_defense: 0, 
constants.ev_special_attack: 0, 
constants.ev_special_defense: 0, 
constants.ev_speed: 0},
'catch rate': 30,
'base happiness': constants.base_happiness,
'base xp': 232,
'growth rate': constants.growthrate_slow,
'egg types': ['Amorphous'],
'gender varience': constants.equal_male_female, 
'egg cycles': 21,
constants.base_hp: 85, 
constants.base_attack: 115, 
constants.base_defense: 80,
constants.base_special_attack: 105, 
constants.base_special_defense: 80, 
constants.base_speed: 50,
'evolution': None, # [{"pokemon_name": {'level':num}}] [{"pokemon_name": {'item':"stone_name"}}],
'level up moves': {
1: [acid.copy(), coil.copy(), crunch.copy(), crush_claw.copy(), discharge.copy(), 
gastro_acid.copy(), headbutt.copy(), ion_deluge.copy(), thrash.copy(), zap_cannon.copy()],
}, 
'egg moves': [],
'learnable moves': [acid.copy(), coil.copy(), crunch.copy(), crush_claw.copy(), discharge.copy(), gastro_acid.copy(), headbutt.copy(), ion_deluge.copy(), thrash.copy(), zap_cannon.copy(),
aqua_tail.copy(), bind.copy(), bounce.copy(), dragon_pulse.copy(), drain_punch.copy(), endure.copy(), fire_punch.copy(), focus_punch.copy(), 
gastro_acid.copy(), giga_drain.copy(), iron_tail.copy(), knock_off.copy(), magnet_rise.copy(), outrage.copy(), shock_wave.copy(), signal_beam.copy(), 
snore.copy(), super_fang.copy(), supepower.copy(), thunder_punch.copy(), acid_spray.copy(), bind.copy(), charge_beam.copy(), spark.copy(), 
tackle.copy(), thunder_wave.copy(), thunderbolt.copy(), wild_charge.copy(), cut.copy(), strength.copy(), rock_smash.copy(), hone_claws.copy(), 
dragon_claw.copy(), roar.copy(), toxic.copy(), hidden_power.copy(), hyper_beam.copy(), light_screen.copy(), protect.copy(), rain_dance.copy(), 
frustration.copy(), thunderbolt.copy(), thunder.copy(), return_.copy(), brick_break.copy(), double_team.copy(), flamethrower.copy(), rock_tomb.copy(), 
facade.copy(), rest.copy(), attract.copy(), round.copy(), acrobatics.copy(), giga_impact.copy(), flash.copy(), volt_switch.copy(), thunder_wave.copy(), 
rock_slide.copy(), dragon_tail.copy(), grass_knot.copy(), swagger.copy(), sleep_talk.copy(), u_turn.copy(), substitute.copy(), 
flash_cannon.copy(), secret_power.copy(), power_up_punch.copy(), confide.copy()],
'pokedex entry': {'data': "One alone can emit only a trickle of electricity, so a group of them gathers to unleash a powerful electric shock."}
}
#
#
#
#
#
#
#
#