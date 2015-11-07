'''
TO-DO:
work on:
After me and priority assignment
Assurance
work on attract, make only work for opposite gender
Beat up
Electric Terrain
Electrify
fell stinger
'''
from constants import constants
#

#
_dict = {
'name': "",
'type': constants.type_unknown,
'category': constants.move_category_physical,
'power': None,
'accuracy': None,
'pp': 0,
'multi-hit':[2,5],
'priority': 0,
'critical hit': 0,
'generation introducted': 1,
'effects': [],
'description': "",
'machine': None,
}
hit_self_in_confusion_dict = {
'name': "Hit it self in its confusion",
'type': None,
'category': constants.move_category_physical,
'power': 40,
'accuracy': 100,
'generation introducted': 1,
'effects': [],
'description': "Hits itself in its confusion.",
'machine': None,
}
#"{} {} {} {} {}".format("10% chance to ", constants.increases , constants.pkm_self , constants.attack , constants.by_1_stage )
# stat change
#'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_poison, constants.pkm_foe)],
# status condition
#'effects': ["{} {} {} {} {}".format("% chance to ", constants. , constants. , constants. , constants. )],
#
#a,
absorb_dict = {
'name': "Absorb",
'type': constants.type_grass,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.recovers, constants.half, constants.damage_delt)],
'description': "",
'power': 20,
'accuracy': 100,
'pp': 25
}
acid_dict = {
'name': "Acid",
'type': constants.type_poison,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("10% chance to ", constants.reduces, constants.pkm_foe, constants.special_defense, constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': None,
'pp': 30
}
acid_armor_dict = {
'name': "Acid Armor",
'type': constants.type_poison,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.defense, constants.by_2_stages)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
acid_spray_dict = {
'name': "Acid Spray",
'type': constants.type_poison,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.special_defense, constants.by_2_stages)],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 20
}
acrobatics_dict = {
'name': "Acrobatics",
'type': constants.type_flying,
'category': constants.move_category_physical,
'effects': ["Stronger when the user does not have a held item."],
'description': "",
'power': 55,
'accuracy': 100,
'pp': 15
}
acupressure_dict = {
'name': "Acupressure",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.random_stat, constants.by_2_stages )],
'description': "",
'power': None,
'accuracy': None,
'pp': 30
}
aerial_ace_dict = {
'name': "Aerial Ace",
'type': constants.type_flying,
'category': constants.move_category_physical,
'effects': ["{} {} {}".format(constants.ignores, constants.pkm_self, constants.accuracy), 
"{} {} {}".format(constants.ignores, constants.pkm_foe, constants.evasion)],
'description': "",
'power': 60,
'accuracy': 1000,
'pp': 20
}
aeroblast_dict = {
'name': "Aeroblast",
'type': constants.type_flying,
'category': constants.move_category_special,
'effects': [constants.high_crit_ratio],
'description': "",
#high_crit_ratio
'power': 100,
'accuracy': 95,
'pp': 5
}
after_you_dict = {
'name': "After You",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["Gives {} to {}".format(constants.priority, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
agility_dict = {
'name': "Agility",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.speed, constants.by_2_stages)],
'description': "",
'power': None,
'accuracy': None,
'pp': 30
}
air_cutter_dict = {
'name': "Air Cutter",
'type': constants.type_flying,
'category': constants.move_category_special,
'effects': [constants.high_crit_ratio],
'description': "",
'power': 60,
'accuracy': 95,
'pp': 25
}
air_slash_dict = {
'name': "Air Slash",
'type': constants.type_flying,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 75,
'accuracy': 95,
'pp': 20
}
ally_switch_dict = {
'name': "Ally Switch",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["Swaps Place with Ally".format()],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
amnesia_dict = {
'name': "Anmesia",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.special_defense, constants.by_2_stages)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
ancient_power_dict = {
'name': "Ancient Power",
'type': constants.type_rock,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("10% chance to ", constants.increases, constants.pkm_self, constants.all_stats, constants.by_1_stage)],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 5
}
aqua_jet_dict = {
'name': "Aqua Jet",
'type': constants.type_water,
'category': constants.move_category_physical,
'effects': [],# none
'description': "",
'priority': 1,
'power': 40,
'accuracy': 100,
'pp': 20
}
aqua_ring_dict = {
'name': "Aqua Ring",
'type': constants.type_water,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.bestow, constants.status_aqua_ring, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
aqua_tail_dict = {
'name': "Aqua Tail",
'type': constants.type_water,
'category': constants.move_category_physical,
'effects': [],# none
'description': "",
'power': 90,
'accuracy': 90,
'pp': 10
}
arm_thrust_dict = {
'name': "Arm Thrust",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],# none
'description': "",
'power': 15,
'accuracy': None,
'pp': 20,
'multi-hit':[2,5]
}
aromatherapy_dict = {
'name': "Aromatherapy",
'type': constants.type_grass,
'category': constants.move_category_status,
'effects': ["{} {} {} {} ".format(constants.remove, constants.status_all_negative, constants.status_infliction, constants.pkm_all_in_party)],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
aromatic_mist_dict = {
'name': "Aromatic Mist",
'type': constants.type_fairy,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_all_allies , constants.special_defense , constants.by_1_stage )],
'power': None,
'accuracy': 100,
'pp': 20
}
assist_dict = {
'name': "Assist",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["In a Double Battle, user randomly attacks with a partner's move."],
'power': None,
'accuracy': None,
'pp': 20
}
assurance_dict = {
'name': "Assurance",
'type': constants.type_dark,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.doubles_if_hit],
'priority': -4,
'power': 60,
'accuracy': 100,
'pp': 10
}
astonish_dict = {
'name': "Astonish",
'type': constants.type_ghost,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 30,
'accuracy': 100,
'pp': 15
}
attack_order_dict = {
'name': "Attack Order",
'type': constants.type_bug,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.high_crit_ratio],
'power': 90,
'accuracy': 100,
'pp': 15
}
attract_dict = {
'name': "Attract",
'type': constants.type_normal,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 15
}
aura_sphere_dict = {
'name': "Aura Sphere",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {}".format(constants.ignores, constants.pkm_self, constants.accuracy), 
"{} {} {}".format(constants.ignores, constants.pkm_foe, constants.evasion)],
'power': 80,
'accuracy': 100,
'pp': 20
}
aurora_beam_dict = {
'name': "Aurora Beam",
'type': constants.type_ice,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("10% chance to ", constants.reduces, constants.pkm_foe, constants.speed, constants.by_1_stage)],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 20
}
autotomize_dict = {
'name': "Autotomize",
'type': constants.type_steel,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {}".format(constants.half, constants.weight),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.speed, constants.by_2_stages)],
'power': None,
'accuracy': None,
'pp': 15
}
avalanche_dict = {
'name': "Avalanche",
'type': constants.type_ice,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.doubles_if_hit],
'priority': -4,
'power': 60,
'accuracy': 100,
'pp': 10
}
#b,
baby_doll_eyes_dict = {
'name': "Baby Doll Eyes",
'type': constants.type_fairy,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.attack, constants.by_1_stage)],
'priority': 1,
'power': None,
'accuracy': 100,
'pp': 30
}
barrage_dict = {
'name': "Barrage",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 15,
'accuracy': 85,
'pp': 20,
'multi-hit':[2,5]
}
barrier_dict = {
'name': "Barrier",
'type': constants.type_psychic,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.defense, constants.by_2_stages)],
'power': None,
'accuracy': None,
'pp': 20
}
baton_pass_dict = {
'name': "Baton Pass",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {}".format(constants.pkm_self, constants.switches_ally, constants.transfer_stats_changes)],
'power': None,
'accuracy': None,
'pp': 40
}
beat_up_dict = {
'name': "Beat Up",
'type': constants.type_dark,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 0
}
belch_dict = {
'name': "Belch",
'type': constants.type_poison,
'category': constants.move_category_special,
'description': "",
'effects': ["Requires a held Berry to attack."],
'power': 120,
'accuracy': 90,
'pp': 10
}
belly_drum_dict = {
'name': "Belly Drum",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["{} to {} {} on {} ".format(constants.pkm_self, constants.inflict, constants.half, constants.health),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.attack, constants.by_6_stages)],
'power': None,
'accuracy': None,
'pp': 10
}
bestow_dict = {
'name': "Bestow",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["Gives the User Held Item to the Foe."],
'power': None,
'accuracy': None,
'pp': 15
}
bide_dict = {
'name': "Bide",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} ".format(constants.pkm_self, constants.bestow, constants.status_bide)],
'power': None,
'accuracy': None,
'pp': 10
}
bind_dict = {
'name': "Bind",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {}".format(constants.inflict, constants.status_partially_trapped, constants.pkm_foe)],
'power': 15,
'accuracy': 85,
'pp': 20
}
bite_dict = {
'name': "Bite",
'type': constants.type_dark,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 60,
'accuracy': 100,
'pp': 25
}
blast_burn_dict = {
'name': "Blast Burn",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {}".format(constants.bestow, constants.status_recharge, constants.pkm_self)],
'power': 150,
'accuracy': 90,
'pp': 5
}
blaze_kick_dict = {
'name': "Blaze Kick",
'type': constants.type_fire,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.high_crit_ratio, 
"{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'power': 85,
'accuracy': 90,
'pp': 10
}
blizzard_dict = {
'name': "Blizzard",
'type': constants.type_ice,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_freeze, constants.pkm_foe)],
'power': 110,
'accuracy': 70,
'pp': 5
}
block_dict = {
'name': "Block",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_trapped, constants.pkm_foe)],
'power': None,
'accuracy': None,
'pp': 5
}
blue_flare_dict = {
'name': "Blue Flare",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("20% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'power': 130,
'accuracy': 85,
'pp': 5
}
body_slam_dict = {
'name': "Body Slam",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'power': 65,
'accuracy': 100,
'pp': 15
}
bolt_strike_dict = {
'name': "Bolt Strike",
'type': constants.type_electric,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("20% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'power': 130,
'accuracy': 85,
'pp': 5
}
bone_club_dict = {
'name': "Bone Club",
'type': constants.type_ground,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 65,
'accuracy': 85,
'pp': 20
}
bone_rush_dict = {
'name': "Bone Rush",
'type': constants.type_ground,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,5],
'power': 25,
'accuracy': 90,
'pp': 10
}
bonemerang_dict = {
'name': "Bonemerang",
'type': constants.type_ground,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,2],
'power': 50,
'accuracy': 90,
'pp': 10
}
boomburst_dict = {
'name': "Boomburst",
'type': constants.type_ground,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 65,
'accuracy': 85,
'pp': 20
}
bounce_dict = {
'name': "Bounce",
'type': constants.type_flying,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe),
"{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_flying),
"{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_semi_invulnerable)
],
'power': 85,
'accuracy': 85,
'pp': 5
}
brave_bird_dict = {
'name': "Brave Bird",
'type': constants.type_flying,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.status_recoil_damage, constants.third, constants.damage_delt)],
'power': 120,
'accuracy': 100,
'pp': 15
}
brick_break_dict = {
'name': "Brock Break",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': ["Breaks through Reflect and Light Screen barriers."],
'power': 75,
'accuracy': 100,
'pp': 15
}
brine_dict = {
'name': "Brine",
'type': constants.type_water,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 65,
'accuracy': 100,
'pp': 10
}
bubble_dict = {
'name': "Bubble",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("10% chance to ", constants.reduces, constants.pkm_foe, constants.speed, constants.by_1_stage)],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 30
}
bubble_beam_dict = {
'name': "Bubble Beam",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("10% chance to ", constants.reduces, constants.pkm_foe, constants.speed, constants.by_1_stage)],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 20
}
bug_bite_dict = {
'name': "Bug Bite",
'type': constants.type_bug,
'category': constants.move_category_physical,
'description': "",
'effects': ["Receives the effect from the opponent's held berry."],
'power': 60,
'accuracy': 100,
'pp': 20
}
bug_buzz_dict = {
'name': "Bug Buzz",
'type': constants.type_bug,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 90,
'accuracy': 100,
'pp': 10
}
bulk_up_dict = {
'name': "Bulk Up",
'type': constants.type_fighting,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.attack , constants.by_1_stage ),
"{} {} {} {}".format(constants.increases , constants.pkm_self , constants.defense , constants.by_1_stage )],
'power': None,
'accuracy': None,
'pp': 20
}
bulldoze_dict = {
'name': "Bulldoze",
'type': constants.type_ground,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 60,
'accuracy': 100,
'pp': 20
}
bullet_punch_dict = {
'name': "Bullet Punch",
'type': constants.type_steel,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 40,
'accuracy': 100,
'pp': 30
}
bullet_seed_dict = {
'name': "Bullet Seed",
'type': constants.type_grass,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,5],
'power': 25,
'accuracy': 100,
'pp': 30
}

#c,
calm_mind_dict = {
'name': "Calm Mind",
'type': constants.type_psychic,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.special_attack , constants.by_1_stage ),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.special_defense, constants.by_1_stage)],
'power': None,
'accuracy': None,
'pp': 20
}
camouflage_dict = {
'name': "Camouflage",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 20
}
captivate_dict = {
'name': "Captivate",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 40
}
celebrate_dict = {
'name': "Celebrate",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 40
}
charge_dict = {
'name': "Charge",
'type': constants.type_electric,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.special_defense, constants.by_1_stage),
"{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_charged)],
'power': None,
'accuracy': None,
'pp': 20
}
charge_beam_dict = {
'name': "Charge Beam",
'type': constants.type_electric,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {} {}".format("70% chance", constants.increases, constants.pkm_self, constants.special_attack, constants.by_1_stage)],
'power': 50,
'accuracy': 90,
'pp': 10
}
charm_dict = {
'name': "Charm",
'type': constants.type_fairy,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.attack, constants.by_2_stages)],
'power': None,
'accuracy': 100,
'pp': 20
}
chatter_dict = {
'name': "Chatter",
'type': constants.type_flying,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("Guranteed", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'power': 65,
'accuracy': 100,
'pp': 20
}
chip_away_dict = {
'name': "Chip Away",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': 70,
'accuracy': 100,
'pp': 20
}
circle_throw_dict = {
'name': "Circle Throw",
'type': constants.type_fairy,
'category': constants.move_category_status,
'description': "",
'effects': [constants.switches_opponent],
'power': 60,
'accuracy': 90,
'pp': 10
}
clamp_dict = {
'name': "Clamp",
'type': constants.type_water,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {}".format(constants.inflict, constants.status_partially_trapped, constants.pkm_foe)],
'power': 35,
'accuracy': 85,
'pp': 10
}
clear_smog_dict = {
'name': "Clear Smog",
'type': constants.type_poison,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {}".format(constants.remove_stat_changes, constants.all_stats, constants.pkm_foe)],
'power': 35,
'accuracy': 85,
'pp': 10
}
close_combat_dict = {
'name': "Close Combat",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_self, constants.special_attack, constants.by_1_stage),
"{} {} {} {}".format(constants.reduces, constants.pkm_self, constants.special_defense, constants.by_1_stage)],
'power': 120,
'accuracy': 100,
'pp': 5
}
coil_dict = {
'name': "Coil",
'type': constants.type_poison,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.attack, constants.by_1_stage),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.defense, constants.by_1_stage),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.accuracy, constants.by_1_stage),],
'power': None,
'accuracy': None,
'pp': 20
}
comet_punch_dict = {
'name': "Coil",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,5],
'power': 18,
'accuracy': 85,
'pp': 15
}
confide_dict = {
'name': "Confide",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.special_attack, constants.by_1_stage)],
'power': None,
'accuracy': None,
'pp': 20
}
confuse_ray_dict = {
'name': "Confuse Ray",
'type': constants.type_ghost,
'category': constants.move_category_status,
'description': "",
'effects': ["{} to {} {} on {} ".format("Guranteed", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'power': None,
'accuracy': 100,
'pp': 10
}
confusion_dict = {
'name': "Confusion",
'type': constants.type_psychic,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'power': 50,
'accuracy': 100,
'pp': 25
}
constrict_dict = {
'name': "Constrict",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {} {}".format("10% chance to ", constants.reduces, constants.pkm_self, constants.speed, constants.by_1_stage)],
'power': 10,
'accuracy': 100,
'pp': 35
}
conversion_dict = {
'name': "Conversion",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 30
}
conversion_2_dict = {
'name': "Conversion 2",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 30
}
copycat_dict = {
'name': "Copycat",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["Copies opponent's last move."],
'power': None,
'accuracy': None,
'pp': 20
}
cosmic_power_dict = {
'name': "Cosmic Power",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.defense , constants.by_1_stage ),
"{} {} {} {}".format(constants.increases , constants.pkm_self , constants.special_defense , constants.by_1_stage )],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
cotton_guard_dict = {
'name': "Cotton Guard",
'type': constants.type_grass,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.defense , constants.by_3_stages)],
'power': None,
'accuracy': None,
'pp': 10
}
cotton_spore_dict = {
'name': "Cotton Spore",
'type': constants.type_grass,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe , constants.speed , constants.by_2_stages)],
'power': None,
'accuracy': 100,
'pp': 40
}
counter_dict = {
'name': "Counter",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 20
}
covet_dict = {
'name': "Covet",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 60,
'accuracy': 100,
'pp': 20
}
crabhammer_dict = {
'name': "Crabhammer",
'type': constants.type_water,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.high_crit_ratio],
'power': 100,
'accuracy': 80,
'pp': 10
}
crafty_shield_dict = {
'name': "Crafty Shield",
'type': constants.type_fairy,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 10
}
cross_chop_dict = {
'name': "Cross Chop",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.high_crit_ratio],
'power': 100,
'accuracy': 80,
'accuracy': 80,
'pp': 5
}
cross_poison_dict = {
'name': "Cross Poison",
'type': constants.type_poison,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("10 % chance", constants.inflict, constants.status_poison, constants.pkm_foe, constants.high_crit_ratio)],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 20
}
crunch_dict = {
'name': "Crunch",
'type': constants.type_dark,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {} {}".format("20 % chance", constants.reduces, constants.pkm_foe, constants.defense, constants.by_1_stage)],
'power': 80,
'accuracy': 100,
'pp': 15
}
crush_claw_dict = {
'name': "Crush Claw",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {} {}".format("50 % chance", constants.reduces, constants.pkm_foe, constants.defense, constants.by_1_stage)],
'power': 75,
'accuracy': 95,
'pp': 10
}
crush_grip_dict = {
'name': "Crush Grip",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 5
}
curse_dict = {
'name': "Curse",
'type': constants.type_ghost,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 10
}
cut_dict = {
'name': "Cut",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 50,
'accuracy': 100,
'pp': 30
}
#d,
dark_pulse_dict = {
'name': "Dark Pulse",
'type': constants.type_dark,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("20% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 80,
'accuracy': 100,
'pp': 15
}
dark_void_dict = {
'name': "Dark Void",
'type': constants.type_dark,
'category': constants.move_category_status,
'description': "",
'effects': ["{} to {} {} on {} ".format("Guranteed", constants.inflict, constants.status_sleep, constants.pkm_all_other)],
'power': None,
'accuracy': 80,
'pp': 10
}
dazzling_gleam_dict = {
'name': "Dazzling Gleam",
'type': constants.type_fairy,
'category': constants.move_category_special,
'description': "",
'effects': ["Hits {} Pokemon".format(constants.pkm_all_other)],
'power': 80,
'accuracy': 100,
'pp': 10
}
defend_order_dict = {
'name': "Defend Order",
'type': constants.type_bug,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.defense, constants.by_1_stage),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.special_defense, constants.by_1_stage)],
'power': None,
'accuracy': None,
'pp': 10
}
defense_curl_dict = {
'name': "Defend Order",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.defense, constants.by_1_stage),
"{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_defense_curl)],
'power': None,
'accuracy': None,
'pp': 40
}
defog_dict = {
'name': "Defog",
'type': constants.type_flying,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe, constants.evasion, constants.by_1_stage)],
'power': None,
'accuracy': None,
'pp': 15
}
destiny_bond_dict = {
'name': "Destiny Bond",
'type': constants.type_ghost,
'category': constants.move_category_status,
'description': "",
'effects': ["If the user faints, the opponent also faints."],
'power': None,
'accuracy': None,
'pp': 5
}
detect_dict = {
'name': "Detect",
'type': constants.type_fighting,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_protected)],
'power': None,
'accuracy': None,
'pp': 5
}
diamond_storm_dict = {
'name': "Diamond Storm",
'type': constants.type_rock,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format("50% chance to", constants.increases , constants.pkm_self, constants.evasion, constants.by_1_stage)],
'power': 100,
'accuracy': 95,
'pp': 5
}
dig_dict = {
'name': "Dig",
'type': constants.type_ground,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_digging),
"{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_semi_invulnerable)],
'power': 80,
'accuracy': 100,
'pp': 10
}
disable_dict = {
'name': "Disable",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {}".format(constants.inflict, constants.pkm_foe, constants.disables_move)],
'power': None,
'accuracy': 100,
'pp': 20
}
disarming_voice_dict = {
'name': "Disarming Voice",
'type': constants.type_fairy,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 40,
'accuracy': 1000,
'pp': 15
}
discharge_dict = {
'name': "Discharge",
'type': constants.type_electric,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'power': 80,
'accuracy': 100,
'pp': 15
}
dive_dict = {
'name': "Dive",
'type': constants.type_water,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_diving),
"{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_semi_invulnerable)],
'power': 80,
'accuracy': 100,
'pp': 10
}
dizzy_punch_dict = {
'name': "Dizzy Punch",
'type': constants.type_water,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("20% chance", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'power': 70,
'accuracy': 100,
'pp': 10
}
doom_desire_dict = {
'name': "Doom Desire",
'type': constants.type_steel,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 140,
'accuracy': 100,
'pp': 5
}
double_hit_dict = {
'name': "Double Hit",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,2],
'power': 35,
'accuracy': 90,
'pp': 10
}
double_kick_dict = {
'name': "Double Kick",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,2],
'power': 30,
'accuracy': 100,
'pp': 30
}
double_slap_dict = {
'name': "Double Slap",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,5],
'power': 15,
'accuracy': 85,
'pp': 10
}
double_team_dict = {
'name': "Double Team",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.evasion , constants.by_1_stage )],
'power': None,
'accuracy': None,
'pp': 15
}
double_edge_dict = {
'name': "Double-Edge",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.pkm_self,  constants.status_recoil_damage, constants.third, constants.damage_delt)],
'power': 120,
'accuracy': 100,
'pp': 15
}
draco_meteor_dict = {
'name': "Draco Meteor",
'type': constants.type_dragon,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_self, constants.special_attack, constants.by_2_stage)],
'power': 130,
'accuracy': 90,
'pp': 5
}
dragon_ascent_dict = {
'name': "Dragon Ascent",
'type': constants.type_flying,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_self, constants.defense, constants.by_1_stage),
"{} {} {} {}".format(constants.reduces, constants.pkm_self, constants.special_defense, constants.by_1_stage)],
'power': 120,
'accuracy': 100,
'pp': 5
}
dragon_breath_dict = {
'name': "Dragon Breath",
'type': constants.type_dragon,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'power': 60,
'accuracy': 100,
'pp': 20
}
dragon_claw_dict = {
'name': "Dragon Claw",
'type': constants.type_dragon,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 80,
'accuracy': 100,
'pp': 15
}
dragon_dance_dict = {
'name': "Dragon Dance",
'type': constants.type_dragon,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.attacl, constants.by_1_stage),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.speed, constants.by_1_stage)],
'power': None,
'accuracy': None,
'pp': 20
}
dragon_pulse_dict = {
'name': "Dragon Pulse",
'type': constants.type_dragon,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 85,
'accuracy': 100,
'pp': 10
}
dragon_rage_dict = {
'name': "Dragon Rage",
'type': constants.type_dragon,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} to {}".format(constants.inflict, constants.set_amount_of_damage, 40, constants.pkm_foe)],
'power': None,
'accuracy': 100,
'pp': 10
}
dragon_rush_dict = {
'name': "Dragon Rush",
'type': constants.type_dragon,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("20% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 100,
'accuracy': 75,
'pp': 10
}
dragon_tail_dict = {
'name': "Dragon Tail",
'type': constants.type_dragon,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.switches_opponent],
'power': 60,
'accuracy': 90,
'pp': 10
}
drain_punch_dict = {
'name': "Drain Punch",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.recovers, constants.half, constants.damage_delt)],
'power': 75,
'accuracy': 100,
'pp': 10
}
draining_kiss_dict = {
'name': "Draining Kiss",
'type': constants.type_fairy,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {}".format(constants.recovers, constants.three_quarters, constants.health, constants.pkm_self)],
'power': 50,
'accuracy': 100,
'pp': 10
}
dream_eater_dict = {
'name': "Dream Eater",
'type': constants.type_psychic,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {} {} {} {}".format(constants.pkm_foe, constants.must_have_status, constants.status_sleep, constants.pkm_self, constants.recovers, constants.half, constants.damage_delt)],
'power': 100,
'accuracy': 100,
'pp': 15
}
drill_peck_dict = {
'name': "Drill Peck",
'type': constants.type_flying,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 80,
'accuracy': 100,
'pp': 20
}
drill_run_dict = {
'name': "Drill Run",
'type': constants.type_ground,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.high_crit_ratio],
'power': 80,
'accuracy': 95,
'pp': 10
}
dual_chop_dict = {
'name': "Dual Chop",
'type': constants.type_ground,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,2],
'power': 40,
'accuracy': 90,
'pp': 15
}
dynamic_punch_dict = {
'name': "Dynamic Punch",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("Guranteed", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'power': 100,
'accuracy': 50,
'pp': 5
}
#e,
earth_power_dict = {
'name': "Earth power",
'type': constants.type_ground,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {} {}".format("10% chance", constants.reduces, constants.pkm_foe, constants.special_defense, constants.by_1_stage)],
'power': 90,
'accuracy': 100,
'pp': 10
}
earthquake_dict = {
'name': "Earthquake",
'type': constants.type_ground,
'category': constants.move_category_physical,
'description': "",
'effects': ["Power is doubled if opponent is underground from using Dig."],
'power': 100,
'accuracy': 100,
'pp': 10
}
echoed_voice_dict = {
'name': "Echoed Voice",
'type': constants.type_normal,
'category': constants.move_category_special,
'description': "",
'effects': ["Power increases each turn."],
'power': 40,
'accuracy': 100,
'pp': 15
}
eerie_impulse_dict = {
'name': "Eerie Impulse",
'type': constants.type_electric,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.special_attack, constants.by_2_stages)],
'power': None,
'accuracy': 100,
'pp': 10
}
egg_bomb_dict = {
'name': "Egg Bomb",
'type': constants.type_electric,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 100,
'accuracy': 75,
'pp': 10
}
electric_terrain_dict = {
'name': "Electric Terrain",
'type': constants.type_electric,
'category': constants.move_category_status,
'description': "",
'effects': ["Prevents all Pokémon from falling asleep for 5 turns."],
'power': None,
'accuracy': None,
'pp': 10
}
electrify_dict = {
'name': "Electrify",
'type': constants.type_electric,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 20
}
electro_ball_dict = {
'name': "Electro Ball",
'type': constants.type_electric,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 20
}
electroweb_dict = {
'name': "Electroweb",
'type': constants.type_electric,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.speed, constants.by_1_stage)],
'power': 55,
'accuracy': 95,
'pp': 15
}
embargo_dict = {
'name': "Embargo",
'type': constants.type_dark,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} on {} ".format(constants.inflict, constants.status_embargo, constants.pkm_foe)],
'power': None,
'accuracy': 100,
'pp': 15
}
ember_dict = {
'name': "Ember",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'power': 40,
'accuracy': 100,
'pp': 25
}
encore_dict = {
'name': "Encore",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 5
}
endeavor_dict = {
'name': "Endeavor",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 5
}
endure_dict = {
'name': "Endure",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 10
}
energy_ball_dict = {
'name': "Energy Ball",
'type': constants.type_grass,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 90,
'accuracy': 100,
'pp': 10
}
entertainment_dict = {
'name': "Entertainment",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 15
}
eruption_dict = {
'name': "Eruption",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 150,
'accuracy': 100,
'pp': 5
}
explosion_dict = {
'name': "Explosion",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {}".format(constants.pkm_self, constants.inflict, constants.status_user_faints)],
'power': 250,
'accuracy': 100,
'pp': 5
}
extrasensory_dict = {
'name': "Extrasensory",
'type': constants.type_psychic,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 80,
'accuracy': 100,
'pp': 20
}
extreme_speed_dict = {
'name': "Extreme Speed",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'priority': 2,
'power': 80,
'accuracy': 100,
'pp': 5
}
#f,
facade_dict = {
'name': "Facade",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 70,
'accuracy': 100,
'pp': 20
}
fairy_lock_dict = {
'name': "Fiary Lock",
'type': constants.type_fairy,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 10
}
fairy_wind_dict = {
'name': "Fiary Wind",
'type': constants.type_fairy,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 40,
'accuracy': 100,
'pp': 30
}
fake_out_dict = {
'name': "Fake Out",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{}, {} {} on {} ".format(constants.first_turn_only, constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 40,
'accuracy': 100,
'pp': 10
}
fake_tears_dict = {
'name': "Fake Tears",
'type': constants.type_dark,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.special_defense, constants.by_2_stages)],
'power': None,
'accuracy': 100,
'pp': 20
}
false_swipe_dict = {
'name': "False Swipe",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 40,
'accuracy': 100,
'pp': 40
}
feather_dance_dict = {
'name': "Feather Dance",
'type': constants.type_flying,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.attack, constants.by_2_stages)],
'power': None,
'accuracy': 100,
'pp': 15
}
feint_dict = {
'name': "Feint",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 30,
'accuracy': 100,
'pp': 10
}
feint_attack_dict = {
'name': "Feint Attack",
'type': constants.type_dark,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 60,
'accuracy': 1000,
'pp': 20
}
fell_stinger_dict = {
'name': "Fell Stinger",
'type': constants.type_bug,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 30,
'accuracy': 100,
'pp': 25
}
fiery_dance_dict = {
'name': "Fiery Dance",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {} {}".format("50% chance to ", constants.increases, constants.pkm_self, constants.special_attack, constants.by_1_stage)],
'power': 80,
'accuracy': 100,
'pp': 10
}
final_gambit_dict = {
'name': "Final Gambit",
'type': constants.type_fighting,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {} ".format(constants.inflict, constants.pkm_foe, constants.set_amount_of_damage, constants.pkm_self, constants.health,),
"{} {} {}".format(constants.pkm_self, constants.inflict, constants.status_user_faints)],
'power': None,
'accuracy': 100,
'pp': 5
}
fire_blast_dict = {
'name': "Fire Blast",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'power': 110,
'accuracy': 85,
'pp': 5
}
fire_fang_dict = {
'name': "Fire Blast",
'type': constants.type_fire,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_burn, constants.pkm_foe),
"{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 65,
'accuracy': 95,
'pp': 15
}
fire_pledge_dict = {
'name': "Fire Pledge",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 80,
'accuracy': 100,
'pp': 10
}
fire_punch_dict = {
'name': "Fire Punch",
'type': constants.type_fire,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'power': 75,
'accuracy': 100,
'pp': 15
}
fire_spin_dict = {
'name': "Fire Spin",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {}".format(constants.inflict, constants.status_partially_trapped, constants.pkm_foe)],
'power': 35,
'accuracy': 85,
'pp': 15
}
fissure_dict = {
'name': "Fissure",
'type': constants.type_ground,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.one_hit_ko],
'power': None,
'accuracy': None,
'pp': 5
}
flail_dict = {
'name': "Flail",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 15
}
flame_burst_dict = {
'name': "Flame Burst",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 70,
'accuracy': 100,
'pp': 15
}
flame_charge_dict = {
'name': "Flame Charge",
'type': constants.type_fire,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.speed, constants.by_1_stages)],
'power': 50,
'accuracy': 100,
'pp': 20
}
flame_wheel_dict = {
'name': "Flame Wheel",
'type': constants.type_fire,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'power': 60,
'accuracy': 100,
'pp': 25
}
flamethrower_dict = {
'name': "Flamethrower",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'power': 90,
'accuracy': 100,
'pp': 15
}
flare_blitz_dict = {
'name': "Flare Blitz",
'type': constants.type_fire,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_burn, constants.pkm_foe), 
"{} {} {} {}".format(constants.pkm_self, constants.status_recoil_damage, constants.third, constants.damage_delt)],
'power': 120,
'accuracy': 100,
'pp': 15
}
flash_dict = {
'name': "Fash",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.accuracy, constants.by_1_stages)],
'power': None,
'accuracy': 100,
'pp': 20
}
flash_cannon_dict = {
'name': "Flash Cannon",
'type': constants.type_steel,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {} {}".format("10% chance", constants.reduces, constants.pkm_foe, constants.special_defense, constants.by_1_stages)],
'power': 80,
'accuracy': 100,
'pp': 10
}
flatter_dict = {
'name': "Flatter",
'type': constants.type_dark,
'category': constants.move_category_status,
'description': "",
'effects': ["{} to {} {} on {} ".format("Guranteed", constants.inflict, constants.status_confusion, constants.pkm_foe), 
"{} {} {} {}".format(constants.increases, constants.pkm_foe, constants.special_attack, constants.by_2_stages)],
'power': None,
'accuracy': 100,
'pp': 15
}
fling_dict = {
'name': "Fling",
'type': constants.type_dark,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 10
}
flower_shield_dict = {
'name': "Flower Shield",
'type': constants.type_fairy,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 10
}
fly_dict = {
'name': "Fly",
'type': constants.type_flying,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_flying),
"{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_semi_invulnerable)],
'power': 90,
'accuracy': 95,
'pp': 15
}
flying_press_dict = {
'name': "Flying Press",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 80,
'accuracy': 95,
'pp': 10
}
focus_blast_dict = {
'name': "Focus Blast",
'type': constants.type_fighting,
'category': constants.move_category_status,
'description': "",
'effects': ["10% chance", constants.reduces, constants.pkm_foe, constants.special_defense, constants.by_1_stages],
'power': 120,
'accuracy': 70,
'pp': 5
}
focus_energy_dict = {
'name': "Focus Energy",
'type': constants.type_normal,
'category': constants.move_category_status,
'power': None,
'accuracy': None,
'pp': 40,
'priority': 0,
'critical hit': 0,
'generation introducted': 1,
'effects': ["Increases Self Critical Hit Ratio 1 Stage".format(constants.increases , constants.pkm_self , constants.crit_ratio , constants.by_1_stage )],
'description': "Focuses power to raise critical-hit ratio.",
'machine': None,
}
focus_punch_dict = {
'name': "Focus Punch",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} on {} {}".format(constants.bestow, constants.status_focusing, constants.pkm_self],
'power': 150,
'accuracy': 100,
'pp': 10
}
follow_me_dict = {
'name': "Follow Me",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 20
}
force_palm_dict = {
'name': "Force Palm",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'power': 60,
'accuracy': 100,
'pp': 10
}
foresight_dict = {
'name': "Foresight",
'type': constants.type_normal,
'category': constants.move_category_status,'description': "",
'effects': ["{} {} {}".format(constants.remove_stat_changes, constants.pkm_foe, constants.evasion)],
'power': None,
'accuracy': None,
'pp': 40
}
forests_curse_dict = {
'name': "Forest's Curse",
'type': constants.type_grass,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 20
}
foul_play_dict = {
'name': "Foul Play",
'type': constants.type_dark,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 95,
'accuracy': 100,
'pp': 15
}
freeze_shock_dict = {
'name': "Freeze Shock",
'type': constants.type_ice,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {}".format(constants.bestow, constants.status_charging, constants.pkm_self),
"{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'power': 140,
'accuracy': 90,
'pp': 5
}
freeze_dry_dict = {
'name': "Freeze-Dry",
'type': constants.type_ice,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_freeze, constants.pkm_foe)],
'power': 70,
'accuracy': 100,
'pp': 20
}
frenzy_plant_dict = {
'name': "Frenzy Plant",
'type': constants.type_grass,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {}".format(constants.bestow, constants.status_recharge, constants.pkm_self)],
'power': 150,
'accuracy': 90,
'pp': 5
}
frost_breath_dict = {
'name': "Frost Breath",
'type': constants.type_ice,
'category': constants.move_category_special,
'description': "",
'effects': [constants.always_crit],
'power': 60,
'accuracy': 90,
'pp': 10
}
frustration_dict = {
'name': "Frustration",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 20
}
#'multi-hit':[2,5],
fury_attack_dict = {
'name': "Fury Attack",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,5],
'power': 15,
'accuracy': 85,
'pp': 20
}
fury_cutter_dict = {
'name': "Fury Cutter",
'type': constants.type_bug,
'category': constants.move_category_physical,
'description': "",
'effects': ["Power increases each turn."],
'power': 40,
'accuracy': 95,
'pp': 20
}
fury_swipes_dict = {
'name': "Fury Swipes",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,5],
'power': 18,
'accuracy': 80,
'pp': 15
}
fusion_bolt_dict = {
'name': "Fusion Bolt",
'type': constants.type_electric,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 100,
'accuracy': 100,
'pp': 5
}
fusion_flare_dict = {
'name': "Fusion Flare",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 100,
'accuracy': 100,
'pp': 5
}
future_sight_dict = {
'name': "Future Sight",
'type': constants.type_psychic,
'category': constants.move_category_special,
'description': "",
'effects': ["Damage occurs 2 turns later."],
'power': 120,
'accuracy': 100,
'pp': 10
}
#g,
gastro_acid_dict = {
'name': "Gastro Acid",
'type': constants.type_poison,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 10
}
gear_grind_dict = {
'name': "Gear Grind",
'type': constants.type_steel,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,2],
'power': 50,
'accuracy': 85,
'pp': 15
}
geomancy_dict = {
'name': "Geomancy",
'type': constants.type_fairy,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {}".format(constants.bestow, constants.status_charging, constants.pkm_self),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.speed, constants.by_2_stages),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.special_attack, constants.by_2_stages),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.special_defense, constants.by_2_stages),
],
'power': None,
'accuracy': None,
'pp': 10
}
giga_drain_dict = {
'name': "Giga Drain",
'type': constants.type_grass,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.recovers, constants.half, constants.damage_delt)],
'power': 75,
'accuracy': 100,
'pp': 10
}
giga_impact_dict = {
'name': "Giga Drain",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {}".format(constants.bestow, constants.status_recharge, constants.pkm_self)],
'power': 150,
'accuracy': 90,
'pp': 5
}
glaciate_dict = {
'name': "Glaciate",
'type': constants.type_ice,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe , constants.speed , constants.by_1_stage )],
'power': 65,
'accuracy': 95,
'pp': 10
}
glare_dict = {
'name': "Glare",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} ".format(constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'power': None,
'accuracy': 100,
'pp': 30
}
grass_knot_dict = {
'name': "Grass Knot",
'type': constants.type_grass,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 20
}
grass_pledge_dict = {
'name': "Grass Pledge",
'type': constants.type_grass,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 80,
'accuracy': 100,
'pp': 10
}
grass_whistle_dict = {
'name': "Grass Whistle",
'type': constants.type_grass,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_sleep, constants.pkm_foe)],
'power': None,
'accuracy': 55,
'pp': 15
}
grassy_terrain_dict = {
'name': "Grass Terrain",
'type': constants.type_grass,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 10
}
gravity_dict = {
'name': "Gravity",
'type': constants.type_psychic,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} Fly Bounce".format(constants.inflict, constants.pkm_foe, constants.disables_move)],
'power': None,
'accuracy': None,
'pp': 5
}
growl_dict = {'name': "Growl", 'type': constants.type_normal,
'category': constants.move_category_status,
'power': None, 'accuracy': 100, 'pp': 40,
'priority': 0, 'critical hit': 0,
'generation introducted': 1,
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe , constants.attack , constants.by_1_stage )],
'description': "Growls cutely to reduce the foe's Attack.",
'machine': None
}
growth_dict = {
'name': "Growth",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.attack , constants.by_1_stage ),
"{} {} {} {}".format(constants.increases , constants.pkm_self , constants.special_attack , constants.by_1_stage )],
'power': None,
'accuracy': None,
'pp': 40
}
grudge_dict = {
'name': "Grudge",
'type': constants.type_ghost,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 5
}
guard_split_dict = {
'name': "Guard Split",
'type': constants.type_psychic,
'category': constants.move_category_status,
'description': "",
'effects': ["Averages Defense and Special Defense with the target."],
'power': None,
'accuracy': None,
'pp': 10
}
guard_swap_dict = {
'name': "Guard Swap",
'type': constants.type_psychic,
'category': constants.move_category_status,
'description': "",
'effects': ["User and opponent swap Defense and Special Defense."],
'power': None,
'accuracy': None,
'pp': 10
}
guillotine_dict = {
'name': "Guillotine",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.one_hit_ko],
'power': None,
'accuracy': None,
'pp': 5
}
gunk_shot_dict = {
'name': "Gunk Shot",
'type': constants.type_poison,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("30 % chance", constants.inflict, constants.status_poison, constants.pkm_foe)],
'description': "",
'power': 120,
'accuracy': 80,
'pp': 5
}
gust_dict = {
'name': "Gust",
'type': constants.type_flying,
'category': constants.move_category_special,
'description': "",
'effects': ["Hits Pokémon using Fly/Bounce with double power."],
'power': 40,
'accuracy': 100,
'pp': 35
}
gyro_ball_dict = {
'name': "Gyro Ball",
'type': constants.type_steel,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': None,
'accuracy': 100,
'pp': 5
}
#h,
hail_dict = {
'name': "Hail",
'type': constants.type_ice,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 10
}
hammer_arm_dict = {
'name': "Hammer Arm",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe, constants.speed , constants.by_1_stage )],
'power': 100,
'accuracy': 90,
'pp': 10
}
happy_hour_dict = {
'name': "Happy Hour",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 30
}
harden_dict = {
'name': "Harden",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.defense, constants.by_1_stage )],
'power': None,
'accuracy': None,
'pp': 30
}
haze_dict = {
'name': "Haze",
'type': constants.type_ice,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {}".format(constants.remove_stat_changes, constants.all_stats, constants.pkm_self),
"{} {} {}".format(constants.remove_stat_changes, constants.all_stats, constants.pkm_all_other)],
'power': None,
'accuracy': None,
'pp': 30
}
head_charge_dict = {
'name': "Head Charge",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.status_recoil_damage, constants.quarter, constants.damage_delt)],
'power': 120,
'accuracy': 100,
'pp': 15
}
head_smash_dict = {
'name': "Head Smash",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.pkm_self,  constants.status_recoil_damage, constants.half, constants.damage_delt)],
'power': 150,
'accuracy': 80,
'pp': 5
}
headbutt_dict = {
'name': "Headbutt",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 70,
'accuracy': 100,
'pp': 15
}
heal_bell_dict = {
'name': "Heal Bell",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 5
}
heal_block_dict = {
'name': "Heal Block",
'type': constants.type_psychic,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} ".format( constants.inflict, constants.status_heal_block, constants.pkm_foe)],
'power': None,
'accuracy': None,
'pp': 15
}
heal_order_dict = {
'name': "Heal Order",
'type': constants.type_bug,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_self)],
'power': None,
'accuracy': None,
'pp': 10
}
heal_pulse_dict = {
'name': "Heal Pulse",
'type': constants.type_psychic,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_foe)],
'power': None,
'accuracy': None,
'pp': 10
}
healing_wish_dict = {
'name': "Healing Wish",
'type': constants.type_psychic,
'category': constants.move_category_status,
'description': "",
'effects': ["Next Pokemon is fully healed."),
"{} {} {}".format(constants.pkm_self, constants.inflict, constants.status_user_faints)],
'power': None,
'accuracy': None,
'pp': 10
}
heart_stamp_dict = {
'name': "Heart Stamp",
'type': constants.type_psychic,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 60,
'accuracy': 100,
'pp': 25
}
heart_swap_dict = {
'name': "Heart Swap",
'type': constants.type_psychic,
'category': constants.move_category_status,
'description': "",
'effects': ["Stat changes are swapped with the opponent."],
'power': None,
'accuracy': None,
'pp': 10
}
heat_crash_dict = {
'name': "Heart Swap",
'type': constants.type_fire,
'category': constants.move_category_physical,
'description': "",
'effects': ["The heavier the user, the stronger the attack."],
'power': None,
'accuracy': 100,
'pp': 10
}
heat_wave_dict = {
'name': "Heat Wave",
'type': constants.type_fire,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'power': 95,
'accuracy': 90,
'pp': 10
}
heavy_slam_dict = {
'name': "Heavy Slam",
'type': constants.type_steel,
'category': constants.move_category_physical,
'description': "",
'effects': ["The heavier the user, the stronger the attack."],
'power': None,
'accuracy': 100,
'pp': 10
}
helping_hand_dict = {
'name': "Helping Hand",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["In Double Battles, boosts the power of the partner's move."],
'power': None,
'accuracy': None,
'pp': 20
}
hex_dict = {
'name': "Hex",
'type': constants.type_ghost,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 65,
'accuracy': 100,
'pp': 10
}
hidden_power_dict = {
'name': "Hidden Power",
'type': constants.type_normal,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 60,
'accuracy': 100,
'pp': 15
}
high_jump_kick_dict = {
'name': "High Jump Kick",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 60,
'accuracy': 100,
'pp': 15
}
hold_back_dict = {
'name': "Hold Back",
'type': constants.type_normal,
'category': constants.move_category_physical,'description': "",
'effects': [],
'power': 40,
'accuracy': 100,
'pp': 40
}
hold_hands_dict = {
'name': "Hold Hands",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': [],
'power': None,
'accuracy': None,
'pp': 40
}
hone_claws_dict = {
'name': "Hold Hands",
'type': constants.type_dark,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.attack , constants.by_1_stage ),
"{} {} {} {}".format(constants.increases , constants.pkm_self , constants.accuracy , constants.by_1_stage )],
'power': None,
'accuracy': None,
'pp': 15
}
horn_attack_dict = {
'name': "Horn Attack",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 65,
'accuracy': 100,
'pp': 25
}
horn_drill_dict = {
'name': "Horn Drill",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': [constants.one_hit_ko],
'power': None,
'accuracy': None,
'pp': 5
}
horn_leech_dict = {
'name': "Horn Leech",
'type': constants.type_bug,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.recovers, constants.half, constants.damage_delt)],
'power': 75,
'accuracy': 100,
'pp': 10
}
howl_dict = {
'name': "Howl",
'type': constants.type_normal,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.attack , constants.by_1_stage)],
'power': None,
'accuracy': None,
'pp': 40
}
hurricane_dict = {
'name': "Hurricane",
'type': constants.type_flying,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'power': 110,
'accuracy': 70,
'pp': 10
}
hydro_cannon_dict = {
'name': "Hydro Cannon",
'type': constants.type_water,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {}".format(constants.bestow, constants.status_recharge, constants.pkm_self)],
'power': 150,
'accuracy': 90,
'pp': 5
}
hydro_pump_dict = {
'name': "Hydro Pump",
'type': constants.type_water,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 110,
'accuracy': 80,
'pp': 5
}
hyper_beam_dict = {
'name': "Hyper Beam",
'type': constants.type_normal,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {}".format(constants.bestow, constants.status_recharge, constants.pkm_self)],
'power': 150,
'accuracy': 90,
'pp': 5
}
hyper_fang_dict = {
'name': "Hyper Fang",
'type': constants.type_normal,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 80,
'accuracy': 90,
'pp': 15
}
hyper_voice_dict = {
'name': "Hyper Voice",
'type': constants.type_normal,
'category': constants.move_category_special,
'description': "",
'effects': [],
'power': 90,
'accuracy': 100,
'pp': 10
}
hyperspace_fury_dict = {
'name': "Hyperspace Fury",
'type': constants.type_dark,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.defense, constants.by_1_stage),
"Can strike through Protect/Detect."],
'power': 100,
'accuracy': 1000,
'pp': 5
}
hyperspace_hole_dict = {
'name': "Hyperspace Hole",
'type': constants.type_psychic,
'category': constants.move_category_special,
'description': "",
'effects': ["Can strike through Protect/Detect."],
'power': 80,
'accuracy': 1000,
'pp': 5
}
hypnosis_dict = {
'name': "Hyperspace Hole",
'type': constants.type_psychic,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {} ".format(constants.inflict, constants.status_sleep, constants.pkm_foe)],
'power': None,
'accuracy': 60,
'pp': 20
}
#i,
ice_ball_dict = {
'name': "Ice Ball",
'type': constants.type_ice,
'category': constants.move_category_physical,
'description': "",
'effects': ["Doubles in power each turn for 5 turns."],
'power': 30,
'accuracy': 90,
'pp': 20
}
ice_beam_dict = {
'name': "Ice Beam",
'type': constants.type_ice,
'category': constants.move_category_special,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_freeze, constants.pkm_foe)],
'power': 90,
'accuracy': 100,
'pp': 10
}
ice_burn_dict = {
'name': "Ice Burn",
'type': constants.type_ice,
'category': constants.move_category_special,
'description': "",
'effects': ["{} {} {}".format(constants.inflict, constants.status_charging, constants.pkm_self),
"{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'power': 140,
'accuracy': 90,
'pp': 5
}
ice_fang_dict = {
'name': "Ice Fang",
'type': constants.type_ice,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_freeze, constants.pkm_foe),
"{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 65,
'accuracy': 95,
'pp': 15
}
ice_punch_dict = {
'name': "Ice Punch",
'type': constants.type_ice,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_freeze, constants.pkm_foe)],
'power': 75,
'accuracy': 100,
'pp': 15
}
ice_shard_dict = {
'name': "Ice Shard",
'type': constants.type_ice,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'power': 40,
'accuracy': 100,
'priority': 1,
'pp': 30
}
icicle_crash_dict = {
'name': "Icicle Crash",
'type': constants.type_ice,
'category': constants.move_category_physical,
'description': "",
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'power': 85,
'accuracy': 90,
'pp': 10
}
#'multi-hit':[2,5],
icicle_spear_dict = {
'name': "Icicle Spear",
'type': constants.type_ice,
'category': constants.move_category_physical,
'description': "",
'effects': [],
'multi-hit':[2,5],
'power': 25,
'accuracy': 100,
'pp': 30
}
icy_wind_dict = {
'name': "Icy Wind",
'type': constants.type_ice,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("Guranteed to ", constants.reduces , constants.pkm_foe , constants.speed , constants.by_1_stage )],
'description': "",
'power': 55,
'accuracy': 95,
'pp': 15
}
imprison_dict = {
'name': "Imprison",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.inflict, constants.pkm_foe, constants.disables_move)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
incinerate_dict = {
'name': "Incinerate",
'type': constants.type_fire,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 15
}
inferno_dict = {
'name': "Inferno",
'type': constants.type_fire,
'category': constants.move_category_special,
'effects': ["{} {} {}".format(constants.inflict, constants.status_burn, constants.pkm_foe)],
'description': "",
'power': 100,
'accuracy': 50,
'pp': 5
}
infestation_dict = {
'name': "Infestation",
'type': constants.type_bug,
'category': constants.move_category_special,
'effects': ["{} {} {}".format(constants.inflict, constants.status_partially_trapped, constants.pkm_foe)],
'description': "",
'power': 20,
'accuracy': 100,
'pp': 20
}
ingrain_dict = {
'name': "Ingain",
'type': constants.type_grass,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.bestow, constants.status_rooted, constants.pkm_self),
"{} {} {}".format(constants.inflict, constants.status_trapped, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
ion_deluge_dict = {
'name': "Ion Deluge",
'type': constants.type_electric,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 25
}
iron_defense_dict = {
'name': "Iron Defense",
'type': constants.type_steel,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.defense, constants.by_2_stages)],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
iron_head_dict = {
'name': "Iron Head",
'type': constants.type_steel,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 15
}
iron_tail_dict = {
'name': "Iron Tail",
'type': constants.type_steel,
'category': constants.move_category_physical,
'effects': ["{} {} {} {} {}".format("10% chance", constants.reduces, constants.pkm_foe, constants.defense, constants.by_1_stages)],
'description': "",
'power': 100,
'accuracy': 75,
'pp': 15
}
#j,
judgement_dict = {
'name': "Judgement",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 100,
'accuracy': 100,
'pp': 10
}
jump_kick_dict = {
'name': "Jump Kick",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 15
}
#k,
karate_chop_dict = {
'name': "Karate Chop",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [constants.high_crit_ratio],
'description': "",
'power': 50,
'accuracy': 100,
'pp': 25
}
kinesis_dict = {
'name': "Kinesis",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': ["{} {} {} {} {}".format("Guarenteed to ", constants.reduces , constants.pkm_foe , constants.accuracy , constants.by_1_stage )],
'description': "",
'power': None,
'accuracy': 80,
'pp': 15
}
kings_shield_dict = {
'name': "King's Shield",
'type': constants.type_steel,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
knock_off_dict = {
'name': "Knock Off",
'type': constants.type_dark,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 25
}
#l,
lands_wrath_dict = {
'name': "Land's Wrath",
'type': constants.type_ground,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 10
}
last_resort_dict = {
'name': "Last Resort",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 140,
'accuracy': 100,
'pp': 5
}
lava_plume_dict = {
'name': "Lava Plume",
'type': constants.type_fire,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 15
}
leaf_blade_dict = {
'name': "Leaf Blade",
'type': constants.type_grass,
'category': constants.move_category_physical,
'effects': [constants.high_crit_ratio],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 15
}
leaf_storm_dict = {
'name': "Leaf Storm",
'type': constants.type_grass,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("Guranteed to ", constants.reduces, constants.pkm_foe, constants.special_attack, constants.by_2_stage)],
'description': "",
'power': 130,
'accuracy': 90,
'pp': 5
}
leaf_tornado_dict = {
'name': "Leaf Tornado",
'type': constants.type_grass,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("30% chance to", constants.reduces, constants.pkm_foe, constants.accuracy, constants.by_1_stage)],
'description': "",
'power': 65,
'accuracy': 90,
'pp': 10
}
leech_life_dict = {
'name': "Leech Life",
'type': constants.type_bug,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.recovers, constants.half, constants.damage_delt)],
'description': "",
'power': 20,
'accuracy': 100,
'pp': 15
}
leech_seed_dict = {
'name': "Leech Seed",
'type': constants.type_grass,
'category': constants.move_category_status,
'power': None,
'accuracy': 90,
'pp': 10,
'priority': 0,
'critical hit': 0,
'generation introducted': 1,
'effects': ["Inflicts Leech Seed on Foe"],
'description': "Leech Seed drains 1/8 of the targets HP per turn, healing the active Pokemon.  Doesn't work on Grass-type Pokemon.",
'machine': None,
}
leer_dict = {
'name': "Leer",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {} {}".format("Guranteed to ", constants.reduces , constants.pkm_foe , constants.defense , constants.by_1_stage )],
'description': "",
'power': None,
'accuracy': 100,
'pp': 30
}
lick_dict = {
'name': "Lick",
'type': constants.type_ghost,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': 30,
'accuracy': 100,
'pp': 30
}
light_of_ruin_dict = {
'name': "Light of Ruin",
'type': constants.type_fairy,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.status_recoil_damage, constants.half, constants.damage_delt)],
'description': "",
'power': 140,
'accuracy': 90,
'pp': 5
}
light_screen_dict = {
'name': "Light Screen",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {} ".format(constants.bestow, constants.status_light_screen, constants.pkm_self),
"{} {} {} ".format(constants.bestow, constants.status_light_screen, constants.pkm_ally)],
'description': "",
'power': None,
'accuracy': None,
'pp': 30
}
lock_on_dict = {
'name': "Lock On",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} ".format(constants.bestow, constants.status_taking_aim, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
lovely_kiss_dict = {
'name': "Lovely Kiss",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} ".format(constants.inflict, constants.status_sleep, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 75,
'pp': 10
}
low_kick_dict = {
'name': "Low Kick",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
low_sweep_dict = {
'name': "Low Sweep",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': ["{} {} {} {} {}".format("Guranteed to ", constants.reduces , constants.pkm_foe , constants.speed , constants.by_1_stage )],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 20
}
lucky_chant_dict = {
'name': "Lucky Chant",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 30
}
lunar_dance_dict = {
'name': "Lunar Dance",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': [Next Pokemon is fully healed."),
"{} {} {}".format(constants.pkm_self, constants.inflict, constants.status_user_faints)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
luster_purge_dict = {
'name': "Luster Purge",
'type': constants.type_psychic,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("50% chance to ", constants.reduces , constants.pkm_foe , constants.speed , constants.by_1_stage )],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 5
}
#m,
mach_punch_dict = {
'name': "Mach Punch",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 40,
'accuracy': 100,
'priority': 1,
'pp': 30
}
magic_coat_dict = {
'name': "Magic Coat",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_magic_coat)],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
magic_room_dict = {
'name': "Magic Room",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
magical_leaf_dict = {
'name': "Magic Room",
'type': constants.type_grass,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 60,
'accuracy': 1000,
'pp': 20
}
magma_storm_dict = {
'name': "Magma Storm",
'type': constants.type_fire,
'category': constants.move_category_special,
'effects': ["{} {} {}".format(constants.inflict, constants.status_partially_trapped, constants.pkm_foe)],
'description': "",
'power': 120,
'accuracy': 75,
'pp': 5
}
magnet_bomb_dict = {
'name': "Magnet Bomb",
'type': constants.type_steel,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 60,
'accuracy': 1000,
'pp': 20
}
magnet_rise_dict = {
'name': "Magnet Rise",
'type': constants.type_electric,
'category': constants.move_category_status,
'effects': ["User becomes immune to Ground-type moves for 5 turns."],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
magnetic_flux_dict = {
'name': "Magnetic Flux",
'type': constants.type_electric,
'category': constants.move_category_status,
'power': None,
'accuracy': None,
'pp': 20
}
magnitude_dict = {
'name': "Magnitude",
'type': constants.type_ground,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 30
}
mat_block_dict = {
'name': "Mat Block",
'type': constants.type_fighting,
'category': constants.move_category_status,
'effects': ["Protects teammates from damaging moves."],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
me_first_dict = {
'name': "Me First",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
mean_look_dict = {
'name': "Mean Look",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_trapped, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
meditate_dict = {
'name': "Meditate",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {} {} ".format(constants.pkm_self, constants.increases, constants.attack, constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
mega_drain_dict = {
'name': "Mega Drain",
'type': constants.type_grass,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.recovers, constants.half, constants.damage_delt)],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 15
}
mega_kick_dict = {
'name': "Mega Kick",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 120,
'accuracy': 75,
'pp': 5
}
mega_punch_dict = {
'name': "Mega Punch",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 80,
'accuracy': 85,
'pp': 20
}
megahorn_dict = {
'name': "Megahorn",
'type': constants.type_bug,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 120,
'accuracy': 85,
'pp': 10
}
memento_dict = {
'name': "Memento",
'type': constants.type_dark,
'category': constants.move_category_status,
'effects': ["{} {} {} {} ".format(constants.pkm_foe, constants.reduces, constants.attack, constants.by_2_stage),
"{} {} {} {} ".format(constants.pkm_foe, constants.reduces, constants.special_attack, constants.by_2_stage)
constants.status_user_faints],
'description': "",
'power': None,
'accuracy': 100,
'pp': 10
}
metal_burst_dict = {
'name': "Metal Burst",
'type': constants.type_steel,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 10
}
metal_claw_dict = {
'name': "Metal Claw",
'type': constants.type_steel,
'category': constants.move_category_physical,
'effects': ["{} {} {} {} {}".format("10% chance to ", constants.increases , constants.pkm_self , constants.attack , constants.by_1_stage )],
'description': "",
'power': 50,
'accuracy': 95,
'pp': 35
}
metal_sound_dict = {
'name': "Metal Sound",
'type': constants.type_steel,
'category': constants.move_category_status,
'effects': ["{} {} {} {} {}".format("Guranteed to ", constants.reduces, constants.pkm_foe, constants.special_defense, constants.by_2_stages)],
'description': "",
'power': None,
'accuracy': 85,
'pp': 40
}
meteor_mash_dict = {
'name': "Meteor Mash",
'type': constants.type_steel,
'category': constants.move_category_status,
'effects': ["{} {} {} {} {}".format("20 % chance to ", constants.increases , constants.pkm_self , constants.attack , constants.by_1_stage )],
'description': "",
'power': 90,
'accuracy': 90,
'pp': 10
}
metronome_dict = {
'name': "Metronome",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["User performs any move in the game at random."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
milk_drink_dict = {
'name': "Milk Drink",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
mimic_dict = {
'name': "Mimic",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
mind_reader_dict = {
'name': "Mind Reader",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
minimize_dict = {
'name': "Minimize",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.evasion, constants.by_2_stages)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
miracle_eye_dict = {
'name': "Miracle Eye",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.remove_stat_changes, constants.pkm_foe, constants.evasion)],
'description': "",
'power': None,
'accuracy': None,
'pp': 40
}
mirror_coat_dict = {
'name': "Mirror Coat",
'type': constants.type_psychic,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
mirror_move_dict = {
'name': "Mirror Move",
'type': constants.type_flying,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
mirror_shot_dict = {
'name': "Mirror Shot",
'type': constants.type_steel,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe , constants.accuracy , constants.by_1_stage )],
'description': "",
'power': 65,
'accuracy': 85,
'pp': 10
}
mist_dict = {
'name': "Mist",
'type': constants.type_ice,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.inflict, constants.pkm_foe, constants.status_mist)],
'description': "",
'power': None,
'accuracy': None,
'pp': 30
}
mist_ball_dict = {
'name': "Mist Ball",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe , constants.special_attack , constants.by_1_stage )],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 5
}
misty_terrain_dict = {
'name': "Misty Terrain",
'type': constants.type_fairy,
'category': constants.move_category_status,
'power': None,
'accuracy': None,
'pp': 10
}
moonblast_dict = {
'name': "Moonblast",
'type': constants.type_fairy,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe , constants.special_attack , constants.by_1_stage )],
'description': "",
'power': 95,
'accuracy': 100,
'pp': 15
}
moonlight_dict = {
'name': "Moonblast",
'type': constants.type_fairy,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
morning_sun_dict = {
'name': "Morning Sun",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
mud_bomb_dict = {
'name': "Mud Bomb",
'type': constants.type_ground,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe , constants.accuracy , constants.by_1_stage )],
'description': "",
'power': 65,
'accuracy': 85,
'pp': 10
}
mud_shot_dict = {
'name': "Mud Shot",
'type': constants.type_ground,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe , constants.speed , constants.by_1_stage )],
'description': "",
'power': 55,
'accuracy': 95,
'pp': 15
}
mud_sport_dict = {
'name': "Mud Sport",
'type': constants.type_ground,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
mud_slap_dict = {
'name': "Mud-slap",
'type': constants.type_ground,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.reduces , constants.pkm_foe , constants.accuracy , constants.by_1_stage )],
'description': "",
'power': 20,
'accuracy': 100,
'pp': 10
}
muddy_water_dict = {
'name': "Muddy Water",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("30% chance", constants.reduces, constants.pkm_foe, constants.accuracy, constants.by_1_stage)],
'description': "",
'power': 90,
'accuracy': 85,
'pp': 10
}
mystical_fire_dict = {
'name': "Mystical Fire",
'type': constants.type_fire,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("100% chance", constants.reduces, constants.pkm_foe, constants.special_attack, constants.by_1_stage)],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 10
}
#n,
nasty_plot_dict = {
'name': "Nasty Plot",
'type': constants.type_dark,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.special_attack, constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
natural_gift_dict = {
'name': "Natural Gift",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
nature_power_dict = {
'name': "Nature Power",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
needle_arm_dict = {
'name': "Needle Arm",
'type': constants.type_grass,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 15
}
night_daze_dict = {
'name': "Night Daze",
'type': constants.type_ghost,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("40% chance", constants.increases, constants.pkm_self, constants.accuracy, constants.by_1_stage)],
'description': "",
'power': 85,
'accuracy': 95,
'pp': 10
}
night_shade_dict = {
'name': "Night Shade",
'type': constants.type_ghost,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
night_slash_dict = {
'name': "Night Slash",
'type': constants.type_dark,
'category': constants.move_category_physical,
'effects': [constants.high_crit_ratio],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 15
}
nightmare_dict = {
'name': "Nightmare",
'type': constants.type_ghost,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("On Sleeping Pokemon", constants.inflict, constants.status_nightmare, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
noble_roar_dict = {
'name': "Noble Roar",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.attack, constants.by_1_stage),
"{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.special_attack, constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 30
}
nuzzle_dict = {
'name': "Nuzzle",
'type': constants.type_electric,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("Guranteed", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': 20,
'accuracy': 100,
'pp': 20
}
#o,
oblivion_wing_dict = {
'name': "Oblivion Wing",
'type': constants.type_flying,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.recovers, constants.three_quarters, constants.health, constants.pkm_self)],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 10
}
octazooka_dict = {
'name': "Octazooka",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("40% chance", constants.reduces, constants.pkm_self, constants.accuracy, constants.by_1_stage)],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 10
}
odor_sleuth_dict = {
'name': "Odor Sleuth",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.remove_stat_changes, constants.pkm_foe, constants.evasion)],
'description': "",
'power': None,
'accuracy': None,
'pp': 40
}
ominous_wind_dict = {
'name': "Ominous Wind",
'type': constants.type_ghost,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("10% chance to ", constants.increases, constants.pkm_self, constants.all_stats, constants.by_1_stage)],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 5
}
origin_pulse_dict = {
'name': "Origin Pulse",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 110,
'accuracy': 85,
'pp': 10
}
outrage_dict = {
'name': "Outrage",
'type': constants.type_dragon,
'category': constants.move_category_physical,
'effects': [constants.repeat_then_become_confused],
'description': "",
'power': 110,
'accuracy': 85,
'pp': 10
}
overheat_dict = {
'name': "Overheat",
'type': constants.type_fire,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_self, constants.special_attack, constants.by_2_stage)],
'description': "",
'power': 130,
'accuracy': 90,
'pp': 5
}
#p,
pain_split_dict = {
'name': "Pain Split",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
parabolic_charge_dict = {
'name': "Parabolic Charge",
'type': constants.type_electric,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.recovers, constants.half, constants.damage_delt)],
'description': "",
'power': 50,
'accuracy': 100,
'pp': 20
}
parting_shot_dict = {
'name': "Parting Shot",
'type': constants.type_dark,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.attack, constants.by_1_stage),
"{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.special_attack, constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
pay_day_dict = {
'name': "Pay Day",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 20
}
payback_dict = {
'name': "Payback",
'type': constants.type_dark,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 50,
'accuracy': 100,
'pp': 10
}
peck_dict = {
'name': "Peck",
'type': constants.type_flying,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 35,
'accuracy': 100,
'pp': 35
}
perish_song_dict = {
'name': "Perish Song",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constats.pkm_self, constats.inflict, constats.status_perish_song),
"{} {} {}".format(constats.pkm_foe, constats.inflict, constats.status_perish_song)],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
petal_blizzard_dict = {
'name': "Petal Blizzard",
'type': constants.type_grass,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 15
}
petal_dance_dict = {
'name': "Petal Dance",
'type': constants.type_grass,
'category': constants.move_category_special,
'effects': [constants.repeat_then_become_confused],
'description': "",
'power': 120,
'accuracy': 100,
'pp': 10
}
phantom_force_dict = {
'name': "Phantom Force",
'type': constants.type_ghost,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 10
}
pin_missile_dict = {
'name': "Pin Missile",
'type': constants.type_bug,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'multi-hit':[2,5],
'power': 25,
'accuracy': 95,
'pp': 20
}
play_nice_dict = {
'name': "Play Nice",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.pkm_foe, constants.reduce, constants.attack, constants.by_1_stage), 
"Always hits."],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
play_rough_dict = {
'name': "Play Rough",
'type': constants.type_fairy,
'category': constants.move_category_physical,
'effects': ["{} {} {} {} {}".format("10% chance", constants.pkm_foe, constants.reduce, constants.attack, constants.by_1_stage)],
'description': "",
'power': 90,
'accuracy': 90,
'pp': 10
}
pluck_dict = {
'name': "Pluck",
'type': constants.type_flying,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 20
}
poison_fang_dict = {
'name': "Poison Fang",
'type': constants.type_poison,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("50 % chance", constants.inflict, constants.status_badly_poison, constants.pkm_foe)],
'description': "",
'power': 50,
'accuracy': 100,
'pp': 15
}
poison_gas_dict = {
'name': "Poison Gas",
'type': constants.type_poison,
'category': constants.move_category_status,
'effects': ["{} to {} {} on {} ".format("guaranteed", constants.inflict, constants.status_poison, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 90,
'pp': 40
}
poison_jab_dict = {
'name': "Poison Jab",
'type': constants.type_poison,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_poison, constants.pkm_foe)],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 20
}
poison_powder_dict = {
'name': "Poison Powder",
'type': constants.type_poison,
'category': constants.move_category_status,
'effects': ["{} to {} {} on {} ".format("guaranteed", constants.inflict, constants.status_poison, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 75,
'pp': 35
}
poison_sting_dict = {
'name': "Poison Sting",
'type': constants.type_poison,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_poison, constants.pkm_foe)],
'description': "",
'power': 15,
'accuracy': 100,
'pp': 35
}
poison_tail_dict = {
'name': "Poison Tail",
'type': constants.type_poison,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("10 % chance", constants.inflict, constants.status_poison, constants.pkm_foe),constants.high_crit_ratio],
'description': "",
'power': 50,
'accuracy': 100,
'pp': 25
}
pound_dict = {
'name': "Pound",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 35
}
powder_dict = {
'name': "Powder",
'type': constants.type_bug,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
powder_snow_dict = {
'name': "Powder Snow",
'type': constants.type_ice,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {}".format("10% chance", constants.inflict, constants.status_freeze, constants.pkm_foe)],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 25
}
power_gem_dict = {
'name': "Power Gem",
'type': constants.type_rock,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 20
}
power_split_dict = {
'name': "Power Split",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["Averages Attack and Special Attack with the target."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
power_swap_dict = {
'name': "Power Swap",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["User and opponent swap Attack and Special Attack."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
power_trick_dict = {
'name': "Power Trick",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["User's own Attack and Defense switch."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
power_whip_dict = {
'name': "Power Whip",
'type': constants.type_grass,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 120,
'accuracy': 85,
'pp': 10
}
power_up_punch_dict = {
'name': "Power-Up Punch",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.attack, constants.by_1_stage)],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 10
}
precipice_blades_dict = {
'name': "Precipice Blades",
'type': constants.type_ground,
'category': constants.move_category_physical,
'effects': ["Hits all adjacent opponents."],
'description': "",
'power': 120,
'accuracy': 85,
'pp': 10
}
present_dict = {
'name': "Present",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': None,
'accuracy': 90,
'pp': 15
}
protect_dict = {
'name': "Protect",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_protected)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
psybeam_dict = {
'name': "Psybeam",
'type': constants.type_psychic,
'category': constants.move_category_special,'effects': [],
'description': "",
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'power': 65,
'accuracy': 100,
'pp': 20
}
psych_up_dict = {
'name': "Psych Up",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["Copies the opponent's stat changes."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
psychic_dict = {
'name': "Psychic",
'type': constants.type_psychic,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("10% chance", constants.pkm_foe, constants.reduces, constants.special_attack, constants.by_1_stage)],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 10
}
psycho_boost_dict = {
'name': "Psycho Boost",
'type': constants.type_psychic,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.reduces, constants.special_attack, constants.by_2_stage)],
'description': "",
'power': 140,
'accuracy': 90,
'pp': 5
}
psycho_cut_dict = {
'name': "Psycho Cut",
'type': constants.type_psychic,
'category': constants.move_category_physical,
'effects': [constants.high_crit_ratio],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 20
}
psycho_shift_dict = {
'name': "Psycho Shift",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["Gives the opponent the user's status condition, if it hits."],
'description': "",
'power': None,
'accuracy': 90,
'pp': 10
}
psyshock_dict = {
'name': "Psyshock",
'type': constants.type_psychic,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 10
}
psystrike_dict = {
'name': "Psystrike",
'type': constants.type_psychic,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 100,
'accuracy': 100,
'pp': 10
}
psywave_dict = {
'name': "Psywave",
'type': constants.type_psychic,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': None,
'accuracy': 80,
'pp': 15
}
punishment_dict = {
'name': "Punishment",
'type': constants.type_dark,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 5
}
pursuit_dict = {
'name': "Pursuit",
'type': constants.type_dark,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 40,
'accuracy': 100,
'priority': 0,
'pp': 20
}
#q,
quash_dict = {
'name': "Quash",
'type': constants.type_dark,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
quick_attack_dict = {
'name': "Quick Attack",
'type': constants.type_normal,
'category': constants.move_category_physical,
'power': 40,
'accuracy': 100,
'pp': 30,
'priority': 1,
'critical hit': 0,
'generation introducted': 1,
'effects': [],
'description': "",
'machine': None,
}
quick_guard_dict = {
'name': "Quick Gaurd",
'type': constants.type_fighting,
'category': constants.move_category_status,
'effects': [],
'description': "",
'priority': 3,
'power': None,
'accuracy': 100,
'pp': 15
}
quiver_dance_dict = {
'name': "Quiver Dance",
'type': constants.type_dark,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.increases, constants.attack, constants.by_1_stage),
"{} {} {} {}".format(constants.pkm_self, constants.increases, constants.special_attack, constants.by_1_stage)
"{} {} {} {}".format(constants.pkm_self, constants.increases, constants.speed, constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
#r,
rage_dict = {
'name': "Rage",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_rage)],
'description': "",
'power': 20,
'accuracy': 100,
'pp': 20
}
rage_powder_dict = {
'name': "Rage Powder",
'type': constants.type_bug,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
rain_dance_dict = {
'name': "Rain Dance",
'type': constants.type_water,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
rapid_spin_dict = {
'name': "Rapid Spin",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': ["{} {} {}".format(constants.pkm_self, constants.remove, constants.trap_effects)],
'description': "",
'power': 20,
'accuracy': 100,
'pp': 40
}
razor_leaf_dict = {
'name': "Razor Leaf",
'type': constants.type_grass,
'category': constants.move_category_physical,
'effects': [constants.high_crit_ratio],
'description': "",
'power': 55,
'accuracy': 95,
'pp': 25
}
razor_shell_dict = {
'name': "Razor Shell",
'type': constants.type_water,
'category': constants.move_category_physical,
'effects': ["{} {} {} {} {}".format("50% chance", constants.pkm_foe, constants.reduces, constants.defense, constants.by_1_stage)],
'description': "",
'power': 75,
'accuracy': 95,
'pp': 10
}
razor_wind_dict = {
'name': "Razor Wind",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': ["{} {} {}".format(constants.inflict, constants.status_charging, constants.pkm_self),
constants.high_crit_ratio],
'description': "",
'power': 80,
'accuracy': 10,
'pp': 10
}
recover_dict = {
'name': "Recover",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
recycle_dict = {
'name': "Recycle",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
reflect_dict = {
'name': "Reflect",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {} ".format(constants.bestow, constants.status_reflect, constants.pkm_self),
"{} {} {} ".format(constants.bestow, constants.status_reflect, constants.pkm_ally)],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
reflect_type_dict = {
'name': "Reflect Type",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
refresh_dict = {
'name': "Refresh",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.remove, constants.status_all_negative, constants.status_infliction, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
relic_song_dict = {
'name': "Relic Song",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_sleep, constants.pkm_foe)],
'description': "",
'power': 75,
'accuracy': 100,
'pp': 10
}
rest_dict = {
'name': "Rest",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_sleep, constants.pkm_self),
"{} {} {} {}".format(constants.recovers, constants.full, constants.health, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
retaliate_dict = {
'name': "Retaliate",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 5
}
return_dict = {
'name': "Return",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
revenge_dict = {
'name': "Revenge",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': ["Power increases if user was hit first."],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 10
}
reversal_dict = {
'name': "Reversal",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
roar_dict = {
'name': "Roar",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [constants.switches_opponent],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
roar_of_time_dict = {
'name': "Roar of Time",
'type': constants.type_dragon,
'category': constants.move_category_special,
'effects': ["{} {} {}".format(constants.bestow, constants.status_recharge, constants.pkm_self)],
'description': "",
'power': 150,
'accuracy': 90,
'pp': 5
}
rock_blast_dict = {
'name': "Rock Blast",
'type': constants.type_rock,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'multi-hit':[2,5],
'power': 25,
'accuracy': 90,
'pp': 10
}
rock_climb_dict = {
'name': "Rock Blimb",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("20% chance", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'description': "",
'power': 90,
'accuracy': 85,
'pp': 20
}
rock_polish_dict = {
'name': "Rock Polish",
'type': constants.type_rock,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.speed, constants.by_2_stage)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
rock_slide_dict = {
'name': "Rock Slide",
'type': constants.type_rock,
'category': constants.move_category_physical,
'effects': ["{} {} {} {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 75,
'accuracy': 90,
'pp': 20
}
rock_smash_dict = {
'name': "Rock Smash",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': ["{} {} {} {} {}".format("30% chance", constants.pkm_foe, constants.reduces, constants.defense, constants.by_1_stage)],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 15
}
rock_throw_dict = {
'name': "Rock Throw",
'type': constants.type_rock,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 50,
'accuracy': 90,
'pp': 15
}
rock_tomb_dict = {
'name': "Rock Tomb",
'type': constants.type_rock,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.speed, constants.by_1_stage)],
'description': "",
'power': 60,
'accuracy': 95,
'pp': 15
}
rock_wrecker_dict = {
'name': "Rock Wrecker",
'type': constants.type_rock,
'category': constants.move_category_physical,
'effects': ["{} {} {}".format(constants.bestow, constants.status_recharge, constants.pkm_self)],
'description': "",
'power': 150,
'accuracy': 90,
'pp': 5
}
role_play_dict = {
'name': "Role Play",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["User copies the opponent's Ability."],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
rolling_kick_dict = {
'name': "Rolling Kick",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 60,
'accuracy': 85,
'pp': 15
}
rollout_dict = {
'name': "Rollout",
'type': constants.type_rock,
'category': constants.move_category_physical,
'effects': ["Doubles in power each turn for 5 turns."],
'description': "",
'power': 30,
'accuracy': 90,
'pp': 20
}
roost_dict = {
'name': "Roost",
'type': constants.type_flying,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
rototiller_dict = {
'name': "Rototiller",
'type': constants.type_ground,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
round_dict = {
'name': "Round",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': ["Power increases if teammates use it in the same turn."],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 15
}
#s
sacred_fire_dict = {
'name': "Sacred Fire",
'type': constants.type_fire,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("50% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'description': "",
'power': 100,
'accuracy': 95,
'pp': 5
}
sacred_sword_dict = {
'name': "Sacred Sword",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 20
}
safeguard_dict = {
'name': "Safeguard",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_safeguard),
"{} {} {}".format(constants.pkm_ally, constants.bestow, constants.status_safeguard)],
'description': "",
'power': None,
'accuracy': None,
'pp': 25
}
sand_attack_dict = {
'name': "Sand Attack",
'type': constants.type_rock,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe , constants.accuracy , constants.by_1_stage )],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
sand_tomb_dict = {
'name': "Sand Tomb",
'type': constants.type_rock,
'category': constants.move_category_physical,
'effects': ["{} {} {}".format(constants.inflict, constants.status_partially_trapped, constants.pkm_foe)],
'description': "",
'power': 35,
'accuracy': 85,
'pp': 15
}
sandstorm_dict = {
'name': "Sandstorm",
'type': constants.type_rock,
'category': constants.move_category_status,
'effects': ["Creates a sandstorm for 5 turns."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
scald_dict = {
'name': "Scald",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 15
}
scary_face_dict = {
'name': "Scary Face",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.speed, constants.by_2_stages)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
scratch_dict = {
'name': "Scratch",
'type': constants.type_normal,
'category': constants.move_category_physical,
'power': 40,
'accuracy': 100,
'pp': 35,
'priority': 0,
'critical hit': 0,
'generation introducted': 1,
'effects': [],
'description': "Scratches the foe with sharp claws.",
'machine': None,
}
screech_dict = {
'name': "Screech",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.defense, constants.by_2_stages)],
'description': "",
'power': None,
'accuracy': 85,
'pp': 40
}
searing_shot_dict = {
'name': "Searing Shot",
'type': constants.type_fire,
'category': constants.move_category_special,
'effects': ["{} {} {} {} ".format("30% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'description': "",
'power': 100,
'accuracy': 100,
'pp': 5
}
secret_power_dict = {
'name': "Secret Power",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 20
}
secret_sword_dict = {
'name': "Secret Power",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 85,
'accuracy': 100,
'pp': 10
}
seed_bomb_dict = {
'name': "Seed Bomb",
'type': constants.type_grass,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 15
}
seed_flare_dict = {
'name': "Seed Flare",
'type': constants.type_grass,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("40% chance", constants.reduces, constants.pkm_foe, constants.special_defense, constants.by_1_stages)],
'description': "",
'power': 120,
'accuracy': 85,
'pp': 5
}
seismic_toss_dict = {
'name': "Seismic Toss",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
self_destruct_dict = {
'name': "Self-Destruct",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': ["{} {} {}".format(constants.pkm_self, constants.inflict, constants.status_user_faints)],
'description': "",
'power': 200,
'accuracy': 100,
'pp': 5
}
shadow_ball_dict = {
'name': "Shadow Ball",
'type': constants.type_ghost,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("20% chance", constants.reduces, constants.pkm_foe, constants.special_defense, constants.by_1_stages)],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 15
}
shadow_claw_dict = {
'name': "Shadow Claw",
'type': constants.type_ghost,
'category': constants.move_category_physical,
'effects': [constants.high_crit_ratio],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 15
}
shadow_force_dict = {
'name': "Shadow Force",
'type': constants.type_ghost,
'category': constants.move_category_physical,
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_shadow_force,
"Can strike through Protect/Detect."],
'description': "",
'power': 120,
'accuracy': 100,
'pp': 5
}
shadow_punch_dict = {
'name': "Shadow Punch",
'type': constants.type_ghost,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 60,
'accuracy': 1000,
'pp': 20
}
shadow_sneak_dict = {
'name': "Shadow Sneak",
'type': constants.type_ghost,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'priority': 1,
'power': 40,
'accuracy': 100,
'pp': 30
}
sharpen_dict = {
'name': "Sharpen",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases , constants.pkm_self , constants.attack , constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': None,
'pp': 30
}
sheer_cold_dict = {
'name': "Sheer Cold",
'type': constants.type_ice,
'category': constants.move_category_special,
'effects': [constants.one_hit_ko],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
shell_smash_dict = {
'name': "Shell Smash",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.attack, constants.by_2_stage),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.special_attack, constants.by_2_stage),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.speed, constants.by_2_stage),
"{} {} {} {}".format(constants.reduces, constants.pkm_self, constants.special_defense, constants.by_1_stage),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.defense, constants.by_1_stage)
],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
shift_gear_dict = {
'name': "Shift Gear",
'type': constants.type_steel,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.attack, constants.by_1_stage),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.speed, constants.by_2_stage)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
shock_wave_dict = {
'name': "Shock Wave",
'type': constants.type_electric,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 60,
'accuracy': 1000,
'pp': 20
}
signal_beam_dict = {
'name': "Signal Beam",
'type': constants.type_bug,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'description': "",
'power': 75,
'accuracy': 100,
'pp': 15
}
silver_wind_dict = {
'name': "Silver Wind",
'type': constants.type_bug,
'category': constants.move_category_special,
'effects': ["{} {} {} {} {}".format("10% chance to", constants.increases, constants.pkm_self, constants.all_stats, constants.by_1_stage)],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 5
}
simple_beam_dict = {
'name': "Simple Beam",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
sing_dict = {
'name': "Sing",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} ".format(constants.inflict, constants.status_sleep, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 55,
'pp': 15
}
sketch_dict = {
'name': "Sketch",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["Permanently copies the opponent's last move."],
'description': "",
'power': None,
'accuracy': None,
'pp': 1
}
skill_swap_dict = {
'name': "Skill Swap",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["The user swaps Abilities with the opponent."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
skull_bash_dict = {
'name': "Skull Bash",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.defense, constants.by_1_stage)
"{} {} {} ".format(constants.pkm_self, constants.bestow, constants.status_charging)],
'description': "",
'power': 130,
'accuracy': 100,
'pp': 10
}
sky_attack_dict = {
'name': "Sky Attack",
'type': constants.type_flying,
'category': constants.move_category_physical,
'effects': ["{} {} {}".format(constants.inflict, constants.status_charging, constants.pkm_self),
"{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 140,
'accuracy': 90,
'pp': 5
}
sky_drop_dict = {
'name': "Sky Drop",
'type': constants.type_flying,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 10
}
sky_uppercut_dict = {
'name': "Sky Uppercut",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': ["Hits the opponent, even during Fly."],
'description': "",
'power': 85,
'accuracy': 90,
'pp': 15
}
slack_off_dict = {
'name': "Slack Off",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
slam_dict = {
'name': "Slam",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 80,
'accuracy': 75,
'pp': 20
}
slash_dict = {
'name': "Slash",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [constants.high_crit_ratio],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 20
}
sleep_powder_dict = {
'name': "Sleep Powder",
'type': constants.type_grass,
'category': constants.move_category_status,
'effects': ["{} {} {} ".format(constants.inflict, constants.status_sleep, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 75,
'pp': 15
}
sleep_talk_dict = {
'name': "Sleep Talk",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
sludge_dict = {
'name': "Sludge",
'type': constants.type_poison,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("30 % chance", constants.inflict, constants.status_poison, constants.pkm_foe)],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 20
}
sludge_bomb_dict = {
'name': "Sludge Bomb",
'type': constants.type_poison,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("30 % chance", constants.inflict, 
constants.status_poison, constants.pkm_foe)],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 10
}
sludge_wave_dict = {
'name': "Sludge Wave",
'type': constants.type_poison,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("10 % chance", constants.inflict, constants.status_poison, constants.pkm_foe)],
'description': "",
'power': 95,
'accuracy': 100,
'pp': 10
}
smack_down_dict = {
'name': "Smack Down",
'type': constants.type_rock,
'category': constants.move_category_physical,
'effects': ["Makes Flying-type Pokémon vulnerable to Ground moves."],
'description': "",
'power': 50,
'accuracy': 100,
'pp': 15
}
smelling_salts_dict = {
'name': "Smelling Salts",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': ["{} {} {}".format(constants.pkm_foe, constants.removes, constants.status_paralysis)]],
'description': "Power doubles if opponent is paralyzed, but cures it.",
'power': 70,
'accuracy': 100,
'pp': 10
}
smog_dict = {
'name': "Smog",
'type': constants.type_poison,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 30,
'accuracy': 70,
'pp': 20
}
smokescreen_dict = {
'name': "Smokescreen",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.accuracy, constants.by_1_stage],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
snarl_dict = {
'name': "Snarl",
'type': constants.type_dark,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.special_attack, constants.by_1_stage],
'description': "",
'power': 55,
'accuracy': 96,
'pp': 15
}
snatch_dict = {
'name': "Snatch",
'type': constants.type_dark,
'category': constants.move_category_special,
'effects': ["Steals the effects of the opponent's next move."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
snore_dict = {
'name': "Snore",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 50,
'accuracy': 100,
'pp': 15
}
soak_dict = {
'name': "Soak",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["Changes the target's type to water."],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
soft_boiled_dict = {
'name': "Soft-Boiled",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
solar_beam_dict = {
'name': "Solar Beam",
'type': constants.type_grass,
'category': constants.move_category_special,
'effects': ["{} {} {}".format(constants.inflict, constants.status_charging, constants.pkm_self)],
'description': "",
'power': 120,
'accuracy': 100,
'pp': 10
}
sonic_boom_dict = {
'name': "Sonic Boom",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': ["{} {} {} to {}".format(constants.inflict, constants.set_amount_of_damage, 20, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 90,
'pp': 20
}
spacial_rend_dict = {
'name': "Spacial Rend",
'type': constants.type_dragon,
'category': constants.move_category_special,
'effects': [constants.high_crit_ratio],
'description': "",
'power': 100,
'accuracy': 95,
'pp': 5
}
spark_dict = {
'name': "Spark",
'type': constants.type_electric,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {}".format("30%", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 20
}
spider_web_dict = {
'name': "Spider Web",
'type': constants.type_bug,
'category': constants.move_category_status,
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_trapped, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
spike_cannon_dict = {
'name': "Spike Cannon",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'multi-hit':[2,5],
'power': 20,
'accuracy': 100,
'pp': 15
}
spikes_dict = {
'name': "Spikes",
'type': constants.type_ground,
'category': constants.move_category_status,
'effects': ["Damages opponent switching into battle."],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
spiky_shield_dict = {
'name': "Spiky Shield",
'type': constants.type_grass,
'category': constants.move_category_status,
'effects': ["Protects user and inflicts damage on contact moves."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
spit_up_dict = {
'name': "Spit up",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': ["{} {} {}".format(constants.pkm_self, constants.remove, constants.status_stockpile)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 10
}
spite_dict = {
'name': "Spite",
'type': constants.type_ghost,
'category': constants.move_category_special,
'effects': ["The opponent's last move loses 2-5 PP."],
'description': "",
'power': None,
'accuracy': 100,
'pp': 10
}
splash_dict = {
'name': "Splash",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 40
}
spore_dict = {
'name': "Spore",
'type': constants.type_grass,
'category': constants.move_category_special,
'effects': ["{} {} {} ".format(constants.inflict, constants.status_sleep, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
stealth_rock_dict = {
'name': "Stealth Rock",
'type': constants.type_rock,
'category': constants.move_category_status,
'effects': ["Damages opponent switching into battle.",],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
steam_eruption_dict = {
'name': "Steam Eruption",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_burn, constants.pkm_foe)],
'description': "",
'power': 110,
'accuracy': 95,
'pp': 5
}
steamroller_dict = {
'name': "Steamroller",
'type': constants.type_bug,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 20
}
steel_wing_dict = {
'name': "Steel Wing",
'type': constants.type_steel,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.increases, constants.defense, constants.by_1_stage)],
'description': "",
'power': 70,
'accuracy': 90,
'pp': 25
}
sticky_web_dict = {
'name': "Sticky Web",
'type': constants.type_bug,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.pkm_foe, constants.reduces, constants.speed, constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
stockpile_dict = {
'name': "Stockpile",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_stockpile)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
stomp_dict = {
'name': "Stomp",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {} ".format("30% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 20
}
stone_edge_dict = {
'name': "Stone Edge",
'type': constants.type_rock,
'category': constants.move_category_physical,
'effects': [constants.high_crit_ratio],
'description': "",
'power': 100,
'accuracy': 80,
'pp': 5
}
stored_power_dict = {
'name': "Stored Power",
'type': constants.type_psychic,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 20,
'accuracy': 100,
'pp': 10
}
storm_throw_dict = {
'name': "Storm Throw",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [constants.always_crit],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 10
}
strength_dict = {
'name': "Strength",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 15
}
string_shot_dict = {
'name': "String Shot",
'type': constants.type_bug,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.speed, constants.by_2_stage)],
'description': "The opposing Pokémon are bound with silk blown from the user’s mouth that harshly lowers the Speed stat.",
'power': None,
'accuracy': 95,
'pp': 40
}
struggle_dict = {
'name': "Struggle",
'type': constants.type_normal,
'category': constants.move_category_physical,
'power': 50,
'accuracy': 100,
'pp': 16,
'priority': 0,
'critical hit': 0,
'generation introducted': 1,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.status_recoil_damage, constants.quarter, constants.damage_delt)],
'description': "Used only if the user runs totally out of PP.  User hit with 1/4 damage delt.",
'machine': None,
}
struggle_bug_dict = {
'name': "Struggle Bug",
'type': constants.type_bug,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_foe, constants.special_attack, constants.by_1_stage)],
'description': "",
'power': 50,
'accuracy': 100,
'pp': 20
}
stun_spore_dict = {
'name': "Stun Spore",
'type': constants.type_grass,
'category': constants.move_category_status,
'effects': ["{} to {} {} on {} ".format("Guranteed", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 75,
'pp': 30
}
submission_dict = {
'name': "Submission",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.status_recoil_damage, constants.quarter, constants.damage_delt)],
'description': "",
'power': 80,
'accuracy': 80,
'pp': 25
}
substitute_dict = {
'name': "Submission",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["Uses HP to creates a decoy that takes hits."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
sucker_punch_dict = {
'name': "Sucker Punch",
'type': constants.type_dark,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'priority': 1,
'power': 80,
'accuracy': 100,
'pp': 5
}
sunny_day_dict = {
'name': "Sunny Day",
'type': constants.type_fire,
'category': constants.move_category_status,
'effects': ["Makes it sunny for 5 turns."],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
super_fang_dict = {
'name': "Super Fang",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': None,
'accuracy': 90,
'pp': 10
}
superpower_dict = {
'name': "Superpower",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 120,
'accuracy': 100,
'pp': 5
}
superpower_dict = {
'name': "Superpower",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.reduces, constants.pkm_self, constants.attack, constants.by_1_stages)
"{} {} {} {}".format(constants.reduces, constants.pkm_self, constants.defense, constants.by_1_stages)],
'description': "",
'power': 120,
'accuracy': 100,
'pp': 5
}
supersonic_dict = {
'name': "Supersonic",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} to {} {} on {} ".format("Guranteed", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 55,
'pp': 20
}
surf_dict = {
'name': "Surf",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["Hits all adjacent Pokémon."],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 15
}
swagger_dict = {
'name': "Swagger",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} to {} {} on {} ".format("Guarenteed", constants.inflict, constants.status_confusion, constants.pkm_foe),
"{} {} {} {} {}".format("10% chance to ", constants.increases, constants.pkm_foe, constants.attack, constants.by_2_stages)],
'description': "",
'power': None,
'accuracy': 90,
'pp': 15
}
swallow_dict = {
'name': "Swallow",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_self, constants.remove, constants.status_stockpile)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
sweet_kiss_dict = {
'name': "Sweet Kiss",
'type': constants.type_fairy,
'category': constants.move_category_status,
'effects': ["{} {} {} {} ".format("Guarenteed", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 75,
'pp': 10
}
sweet_scent_dict = {
'name': "Sweet Scent",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
swift_dict = {
'name': "Swift",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 60,
'accuracy': 1000,
'pp': 20
}
switcheroo_dict = {
'name': "Switcheroo",
'type': constants.type_dark,
'category': constants.move_category_status,
'effects': ["Swaps held items with the opponent."],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
swords_dance_dict = {
'name': "Swords Dance",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.attack, constants.by_2_stages)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
synchronoise_dict = {
'name': "Synchronoise",
'type': constants.type_psychic,
'category': constants.move_category_special,
'effects': ["Hits any Pokémon that shares a type with the user."],
'description': "",
'power': 120,
'accuracy': 100,
'pp': 15
}
synthesis_dict = {
'name': "Synthesis",
'type': constants.type_grass,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
#t,
tackle_dict = {
'name': "Tackle",
'type': constants.type_normal,
'category': constants.move_category_physical,
'power': 50,
'accuracy': 100,
'pp': 35,
'priority': 0,
'critical hit': 0,
'generation introducted': 1,
'effects': [],
'description': "Charges the foe with a full-body tackle.",
'machine': None,
}
tail_glow_dict = {
'name': "Tail Glow",
'type': constants.type_bug,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.special_attack, constants.by_3_stages)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
tail_slap_dict = {
'name': "Tail Slap",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'multi-hit':[2,5],
'power': 25,
'accuracy': 85,
'pp': 10
}
#'multi-hit':[2,5],
tail_whip_dict = {
'name': "Tail Whip",
'type': constants.type_normal,
'category': constants.move_category_status,
'power': None,
'accuracy': 100,
'pp': 30,
'priority': 0,
'critical hit': 0,
'generation introducted': 1,
'effects': ["Reduces Foe Defense 1 Stage"],
'description': "Wags the tail to lower the foe's Defense.",
'machine': None,
}
tailwind_dict = {
'name': "Tailwind",
'type': constants.type_flying,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_tailwind)],
'description': "",
'power': None,
'accuracy': None,
'pp': 30
}
take_down_dict = {
'name': "Take Down",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.status_recoil_damage, constants.quarter, constants.damage_delt)],
'description': "",
'power': 90,
'accuracy': 85,
'pp': 20
}
taunt_dict = {
'name': "Taunt",
'type': constants.type_dark,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_foe, constants.inflict, constants.status_taunt)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
techno_blast_dict = {
'name': "Techno Blast",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': ["Type depends on the Drive being held."s],
'description': "",
'power': 85,
'accuracy': 100,
'pp': 5
}
teeter_dance_dict = {
'name': "Teeter Dance",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} to {} {} on {} ".format("Guarenteed", constants.inflict, constants.status_confusion, constants.pkm_foe),
"{} to {} {} on {} ".format("Guarenteed", constants.inflict, constants.status_confusion, constants.pkm_ally)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
telekinesis_dict = {
'name': "Telekinesis",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_foe, constants.inflict, constants.status_levitation)],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
teleport_dict = {
'name': "Teleport",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_self, constants.switches_ally, constants.transfer_stats_changes),
"Allows user to flee wild battles."],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
thief_dict = {
'name': "Thief",
'type': constants.type_dark,
'category': constants.move_category_physical,
'effects': ["Steals opponent's held item."],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 25
}
thousand_arrows_dict = {
'name': "Thousand Arrows",
'type': constants.type_ground,
'category': constants.move_category_physical,
'effects': ["Makes Flying-type Pokémon vulnerable to Ground moves."],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 10
}
thousand_waves_dict = {
'name': "Thousand Waves",
'type': constants.type_ground,
'category': constants.move_category_physical,
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_trapped, constants.pkm_foe)],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 10
}
thrash_dict = {
'name': "Thrash",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
#'multi-hit':[2,3],
'power': 120,
'accuracy': 100,
'pp': 10
}
thunder_dict = {
'name': "Thunder",
'type': constants.type_electric,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {}".format("30%", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': 110,
'accuracy': 70,
'pp': 10
}
thunder_fang_dict = {
'name': "Thunder Fang",
'type': constants.type_electric,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {}".format("10%", constants.inflict, constants.status_paralysis, constants.pkm_foe),
"{} to {} {} on {}".format("10%", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 65,
'accuracy': 95,
'pp': 15
}
thunder_punch_dict = {
'name': "Thunder Punch",
'type': constants.type_electric,
'category': constants.move_category_physical,
'effects': ["{} to {} {} on {}".format("10% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': 75,
'accuracy': 100,
'pp': 15
}
thunder_shock_dict = {
'name': "Thunder Shock",
'type': constants.type_electric,
'category': constants.move_category_special,
'power': 40,
'accuracy': 100,
'pp': 30,
'priority': 0,
'critical hit': 0,
'generation introducted': 1,
'effects': ["{} to {} {} on {}".format("10% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'machine': None,
}
thunder_wave_dict = {
'name': "Thunder Wave",
'type': constants.type_electric,
'category': constants.move_category_status,
'effects': ["{} to {} {} on {}".format("Guaranteed", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
thunderbolt_dict = {
'name': "Thunderbolt",
'type': constants.type_electric,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {}".format("10% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 15
}
tickle_dict = {
'name': "Tickle",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.pkm_foe, constants.reduces, constants.attack, constants.by_1_stage),
"{} {} {} {}".format(constants.pkm_foe, constants.reduces, constants.defense, constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
topsy_turvy_dict = {
'name': "Topsy-Turvy",
'type': constants.type_dark,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_foe, constants.inflict, constants.reverse_stats)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
torment_dict = {
'name': "Torment",
'type': constants.type_dark,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.pkm_foe, constants.inflict, constants.status_torment)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
toxic_dict = {
'name': "Toxic",
'type': constants.type_poison,
'category': constants.move_category_status,
'effects': ["When Switching, {} to {} {} on {} ".format("guaranteed", constants.inflict, constants.status_badly_poison, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 90,
'pp': 10
}
toxic_spikes_dict = {
'name': "Toxic Spikes",
'type': constants.type_poison,
'category': constants.move_category_status,
'effects': ["Damages opponent switching into battle.",
"{} to {} {} on {}".format("guaranteed", constants.inflict, constants.status_poison, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
transform_dict = {
'name': "Transform",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
tri_attack_dict = {
'name': "Tri Attack",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': [
"{} to {} {} on {}".format("20% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe),
"{} to {} {} on {}".format("20% chance", constants.inflict, constants.status_burn, constants.pkm_foe),
"{} to {} {} on {}".format("20% chance", constants.inflict, constants.status_freeze, constants.pkm_foe)],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 10
}
trick_dict = {
'name': "Trick",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["Swaps held items with the opponent."],
'description': "",
'power': 100,
'accuracy': None,
'pp': 10
}
trick_room_dict = {
'name': "Trick Room",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.inflict, constants.status_trick_room, constants.pkm_foe),
"{} {} {}".format(constants.inflict, constants.status_trick_room, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 5
}
trick_or_treat_dict = {
'name': "Trick-or-Treat",
'type': constants.type_ghost,
'category': constants.move_category_status,
'effects': ["Adds Ghost type to opponent."],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
triple_kick_dict = {
'name': "Triple Kick",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 10,
'multi-hit':[3,3],
'accuracy': 90,
'pp': 10
}
trump_card_dict = {
'name': "Trump Card",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': None,
'accuracy': 1000,
'pp': 5
}
twineedle_dict = {
'name': "Twineedle",
'type': constants.type_bug,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'multi-hit':[2,2],
'power': 25,
'accuracy': 100,
'pp': 20
}
twister_dict = {
'name': "Twister",
'type': constants.type_dragon,
'category': constants.move_category_special,
'effects': ["{} {} {} {} ".format("20% chance", constants.inflict, constants.status_flinch, constants.pkm_foe),
"Hits Pokémon using Fly/Bounce with double power."],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 20
}
#u,
u_turn_dict = {
'name': "U-turn",
'type': constants.type_bug,
'category': constants.move_category_physical,
'effects': ["{} {}".format(constants.pkm_self, constants.switches_ally)],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 20
}
uproar_dict = {
'name': "Uproar",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 10
}
#v,
v_create_dict = {
'name': "V-Create",
'type': constants.type_fire,
'category': constants.move_category_special,
'effects': ["{} {} {} {}".format(constants.pkm_foe, constants.reduces, constants.defense, constants.by_1_stage),
"{} {} {} {}".format(constants.pkm_foe, constants.reduces, constants.special_defense, constants.by_1_stage),
"{} {} {} {}".format(constants.pkm_foe, constants.reduces, constants.speed, constants.by_1_stage)],
'description': "",
'power': 180,
'accuracy': 95,
'pp': 5
}
vacuum_wave_dict = {
'name': "Vacuum Wave",
'type': constants.type_fighting,
'category': constants.move_category_special,
'effects': [],
'description': "",
'priority': 1,
'power': 40,
'accuracy': 100,
'pp': 30
}
venom_drench_dict = {
'name': "Venom Drench",
'type': constants.type_poison,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.pkm_foe, constants.reduces, constants.special_attack, constants.by_1_stage),
"{} {} {} {}".format(constants.pkm_foe, constants.reduces, constants.speed, constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 20
}
venoshock_dict = {
'name': "Venoshock",
'type': constants.type_poison,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 65,
'accuracy': 100,
'pp': 10
}
vice_grip_dict = {
'name': "Vice Grip",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 55,
'accuracy': 100,
'pp': 30
}
vine_whip_dict = {
'name': "Vine Whip",
'type': constants.type_grass,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 45,
'accuracy': 100,
'pp': 25
}
vital_throw_dict = {
'name': "Vital Throw",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 70,
'priority': -1,
'accuracy': 1000,
'pp': 10
}
volt_switch_dict = {
'name': "Volt Switch",
'type': constants.type_electric,
'category': constants.move_category_special,
'effects': ["{} {}".format(constants.pkm_self, constants.switches_ally)],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 20
}
volt_tackle_dict = {
'name': "Volt Tackle",
'type': constants.type_electric,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.status_recoil_damage, constants.third, constants.damage_delt),
"{} to {} {} on {} ".format("10% chance", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': 120,
'accuracy': 100,
'pp': 15
}
#w,
wake_up_slap_dict = {
'name': "Wake-Up Slap",
'type': constants.type_fighting,
'category': constants.move_category_physical,
'effects': ["{} {} {} ".format(constants.remove, constants.status_sleep, constants.pkm_foe)],
'description': "",
'power': 70,
'accuracy': 100,
'pp': 10
}
water_gun_dict = {
'name': "Water Gun",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 25
}
water_pledge_dict = {
'name': "Water Pledge",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 10
}
water_pulse_dict = {
'name': "Water Pulse",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["{} {} {} {} ".format("20% chance", constants.inflict, constants.status_confusion, constants.pkm_foe)],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 20
}
water_shuriken_dict = {
'name': "Water Shuriken",
'type': constants.type_water,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'multi-hit':[2,5],
'power': 15,
'accuracy': 100,
'pp': 10
}
water_sport_dict = {
'name': "Water Sport",
'type': constants.type_water,
'category': constants.move_category_status,
'effects': ["Weakens the power of Fire-type moves."],
'description': "",
'power': None,
'accuracy': None,
'pp': 15
}
water_spout_dict = {
'name': "Water Spout",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 150,
'accuracy': 100,
'pp': 5
}
waterfall_dict = {
'name': "Waterfall",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("20% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 15
}
weather_ball_dict = {
'name': "Weather Ball",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': 50,
'accuracy': 100,
'pp': 10
}
whirlpool_dict = {
'name': "Whirlpool",
'type': constants.type_water,
'category': constants.move_category_special,
'effects': ["{} {} {}".format(constants.inflict, constants.status_partially_trapped, constants.pkm_foe)],
'description': "",
'power': 30,
'accuracy': 85,
'pp': 15
}
whirlwind_dict = {
'name': "Whirlwind",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': [constants.switches_opponent],
'description': "",
'power': None,
'accuracy': None,
'pp': 20
}
wide_guard_dict = {
'name': "Wide Gaurd",
'type': constants.type_rock,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.bestow, constants.status_partially_trapped, constants.pkm_self),
"{} {} {}".format(constants.bestow, constants.status_partially_trapped, constants.pkm_ally)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
wild_charge_dict = {
'name': "Wild Charge",
'type': constants.type_electric,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.status_recoil_damage, constants.quarter, constants.damage_delt)],
'description': "",
'power': 90,
'accuracy': 100,
'pp': 15
}
will_o_wisp_dict = {
'name': "Will-O-Wisp",
'type': constants.type_ghost,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.inflict, constants.status_burn, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 85,
'pp': 15
}
wing_attack_dict = {
'name': "Wing Attack",
'type': constants.type_flying,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 60,
'accuracy': 100,
'pp': 35
}
wish_dict = {
'name': "Wish",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.recovers, constants.half, constants.health, constants.pkm_self)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
withdraw_dict = {
'name': "Withdraw",
'type': constants.type_water,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.defense, constants.by_1_stage),
"{} {} {}".format(constants.pkm_self, constants.bestow, constants.status_withdraw)],
'description': "",
'power': None,
'accuracy': None,
'pp': 40
}
wonder_room_dict = {
'name': "Wonder Room",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["Swaps every Pokémon's Defense and Special Defense for 5 turns."],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
wood_hammer_dict = {
'name': "Wood Hammer",
'type': constants.type_grass,
'category': constants.move_category_physical,
'effects': ["{} {} {} {}".format(constants.pkm_self, constants.status_recoil_damage, constants.third, constants.damage_delt)],
'description': "",
'power': 120,
'accuracy': 100,
'pp': 15
}
work_up_dict = {
'name': "Work Up",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {}".format(constants.increases, constants.pkm_self, constants.attack, constants.by_1_stage),
"{} {} {} {}".format(constants.increases, constants.pkm_self, constants.special_attack, constants.by_1_stage)],
'description': "",
'power': None,
'accuracy': None,
'pp': 30
}
worry_seed_dict = {
'name': "Worry Seed",
'type': constants.type_grass,
'category': constants.move_category_status,
'effects': ["Changes the opponent's Ability to Insomnia."],
'description': "",
'power': None,
'accuracy': 100,
'pp': 10
}
wrap_dict = {
'name': "Wrap",
'type': constants.type_normal,
'category': constants.move_category_physical,
'effects': ["{} {} {}".format(constants.inflict, constants.status_partially_trapped, constants.pkm_foe)],
'description': "",
'power': 15,
'accuracy': 90,
'pp': 20
}
wring_out_dict = {
'name': "Wring Out",
'type': constants.type_normal,
'category': constants.move_category_special,
'effects': [],
'description': "",
'power': None,
'accuracy': 100,
'pp': 5
}
#x,
x_scissor_dict = {
'name': "X Scissor",
'type': constants.type_bug,
'category': constants.move_category_physical,
'effects': [],
'description': "",
'power': 80,
'accuracy': 100,
'pp': 15
}
#y,
yawn_dict = {
'name': "Yawn",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {} {} ".format("Next Turn", constants.inflict, constants.status_sleep, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': None,
'pp': 10
}
#z.
zap_cannon_dict = {
'name': "Zap Cannon",
'type': constants.type_electric,
'category': constants.move_category_special,
'effects': ["{} to {} {} on {} ".format("Guranteed", constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': 120,
'accuracy': 50,
'pp': 5
}
zen_headbutt_dict = {
'name': "Zen Headbutt",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} to {} {} on {} ".format("20% chance", constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 80,
'accuracy': 90,
'pp': 15
}
#'multi-hit':[2,2],