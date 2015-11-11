from constants import constants
from move_dict import *
#
# constants.type_normal constants.type_fire
# constants.type_water  constants.type_electric
# constants.type_ice    constants.type_fighting
# constants.type_grass, constants.type_poison
# constants.type_ground constants.type_flying
# constants.type_psychic constants.type_bug
# constants.type_rock   constants.type_ghost
# constants.type_dragon constants.type_dark
# constants.type_steel  constants.type_fairy
#
#move_category_physical = "Physical"
#move_category_special = "Special"
#move_category_status = "Status"
#
class move():
    def __init__(self, move_dict=None, copy=False):
        self.name = "Struggle"
        self.type = constants.type_normal
        self.category = constants.move_category_physical
        #constants.move_category_physical = "Physical"
        #constants.move_category_special = "Special"
        #constants.move_category_status = "Status"
        self.power = 50
        self.accuracy = 100
        self.pp_max = 16
        self.pp = 16
        self.priority = 0
        self.critical_hit = 0
        self.generation_introducted = 1
        self.effects = "Recoil damage."
        self.description = 'Used only if the user runs totally out of PP.  The user is hit with 1/2 of the damage it inflicts.'
        self.machine = None # either TM 1-? or HM 1-?
        self.multi_hit = [1,1]
        is_disabled = False
        if move_dict is not None:
            self.set_move_from_dict(move_dict=move_dict, copy=copy)
    def set_move_from_dict(self, move_dict=None, copy=False):
        self.name = move_dict.get('name')
        self.type = move_dict.get('type')
        self.category = move_dict.get('category')
        self.power = move_dict.get('power')
        self.accuracy = move_dict.get('accuracy')
        self.pp_max = move_dict.get('pp')
        self.pp = move_dict.get('pp')
        if move_dict.get('priority') is not None:
            self.priority = move_dict.get('priority')
        else:
            self.priority = 0
        self.critical_hit = move_dict.get('critical hit')
        self.generation_introducted = move_dict.get('generation introducted')
        self.effects = move_dict.get('effects')
        self.description = move_dict.get('description')
        self.machine = move_dict.get('machine')
        if move_dict.get('multi-hit') is not None:
            self.multi_hit = move_dict.get('multi-hit')
        if copy:
            return self.copy()
    def copy(self):
        new_move = move()
        new_move.name = self.name
        new_move.type = self.type
        new_move.category = self.category
        new_move.power = self.power
        new_move.accuracy = self.accuracy
        new_move.pp_max = self.pp_max
        new_move.pp = self.pp
        new_move.priority = self.priority
        new_move.critical_hit = self.critical_hit
        new_move.generation_introducted = self.generation_introducted
        new_move.effects = self.effects
        new_move.description = self.description
        new_move.multi_hit = self.multi_hit 
        new_move.machine = self.machine
        #print new_move.__str__()
        return new_move
    def __str__(self):
        info = "{0}: ({1}, {2}), Power: {3}, PP: {4} / {5}".format(self.name, self.type.name, self.category, self.power, self.pp, self.pp_max)
        return info
    def get_move(self):
        info = "{0:15}{1}\n".format('MOVE:', self.name)
        info += "{0:15}{1}\n".format('TYPE:', self.type.name)
        info += "{0:15}{1}\n".format('CATEGORY:', self.category)
        info += "{0:15}{1}\n".format('POWER:', self.power)
        info += "{0:15}{1}\n".format('ACCURACY:', self.accuracy)
        info += "{0:15}{1} / {2}\n".format('PP:', self.pp, self.pp_max)
        info += "{0:15}{1} {2}\n".format('INTRODUCED:', 'Generation', self.generation_introducted)
        info += "{0:15}{1}\n".format('EFFECTS:', self.effects)
        info += "{0:15}{1}\n".format('DESCRIPTION:', self.description)
        info += "{0:15}{1}\n".format('MACHINE:', self.machine)
        return info
    def has_effect(self, move_effect=None):
        if move_effect is None:
            return None
        for effect in self.effects:
            if move_effect in effect:
                return True
        return False
# All Moves 
#a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z
# new_move = move(_dict).set_move_from_dict(move_dict, True)

#
hit_self_in_confusion = move(hit_self_in_confusion_dict)
#a
absorb = move(absorb_dict)#.set_move_from_dict(_dict, True)
acid = move(acid_dict)#.set_move_from_dict(_dict, True)
acid_armor = move(acid_armor_dict)#.set_move_from_dict(_dict, True)
acid_spray = move(acid_spray_dict)#.set_move_from_dict(_dict, True)
acrobatics = move(acrobatics_dict)#.set_move_from_dict(_dict, True)
acupressure = move(acupressure_dict)#.set_move_from_dict(_dict, True)
aerial_ace = move(aerial_ace_dict)#.set_move_from_dict(_dict, True)
aeroblast = move(aeroblast_dict)#.set_move_from_dict(_dict, True)
after_you = move(after_you_dict)#.set_move_from_dict(_dict, True)
agility = move(agility_dict)#.set_move_from_dict(_dict, True)
air_cutter = move(air_cutter_dict)#.set_move_from_dict(_dict, True)
air_slash = move(air_slash_dict)#.set_move_from_dict(_dict, True)
ally_switch = move(ally_switch_dict)#.set_move_from_dict(_dict, True)
amnesia = move(amnesia_dict)#.set_move_from_dict(_dict, True)
ancient_power = move(ancient_power_dict)#.set_move_from_dict(_dict, True)
aqua_jet = move(aqua_jet_dict)#.set_move_from_dict(_dict, True)
aqua_ring = move(aqua_ring_dict)#.set_move_from_dict(_dict, True)
aqua_tail = move(aqua_tail_dict)#.set_move_from_dict(_dict, True)
arm_thrust = move(arm_thrust_dict)#.set_move_from_dict(_dict, True)
aromatherapy = move(aromatherapy_dict)#.set_move_from_dict(_dict, True)
aromatic_mist = move(aromatic_mist_dict)#.set_move_from_dict(_dict, True)
assist = move(assist_dict)#.set_move_from_dict(_dict, True)
assurance = move(assurance_dict)#.set_move_from_dict(_dict, True)
astonish = move(astonish_dict)#.set_move_from_dict(_dict, True)
attack_order = move(attack_order_dict)#.set_move_from_dict(_dict, True)
attract = move(attract_dict)#.set_move_from_dict(_dict, True)
aura_sphere = move(aura_sphere_dict)#.set_move_from_dict(_dict, True)
aurora_beam = move(aurora_beam_dict)#.set_move_from_dict(_dict, True)
aura_sphere = move(aura_sphere_dict)#.set_move_from_dict(_dict, True)
aurora_beam = move(aurora_beam_dict)#.set_move_from_dict(_dict, True)
autotomize = move(autotomize_dict)#.set_move_from_dict(_dict, True)
avalanche = move(avalanche_dict)#.set_move_from_dict(_dict, True)
#b
baby_doll_eyes = move(baby_doll_eyes_dict)#.set_move_from_dict(_dict, True)
barrage = move(barrage_dict)#.set_move_from_dict(_dict, True)
barrier = move(barrier_dict)#.set_move_from_dict(_dict, True)
baton_pass = move(baton_pass_dict)#.set_move_from_dict(_dict, True)
beat_up = move(beat_up_dict)#.set_move_from_dict(_dict, True)
belch = move(belch_dict)#.set_move_from_dict(_dict, True)
belly_drum = move(belly_drum_dict)#.set_move_from_dict(_dict, True)
bestow = move(bestow_dict)#.set_move_from_dict(_dict, True)
bide = move(bide_dict)#.set_move_from_dict(_dict, True)
bind = move(bind_dict)#.set_move_from_dict(_dict, True)
bite = move(bite_dict)#.set_move_from_dict(_dict, True)
blast_burn = move(blast_burn_dict)#.set_move_from_dict(_dict, True)
blaze_kick = move(blaze_kick_dict)#.set_move_from_dict(_dict, True)
blizzard = move(blizzard_dict)#.set_move_from_dict(_dict, True)
block = move(block_dict)#.set_move_from_dict(_dict, True)
blue_flare = move(blue_flare_dict)#.set_move_from_dict(_dict, True)
body_slam = move(body_slam_dict)#.set_move_from_dict(_dict, True)
bolt_strike = move(bolt_strike_dict)#.set_move_from_dict(_dict, True)
bone_club = move(bone_club_dict)#.set_move_from_dict(_dict, True)
bone_rush = move(bone_rush_dict)#.set_move_from_dict(_dict, True)
bonemerang = move(bonemerang_dict)#.set_move_from_dict(_dict, True)
boomburst = move(boomburst_dict)#.set_move_from_dict(_dict, True)
bounce = move(bounce_dict)#.set_move_from_dict(_dict, True)
brave_bird = move(brave_bird_dict)#.set_move_from_dict(_dict, True)
brick_break = move(brick_break_dict)#.set_move_from_dict(_dict, True)
brine = move(brine_dict)#.set_move_from_dict(_dict, True)
bubble = move(bubble_dict)#.set_move_from_dict(_dict, True)
bubble_beam = move(bubble_beam_dict)#.set_move_from_dict(_dict, True)
bug_bite = move(bug_bite_dict)#.set_move_from_dict(_dict, True)
bug_buzz = move(bug_buzz_dict)#.set_move_from_dict(_dict, True)
bulk_up = move(bulk_up_dict)#.set_move_from_dict(_dict, True)
bulldoze = move(bulldoze_dict)#.set_move_from_dict(_dict, True)
bullet_punch = move(bullet_punch_dict)#.set_move_from_dict(_dict, True)
bullet_seed = move(bullet_seed_dict)#.set_move_from_dict(_dict, True)
#c
calm_mind = move(calm_mind_dict)#.set_move_from_dict(_dict, True)
camouflage = move(camouflage_dict)#.set_move_from_dict(_dict, True)
captivate = move(captivate_dict)#.set_move_from_dict(_dict, True)
celebrate = move(celebrate_dict)#.set_move_from_dict(_dict, True)
charge = move(charge_dict)#.set_move_from_dict(_dict, True)
charge_beam = move(charge_beam_dict)#.set_move_from_dict(_dict, True)
charm = move(charm_dict)#.set_move_from_dict(_dict, True)
chatter = move(chatter_dict)#.set_move_from_dict(_dict, True)
chip_away = move(chip_away_dict)#.set_move_from_dict(_dict, True)
circle_throw = move(circle_throw_dict)#.set_move_from_dict(_dict, True)
clamp = move(clamp_dict)#.set_move_from_dict(_dict, True)
clear_smog = move(clear_smog_dict)#.set_move_from_dict(_dict, True)
close_combat = move(close_combat_dict)#.set_move_from_dict(_dict, True)
coil = move(coil_dict)#.set_move_from_dict(_dict, True)
comet_punch = move(comet_punch_dict)#.set_move_from_dict(_dict, True)
confide = move(confide_dict)#.set_move_from_dict(_dict, True)
confuse_ray = move(confuse_ray_dict)#.set_move_from_dict(_dict, True)
confusion = move(confusion_dict)#.set_move_from_dict(_dict, True)
constrict = move(constrict_dict)#.set_move_from_dict(_dict, True)
conversion = move(conversion_dict)#.set_move_from_dict(_dict, True)
conversion_2 = move(conversion_2_dict)#.set_move_from_dict(_dict, True)
copycat = move(copycat_dict)#.set_move_from_dict(_dict, True)
cosmic_power = move(cosmic_power_dict)#.set_move_from_dict(_dict, True)
cotton_guard = move(cotton_guard_dict)#.set_move_from_dict(_dict, True)
cotton_spore = move(cotton_spore_dict)#.set_move_from_dict(_dict, True)
counter = move(counter_dict)#.set_move_from_dict(_dict, True)
covet = move(covet_dict)#.set_move_from_dict(_dict, True)
crabhammer = move(crabhammer_dict)#.set_move_from_dict(_dict, True)
crafty_shield = move(crafty_shield_dict)#.set_move_from_dict(_dict, True)
cross_chop = move(cross_chop_dict)#.set_move_from_dict(_dict, True)
cross_poison = move(cross_poison_dict)#.set_move_from_dict(_dict, True)
crunch = move(crunch_dict)#.set_move_from_dict(_dict, True)
crush_claw = move(crush_claw_dict)#.set_move_from_dict(_dict, True)
crush_grip = move(crush_grip_dict)#.set_move_from_dict(_dict, True)
curse = move(curse_dict)#.set_move_from_dict(_dict, True)
cut = move(cut_dict)#.set_move_from_dict(_dict, True)
#d
dark_pulse = move(dark_pulse_dict)#.set_move_from_dict(_dict, True)
dark_void = move(dark_void_dict)#.set_move_from_dict(_dict, True)
dazzling_gleam = move(dazzling_gleam_dict)#.set_move_from_dict(_dict, True)
defend_order = move(defend_order_dict)#.set_move_from_dict(_dict, True)
defense_curl = move(defense_curl_dict)#.set_move_from_dict(_dict, True)
defog = move(defog_dict)#.set_move_from_dict(_dict, True)
destiny_bond = move(destiny_bond_dict)#.set_move_from_dict(_dict, True)
detect = move(detect_dict)#.set_move_from_dict(_dict, True)
diamond_storm = move(diamond_storm_dict)#.set_move_from_dict(_dict, True)
dig = move(dig_dict)#.set_move_from_dict(_dict, True)
disable = move(disable_dict)#.set_move_from_dict(_dict, True)
disarming_voice = move(disarming_voice_dict)#.set_move_from_dict(_dict, True)
discharge = move(discharge_dict)#.set_move_from_dict(_dict, True)
dive = move(dive_dict)#.set_move_from_dict(_dict, True)
dizzy_punch = move(dizzy_punch_dict)#.set_move_from_dict(_dict, True)
doom_desire = move(doom_desire_dict)#.set_move_from_dict(_dict, True)
double_hit = move(double_hit_dict)#.set_move_from_dict(_dict, True)
double_kick = move(double_kick_dict)#.set_move_from_dict(_dict, True)
double_slap = move(double_slap_dict)#.set_move_from_dict(_dict, True)
double_team = move(double_team_dict)#.set_move_from_dict(_dict, True)
double_edge = move(double_edge_dict)#.set_move_from_dict(_dict, True)
draco_meteor = move(draco_meteor_dict)#.set_move_from_dict(_dict, True)
dragon_ascent = move(dragon_ascent_dict)#.set_move_from_dict(_dict, True)
dragon_breath = move(dragon_breath_dict)#.set_move_from_dict(_dict, True)
dragon_claw = move(dragon_claw_dict)#.set_move_from_dict(_dict, True)
dragon_dance = move(dragon_dance_dict)#.set_move_from_dict(_dict, True)
dragon_pulse = move(dragon_pulse_dict)#.set_move_from_dict(_dict, True)
dragon_rage = move(dragon_rage_dict)#.set_move_from_dict(_dict, True)
dragon_rush = move(dragon_rush_dict)#.set_move_from_dict(_dict, True)
dragon_tail = move(dragon_tail_dict)#.set_move_from_dict(_dict, True)
drain_punch = move(drain_punch_dict)#.set_move_from_dict(_dict, True)
draining_kiss = move(draining_kiss_dict)#.set_move_from_dict(_dict, True)
dream_eater = move(dream_eater_dict)#.set_move_from_dict(_dict, True)
drill_peck = move(drill_peck_dict)#.set_move_from_dict(_dict, True)
drill_run = move(drill_run_dict)#.set_move_from_dict(_dict, True)
dual_chop = move(dual_chop_dict)#.set_move_from_dict(_dict, True)
dynamic_punch = move(dynamic_punch_dict)#.set_move_from_dict(_dict, True)
#e
earth_power = move(earth_power_dict)#.set_move_from_dict(_dict, True)
earthquake = move(earthquake_dict)#.set_move_from_dict(_dict, True)
echoed_voice = move(echoed_voice_dict)#.set_move_from_dict(_dict, True)
eerie_impulse = move(eerie_impulse_dict)#.set_move_from_dict(_dict, True)
egg_bomb = move(egg_bomb_dict)#.set_move_from_dict(_dict, True)
electric_terrain = move(electric_terrain_dict)#.set_move_from_dict(_dict, True)
electrify = move(electrify_dict)#.set_move_from_dict(_dict, True)
electro_ball = move(electro_ball_dict)#.set_move_from_dict(_dict, True)
electroweb = move(electroweb_dict)#.set_move_from_dict(_dict, True)
embargo = move(embargo_dict)#.set_move_from_dict(_dict, True)
ember = move(ember_dict)#.set_move_from_dict(_dict, True)
encore = move(encore_dict)#.set_move_from_dict(_dict, True)
endeavor = move(endeavor_dict)#.set_move_from_dict(_dict, True)
endure = move(endure_dict)#.set_move_from_dict(_dict, True)
energy_ball = move(energy_ball_dict)#.set_move_from_dict(_dict, True)
entertainment = move(entertainment_dict)#.set_move_from_dict(_dict, True)
eruption = move(eruption_dict)#.set_move_from_dict(_dict, True)
explosion = move(explosion_dict)#.set_move_from_dict(_dict, True)
extrasensory = move(extrasensory_dict)#.set_move_from_dict(_dict, True)
extreme_speed = move(extreme_speed_dict)#.set_move_from_dict(_dict, True)
#f
facade = move(facade_dict)#.set_move_from_dict(_dict, True)
fairy_lock = move(fairy_lock_dict)#.set_move_from_dict(_dict, True)
fairy_wind = move(fairy_wind_dict)#.set_move_from_dict(_dict, True)
fake_out = move(fake_out_dict)#.set_move_from_dict(_dict, True)
fake_tears = move(fake_tears_dict)#.set_move_from_dict(_dict, True)
false_swipe = move(false_swipe_dict)#.set_move_from_dict(_dict, True)
feather_dance = move(feather_dance_dict)#.set_move_from_dict(_dict, True)
feint = move(feint_dict)#.set_move_from_dict(_dict, True)
feint_attack = move(feint_attack_dict)#.set_move_from_dict(_dict, True)
fell_stinger = move(fell_stinger_dict)#.set_move_from_dict(_dict, True)
fiery_dance = move(fiery_dance_dict)#.set_move_from_dict(_dict, True)
final_gambit = move(final_gambit_dict)#.set_move_from_dict(_dict, True)
fire_blast = move(fire_blast_dict)#.set_move_from_dict(_dict, True)
fire_fang = move(fire_fang_dict)#.set_move_from_dict(_dict, True)
fire_pledge = move(fire_pledge_dict)#.set_move_from_dict(_dict, True)
fire_punch = move(fire_punch_dict)#.set_move_from_dict(_dict, True)
fire_spin = move(fire_spin_dict)#.set_move_from_dict(_dict, True)
fissure = move(fissure_dict)#.set_move_from_dict(_dict, True)
flame_burst = move(flame_burst_dict)#.set_move_from_dict(_dict, True)
flame_charge = move(flame_charge_dict)#.set_move_from_dict(_dict, True)
flame_wheel = move(flame_wheel_dict)#.set_move_from_dict(_dict, True)
flamethrower = move(flamethrower_dict)#.set_move_from_dict(_dict, True)
flail = move(flail_dict)#.set_move_from_dict(_dict, True)
flare_blitz = move(flare_blitz_dict)#.set_move_from_dict(_dict, True)
flash = move(flash_dict)#.set_move_from_dict(_dict, True)
flash_cannon = move(flash_cannon_dict)#.set_move_from_dict(_dict, True)
flatter = move(flatter_dict)#.set_move_from_dict(_dict, True)
fling = move(fling_dict)#.set_move_from_dict(_dict, True)
flower_shield = move(flower_shield_dict)#.set_move_from_dict(_dict, True)
fly = move(fly_dict)#.set_move_from_dict(_dict, True)
flying_press = move(flying_press_dict)#.set_move_from_dict(_dict, True)
focus_blast = move(focus_blast_dict)#.set_move_from_dict(_dict, True)
focus_energy = move(focus_energy_dict)#.set_move_from_dict(_dict, True)
focus_punch = move(focus_punch_dict)#.set_move_from_dict(_dict, True)
follow_me = move(follow_me_dict)#.set_move_from_dict(_dict, True)
force_palm = move(force_palm_dict)#.set_move_from_dict(_dict, True)
foresight = move(foresight_dict)#.set_move_from_dict(_dict, True)
forests_curse = move(forests_curse_dict)#.set_move_from_dict(_dict, True)
foul_play = move(foul_play_dict)#.set_move_from_dict(_dict, True)
freeze_shock = move(freeze_shock_dict)#.set_move_from_dict(_dict, True)
freeze_dry = move(freeze_dry_dict)#.set_move_from_dict(_dict, True)
frenzy_plant = move(frenzy_plant_dict)#.set_move_from_dict(_dict, True)
frost_breath = move(frost_breath_dict)#.set_move_from_dict(_dict, True)
frustration = move(frustration_dict)#.set_move_from_dict(_dict, True)
fury_attack = move(fury_attack_dict)#.set_move_from_dict(_dict, True)
fury_cutter = move(fury_cutter_dict)#.set_move_from_dict(_dict, True)
fury_swipes = move(fury_swipes_dict)#.set_move_from_dict(_dict, True)
fusion_bolt = move(fusion_bolt_dict)#.set_move_from_dict(_dict, True)
fusion_flare = move(fusion_flare_dict)#.set_move_from_dict(_dict, True)
future_sight = move(future_sight_dict)#.set_move_from_dict(_dict, True)
#g
gastro_acid = move(gastro_acid_dict)#.set_move_from_dict(_dict, True)
gear_grind = move(gear_grind_dict)#.set_move_from_dict(_dict, True)
gear_grind = move(gear_grind_dict)#.set_move_from_dict(_dict, True)
giga_drain = move(giga_drain_dict)#.set_move_from_dict(_dict, True)
giga_impact = move(giga_impact_dict)#.set_move_from_dict(_dict, True)
glaciate = move(glaciate_dict)#.set_move_from_dict(_dict, True)
glare = move(glare_dict)#.set_move_from_dict(_dict, True)
grass_knot = move(grass_knot_dict)#.set_move_from_dict(_dict, True)
grass_pledge = move(grass_pledge_dict)#.set_move_from_dict(_dict, True)
grass_whistle = move(grass_whistle_dict)#.set_move_from_dict(_dict, True)
grassy_terrain = move(grassy_terrain_dict)#.set_move_from_dict(_dict, True)
gravity = move(gravity_dict)#.set_move_from_dict(_dict, True)
growl = move(growl_dict).set_move_from_dict(growl_dict, True)
growth = move(growth_dict)#.set_move_from_dict(_dict, True)
grudge = move(grudge_dict)#.set_move_from_dict(_dict, True)
guard_split = move(guard_split_dict)#.set_move_from_dict(_dict, True)
guard_swap = move(guard_swap_dict)#.set_move_from_dict(_dict, True)
guillotine = move(guillotine_dict)#.set_move_from_dict(_dict, True)
gunk_shot = move(gunk_shot_dict)#.set_move_from_dict(_dict, True)
gust = move(gust_dict)#.set_move_from_dict(_dict, True)
gyro_ball = move(gyro_ball_dict)#.set_move_from_dict(_dict, True)
#h
hail = move(hail_dict)#.set_move_from_dict(_dict, True)
hammer_arm = move(hammer_arm_dict)#.set_move_from_dict(_dict, True)
happy_hour = move(happy_hour_dict)#.set_move_from_dict(_dict, True)
harden = move(harden_dict)#.set_move_from_dict(_dict, True)
haze = move(haze_dict)#.set_move_from_dict(_dict, True)
head_charge = move(head_charge_dict)#.set_move_from_dict(_dict, True)
head_smash = move(head_smash_dict)#.set_move_from_dict(_dict, True)
headbutt = move(headbutt_dict)#.set_move_from_dict(_dict, True)
heal_bell = move(heal_bell_dict)#.set_move_from_dict(_dict, True)
heal_block = move(heal_block_dict)#.set_move_from_dict(_dict, True)
heal_order = move(heal_order_dict)#.set_move_from_dict(_dict, True)
heal_pulse = move(heal_pulse_dict)#.set_move_from_dict(_dict, True)
healing_wish = move(healing_wish_dict)#.set_move_from_dict(_dict, True)
heart_stamp = move(heart_stamp_dict)#.set_move_from_dict(_dict, True)
heart_swap = move(heart_swap_dict)#.set_move_from_dict(_dict, True)
heat_crash = move(heat_crash_dict)#.set_move_from_dict(_dict, True)
heat_wave = move(heat_wave_dict)#.set_move_from_dict(_dict, True)
heavy_slam = move(heavy_slam_dict)#.set_move_from_dict(_dict, True)
helping_hand = move(helping_hand_dict)#.set_move_from_dict(_dict, True)
hex = move(hex_dict)#.set_move_from_dict(_dict, True)
hidden_power = move(hidden_power_dict)#.set_move_from_dict(_dict, True)
high_jump_kick = move(high_jump_kick_dict)#.set_move_from_dict(_dict, True)
hold_back = move(hold_back_dict)#.set_move_from_dict(_dict, True)
hold_hands = move(hold_hands_dict)#.set_move_from_dict(_dict, True)
hone_claws = move(hone_claws_dict)#.set_move_from_dict(_dict, True)
horn_drill = move(horn_drill_dict)#.set_move_from_dict(_dict, True)
horn_attack = move(horn_attack_dict)#.set_move_from_dict(_dict, True)
horn_leech = move(horn_leech_dict)#.set_move_from_dict(_dict, True)
howl = move(howl_dict)#.set_move_from_dict(_dict, True)
hurricane = move(hurricane_dict)#.set_move_from_dict(_dict, True)
hydro_cannon = move(hydro_cannon_dict)#.set_move_from_dict(_dict, True)
hydro_pump = move(hydro_pump_dict)#.set_move_from_dict(_dict, True)
hyper_beam = move(hyper_beam_dict)#.set_move_from_dict(_dict, True)
hyper_fang = move(hyper_fang_dict)#.set_move_from_dict(_dict, True)
hyper_voice = move(hyper_voice_dict)#.set_move_from_dict(_dict, True)
hyperspace_fury = move(hyperspace_fury_dict)#.set_move_from_dict(_dict, True)
hypnosis = move(hypnosis_dict)#.set_move_from_dict(_dict, True)


#i
ice_ball = move(ice_ball_dict)#.set_move_from_dict(_dict, True)
ice_beam = move(ice_beam_dict)#.set_move_from_dict(_dict, True)
ice_burn = move(ice_burn_dict)#.set_move_from_dict(_dict, True)
ice_fang = move(ice_fang_dict)#.set_move_from_dict(_dict, True)
ice_punch = move(ice_punch_dict)#.set_move_from_dict(_dict, True)
ice_shard = move(ice_shard_dict)#.set_move_from_dict(_dict, True)
icicle_crash = move(icicle_crash_dict)#.set_move_from_dict(_dict, True)
icicle_spear = move(icicle_spear_dict)#.set_move_from_dict(_dict, True)
icy_wind = move(icy_wind_dict)#.set_move_from_dict(_dict, True)
imprison = move(imprison_dict)#.set_move_from_dict(_dict, True)
incinerate = move(incinerate_dict)#.set_move_from_dict(_dict, True)
inferno = move(inferno_dict)#.set_move_from_dict(_dict, True)
infestation = move(infestation_dict)#.set_move_from_dict(_dict, True)
ingrain = move(ingrain_dict)#.set_move_from_dict(_dict, True)
ion_deluge = move(ion_deluge_dict)#.set_move_from_dict(_dict, True)
iron_defense = move(iron_defense_dict)#.set_move_from_dict(_dict, True)
iron_head = move(iron_head_dict)#.set_move_from_dict(_dict, True)
iron_tail = move(iron_tail_dict)#.set_move_from_dict(_dict, True)
#j
judgement = move(judgement_dict)#.set_move_from_dict(_dict, True)
jump_kick = move(jump_kick_dict)#.set_move_from_dict(_dict, True)
#k
karate_chop = move(karate_chop_dict)#.set_move_from_dict(_dict, True)
kinesis = move(kinesis_dict)#.set_move_from_dict(_dict, True)
kings_shield = move(kings_shield_dict)#.set_move_from_dict(_dict, True)
knock_off = move(knock_off_dict)#.set_move_from_dict(_dict, True)
#l
lands_wrath = move(lands_wrath_dict)#.set_move_from_dict(_dict, True)
last_resort = move(last_resort_dict)#.set_move_from_dict(_dict, True)
lava_plume = move(lava_plume_dict)#.set_move_from_dict(_dict, True)
leaf_blade = move(leaf_blade_dict)#.set_move_from_dict(_dict, True)
leaf_storm = move(leaf_storm_dict)#.set_move_from_dict(_dict, True)
leaf_tornado = move(leaf_tornado_dict)#.set_move_from_dict(_dict, True)
leech_life = move(leech_life_dict)#.set_move_from_dict(_dict, True)
leech_seed = move(leech_seed_dict).set_move_from_dict(leech_seed_dict, True)
leer = move(leer_dict)#.set_move_from_dict(_dict, True)
lick = move(lick_dict)#.set_move_from_dict(_dict, True)
light_of_ruin = move(light_of_ruin_dict)#.set_move_from_dict(_dict, True)
light_screen = move(light_screen_dict)#.set_move_from_dict(_dict, True)
lock_on = move(lock_on_dict)#.set_move_from_dict(_dict, True)
lovely_kiss = move(lovely_kiss_dict)#.set_move_from_dict(_dict, True)
low_kick = move(low_kick_dict)#.set_move_from_dict(_dict, True)
low_sweep = move(low_sweep_dict)#.set_move_from_dict(_dict, True)
lucky_chant = move(lucky_chant_dict)#.set_move_from_dict(_dict, True)
lunar_dance = move(lunar_dance_dict)#.set_move_from_dict(_dict, True)
luster_purge = move(luster_purge_dict)#.set_move_from_dict(_dict, True)
#m
mach_punch = move(mach_punch_dict)#.set_move_from_dict(_dict, True)
magic_coat = move(magic_coat_dict)#.set_move_from_dict(_dict, True)
magic_room = move(magic_room_dict)#.set_move_from_dict(_dict, True)
magical_leaf = move(magical_leaf_dict)#.set_move_from_dict(_dict, True)
magma_storm = move(magma_storm_dict)#.set_move_from_dict(_dict, True)
magnet_bomb = move(magnet_bomb_dict)#.set_move_from_dict(_dict, True)
magnet_rise = move(magnet_rise_dict)#.set_move_from_dict(_dict, True)
magnetic_flux = move(magnetic_flux_dict)#.set_move_from_dict(_dict, True)
magnitude = move(magnitude_dict)#.set_move_from_dict(_dict, True)
mat_block = move(mat_block_dict)#.set_move_from_dict(_dict, True)
me_first = move(me_first_dict)#.set_move_from_dict(_dict, True)
mean_look = move(mean_look_dict)#.set_move_from_dict(_dict, True)
meditate = move(meditate_dict)#.set_move_from_dict(_dict, True)
mega_drain = move(mega_drain_dict)#.set_move_from_dict(_dict, True)
mega_kick = move(mega_kick_dict)#.set_move_from_dict(_dict, True)
mega_punch = move(mega_punch_dict)#.set_move_from_dict(_dict, True)
megahorn = move(megahorn_dict)#.set_move_from_dict(_dict, True)
memento = move(memento_dict)#.set_move_from_dict(_dict, True)
metal_burst = move(metal_burst_dict)#.set_move_from_dict(_dict, True)
metal_claw = move(metal_claw_dict)#.set_move_from_dict(_dict, True)
metal_sound = move(metal_sound_dict)#.set_move_from_dict(_dict, True)
meteor_mash = move(meteor_mash_dict)#.set_move_from_dict(_dict, True)
metronome = move(metronome_dict)#.set_move_from_dict(_dict, True)
milk_drink = move(milk_drink_dict)#.set_move_from_dict(_dict, True)
mimic = move(mimic_dict)#.set_move_from_dict(_dict, True)
mind_reader = move(mind_reader_dict)#.set_move_from_dict(_dict, True)
minimize = move(minimize_dict)#.set_move_from_dict(_dict, True)
miracle_eye = move(miracle_eye_dict)#.set_move_from_dict(_dict, True)
mirror_coat = move(mirror_coat_dict)#.set_move_from_dict(_dict, True)
mirror_move = move(mirror_move_dict)#.set_move_from_dict(_dict, True)
mirror_shot = move(mirror_shot_dict)#.set_move_from_dict(_dict, True)
mist = move(mist_dict)#.set_move_from_dict(_dict, True)
mist_ball = move(mist_ball_dict)#.set_move_from_dict(_dict, True)
misty_terrain = move(misty_terrain_dict)#.set_move_from_dict(_dict, True)
moonblast = move(moonblast_dict)#.set_move_from_dict(_dict, True)
moonlight = move(moonlight_dict)#.set_move_from_dict(_dict, True)
morning_sun = move(morning_sun_dict)#.set_move_from_dict(_dict, True)
mud_bomb = move(mud_bomb_dict)#.set_move_from_dict(_dict, True)
mud_shot = move(mud_shot_dict)#.set_move_from_dict(_dict, True)
mud_sport = move(mud_sport_dict)#.set_move_from_dict(_dict, True)
mud_slap = move(mud_slap_dict)#.set_move_from_dict(_dict, True)
muddy_water = move(muddy_water_dict)#.set_move_from_dict(_dict, True)
mystical_fire = move(mystical_fire_dict)#.set_move_from_dict(_dict, True)
#n
nasty_plot = move(nasty_plot_dict)#.set_move_from_dict(_dict, True)
natural_gift = move(natural_gift_dict)#.set_move_from_dict(_dict, True)
nature_power = move(nature_power_dict)#.set_move_from_dict(_dict, True)
needle_arm = move(needle_arm_dict)#.set_move_from_dict(_dict, True)
night_daze = move(night_daze_dict)#.set_move_from_dict(_dict, True)
night_shade = move(night_shade_dict)#.set_move_from_dict(_dict, True)
night_slash = move(night_slash_dict)#.set_move_from_dict(_dict, True)
nightmare = move(nightmare_dict)#.set_move_from_dict(_dict, True)
noble_roar = move(noble_roar_dict)#.set_move_from_dict(_dict, True)
nuzzle = move(nuzzle_dict)#.set_move_from_dict(_dict, True)
#o
oblivion_wing = move(oblivion_wing_dict)#.set_move_from_dict(_dict, True)
octazooka = move(octazooka_dict)#.set_move_from_dict(_dict, True)
odor_sleuth = move(odor_sleuth_dict)#.set_move_from_dict(_dict, True)
ominous_wind = move(ominous_wind_dict)#.set_move_from_dict(_dict, True)
origin_pulse = move(origin_pulse_dict)#.set_move_from_dict(_dict, True)
outrage = move(outrage_dict)#.set_move_from_dict(_dict, True)
overheat = move(overheat_dict)#.set_move_from_dict(_dict, True)
#p
pain_split = move(pain_split_dict)#.set_move_from_dict(_dict, True)
parabolic_charge = move(parabolic_charge_dict)#.set_move_from_dict(_dict, True)
parting_shot = move(parting_shot_dict)#.set_move_from_dict(_dict, True)
pay_day = move(pay_day_dict)#.set_move_from_dict(_dict, True)
payback = move(payback_dict)#.set_move_from_dict(_dict, True)
peck = move(peck_dict)#.set_move_from_dict(_dict, True)
perish_song = move(perish_song_dict)#.set_move_from_dict(_dict, True)
petal_blizzard = move(petal_blizzard_dict)#.set_move_from_dict(_dict, True)
petal_dance = move(petal_dance_dict)#.set_move_from_dict(_dict, True)
phantom_force = move(phantom_force_dict)#.set_move_from_dict(_dict, True)
pin_missile = move(pin_missile_dict)#.set_move_from_dict(_dict, True)
play_nice = move(play_nice_dict)#.set_move_from_dict(_dict, True)
play_rough = move(play_rough_dict)#.set_move_from_dict(_dict, True)
pluck = move(pluck_dict)#.set_move_from_dict(_dict, True)
poison_fang = move(poison_fang_dict)#.set_move_from_dict(_dict, True)
poison_gas = move(poison_gas_dict)#.set_move_from_dict(_dict, True)
poison_jab = move(poison_jab_dict)#.set_move_from_dict(_dict, True)
poison_powder = move(poison_powder_dict)#.set_move_from_dict(_dict, True)
poison_sting = move(poison_sting_dict)#.set_move_from_dict(_dict, True)
poison_tail = move(poison_tail_dict)#.set_move_from_dict(_dict, True)
pound = move(pound_dict)#.set_move_from_dict(_dict, True)
powder = move(powder_dict)#.set_move_from_dict(_dict, True)
powder_snow = move(powder_snow_dict)#.set_move_from_dict(_dict, True)
power_gem = move(power_gem_dict)#.set_move_from_dict(_dict, True)
power_split = move(power_split_dict)#.set_move_from_dict(_dict, True)
power_swap = move(power_swap_dict)#.set_move_from_dict(_dict, True)
power_trick = move(power_trick_dict)#.set_move_from_dict(_dict, True)
power_whip = move(power_whip_dict)#.set_move_from_dict(_dict, True)
power_up_punch = move(power_up_punch_dict)#.set_move_from_dict(_dict, True)
precipice_blades = move(precipice_blades_dict)#.set_move_from_dict(_dict, True)
present = move(present_dict)#.set_move_from_dict(_dict, True)
protect = move(protect_dict)#.set_move_from_dict(_dict, True)
psybeam = move(psybeam_dict)#.set_move_from_dict(_dict, True)
psych_up = move(psych_up_dict)#.set_move_from_dict(_dict, True)
psychic = move(psychic_dict)#.set_move_from_dict(_dict, True)
psycho_boost = move(psycho_boost_dict)#.set_move_from_dict(_dict, True)
psycho_cut = move(psycho_cut_dict)#.set_move_from_dict(_dict, True)
psycho_shift = move(psycho_shift_dict)#.set_move_from_dict(_dict, True)
psyshock = move(psyshock_dict)#.set_move_from_dict(_dict, True)
psystrike = move(psystrike_dict)#.set_move_from_dict(_dict, True)
psywave = move(psywave_dict)#.set_move_from_dict(_dict, True)
punishment = move(punishment_dict)#.set_move_from_dict(_dict, True)
pursuit = move(pursuit_dict)#.set_move_from_dict(_dict, True)
#q
quash = move(quash_dict)#.set_move_from_dict(_dict, True)
quick_attack = move(quick_attack_dict)#.set_move_from_dict(_dict, True)
quick_guard = move(quick_guard_dict)#.set_move_from_dict(_dict, True)
quiver_dance = move(quiver_dance_dict)#.set_move_from_dict(_dict, True)
#r
rage = move(rage_dict)#.set_move_from_dict(_dict, True)
rage_powder = move(rage_powder_dict)#.set_move_from_dict(_dict, True)
rain_dance = move(rain_dance_dict)#.set_move_from_dict(_dict, True)
rapid_spin = move(rapid_spin_dict)#.set_move_from_dict(_dict, True)
razor_leaf = move(razor_leaf_dict)#.set_move_from_dict(_dict, True)
razor_shell = move(razor_shell_dict)#.set_move_from_dict(_dict, True)
razor_wind = move(razor_wind_dict)#.set_move_from_dict(_dict, True)
recover = move(recover_dict)#.set_move_from_dict(_dict, True)
recycle = move(recycle_dict)#.set_move_from_dict(_dict, True)
reflect = move(reflect_dict)#.set_move_from_dict(_dict, True)
reflect_type = move(reflect_type_dict)#.set_move_from_dict(_dict, True)
refresh = move(refresh_dict)#.set_move_from_dict(_dict, True)
relic_song = move(relic_song_dict)#.set_move_from_dict(_dict, True)
rest = move(rest_dict)#.set_move_from_dict(_dict, True)
retaliate = move(retaliate_dict)#.set_move_from_dict(_dict, True)
return_ = move(return_dict)#.set_move_from_dict(_dict, True)
revenge = move(revenge_dict)#.set_move_from_dict(_dict, True)
reversal = move(reversal_dict)#.set_move_from_dict(_dict, True)
roar = move(roar_dict)#.set_move_from_dict(_dict, True)
roar_of_time = move(roar_of_time_dict)#.set_move_from_dict(_dict, True)
rock_blast = move(rock_blast_dict)#.set_move_from_dict(_dict, True)
rock_climb = move(rock_climb_dict)#.set_move_from_dict(_dict, True)
rock_polish = move(rock_polish_dict)#.set_move_from_dict(_dict, True)
rock_slide = move(rock_slide_dict)#.set_move_from_dict(_dict, True)
rock_smash = move(rock_smash_dict)#.set_move_from_dict(_dict, True)
rock_throw = move(rock_throw_dict)#.set_move_from_dict(_dict, True)
rock_tomb = move(rock_tomb_dict)#.set_move_from_dict(_dict, True)
rock_wrecker = move(rock_wrecker_dict)#.set_move_from_dict(_dict, True)
role_play = move(role_play_dict)#.set_move_from_dict(_dict, True)
rolling_kick = move(rolling_kick_dict)#.set_move_from_dict(_dict, True)
rollout = move(rollout_dict)#.set_move_from_dict(_dict, True)
roost = move(roost_dict)#.set_move_from_dict(_dict, True)
rototiller = move(rototiller_dict)#.set_move_from_dict(_dict, True)
round = move(round_dict)#.set_move_from_dict(_dict, True)
#s
sacred_fire = move(sacred_fire_dict)#.set_move_from_dict(_dict, True)
sacred_sword = move(sacred_sword_dict)#.set_move_from_dict(_dict, True)
safeguard = move(safeguard_dict)#.set_move_from_dict(_dict, True)
sand_attack = move(sand_attack_dict)#.set_move_from_dict(_dict, True)
sand_tomb = move(sand_tomb_dict)#.set_move_from_dict(_dict, True)
sandstorm = move(sandstorm_dict)#.set_move_from_dict(_dict, True)
scald = move(scald_dict)#.set_move_from_dict(_dict, True)
scary_face = move(scary_face_dict)#.set_move_from_dict(_dict, True)
scratch = move(scratch_dict).set_move_from_dict(scratch_dict, True)
screech = move(screech_dict)#.set_move_from_dict(_dict, True)
searing_shot = move(searing_shot_dict)#.set_move_from_dict(_dict, True)
secret_power = move(secret_power_dict)#.set_move_from_dict(_dict, True)
secret_sword = move(secret_sword_dict)#.set_move_from_dict(_dict, True)
seed_bomb = move(seed_bomb_dict)#.set_move_from_dict(_dict, True)
seed_flare = move(seed_flare_dict)#.set_move_from_dict(_dict, True)
seismic_toss = move(seismic_toss_dict)#.set_move_from_dict(_dict, True)
self_destruct = move(self_destruct_dict)#.set_move_from_dict(_dict, True)
shadow_ball = move(shadow_ball_dict)#.set_move_from_dict(_dict, True)
shadow_claw = move(shadow_claw_dict)#.set_move_from_dict(_dict, True)
shadow_force = move(shadow_force_dict)#.set_move_from_dict(_dict, True)
shadow_punch = move(shadow_punch_dict)#.set_move_from_dict(_dict, True)
shadow_sneak = move(shadow_sneak_dict)#.set_move_from_dict(_dict, True)
sharpen = move(sharpen_dict)#.set_move_from_dict(_dict, True)
sheer_cold = move(sheer_cold_dict)#.set_move_from_dict(_dict, True)
shell_smash = move(shell_smash_dict)#.set_move_from_dict(_dict, True)
shift_gear = move(shift_gear_dict)#.set_move_from_dict(_dict, True)
shock_wave = move(shock_wave_dict)#.set_move_from_dict(_dict, True)
signal_beam = move(signal_beam_dict)
silver_wind = move(silver_wind_dict)
simple_beam = move(simple_beam_dict)#.set_move_from_dict(_dict, True)
sing = move(sing_dict)#.set_move_from_dict(_dict, True)
sketch = move(sketch_dict)#.set_move_from_dict(_dict, True)
skull_bash = move(skull_bash_dict)#.set_move_from_dict(_dict, True)
sky_attack = move(sky_attack_dict)#.set_move_from_dict(_dict, True)
sky_drop = move(sky_drop_dict)#.set_move_from_dict(_dict, True)
sky_uppercut = move(sky_uppercut_dict)#.set_move_from_dict(_dict, True)
slack_off = move(slack_off_dict)#.set_move_from_dict(_dict, True)
slam = move(slam_dict)#.set_move_from_dict(_dict, True)
slash = move(slash_dict)#.set_move_from_dict(_dict, True)
sleep_powder = move(sleep_powder_dict)#.set_move_from_dict(_dict, True)
sleep_talk = move(sleep_talk_dict)#.set_move_from_dict(_dict, True)
sludge = move(sludge_dict)#.set_move_from_dict(_dict, True)
sludge_bomb = move(sludge_bomb_dict)#.set_move_from_dict(_dict, True)
sludge_wave = move(sludge_wave_dict)#.set_move_from_dict(_dict, True)
smack_down = move(smack_down_dict)#.set_move_from_dict(_dict, True)
smelling_salts = move(smelling_salts_dict)#.set_move_from_dict(_dict, True)
smog = move(smog_dict)#.set_move_from_dict(_dict, True)
smokescreen = move(smokescreen_dict)#.set_move_from_dict(_dict, True)
snarl = move(snarl_dict)#.set_move_from_dict(_dict, True)
snore = move(snore_dict)#.set_move_from_dict(_dict, True)
soak = move(soak_dict)#.set_move_from_dict(_dict, True)
soft_boiled = move(soft_boiled_dict)#.set_move_from_dict(_dict, True)
solar_beam = move(solar_beam_dict)#.set_move_from_dict(_dict, True)
sonic_boom = move(sonic_boom_dict)#.set_move_from_dict(_dict, True)
spacial_rend = move(spacial_rend_dict)#.set_move_from_dict(_dict, True)
spark = move(spark_dict)#.set_move_from_dict(_dict, True)
spider_web = move(spider_web_dict)#.set_move_from_dict(_dict, True)
spike_cannon = move(spike_cannon_dict)#.set_move_from_dict(_dict, True)
spikes = move(spikes_dict)#.set_move_from_dict(_dict, True)
spiky_shield = move(spiky_shield_dict)#.set_move_from_dict(_dict, True)
spit_up = move(spit_up_dict)#.set_move_from_dict(_dict, True)
spite = move(spite_dict)#.set_move_from_dict(_dict, True)
splash = move(splash_dict)#.set_move_from_dict(_dict, True)
spore = move(spore_dict)#.set_move_from_dict(_dict, True)
stealth_rock = move(stealth_rock_dict)#.set_move_from_dict(_dict, True)
steamroller = move(steamroller_dict)#.set_move_from_dict(_dict, True)
steel_wing = move(steel_wing_dict)#.set_move_from_dict(_dict, True)
sticky_web = move(sticky_web_dict)#.set_move_from_dict(_dict, True)
stockpile = move(stockpile_dict)#.set_move_from_dict(_dict, True)
stomp = move(stomp_dict)#.set_move_from_dict(_dict, True)
stone_edge = move(stone_edge_dict)#.set_move_from_dict(_dict, True)
stored_power = move(stored_power_dict)#.set_move_from_dict(_dict, True)
storm_throw = move(storm_throw_dict)#.set_move_from_dict(_dict, True)
strength = move(strength_dict)#.set_move_from_dict(_dict, True)
string_shot = move(string_shot_dict)#.set_move_from_dict(_dict, True)
struggle = move(struggle_dict).set_move_from_dict(struggle_dict, True)
struggle_bug = move(struggle_bug_dict)#.set_move_from_dict(_dict, True)
stun_spore = move(stun_spore_dict)#.set_move_from_dict(_dict, True)
submission = move(submission_dict)#.set_move_from_dict(_dict, True)
substitute = move(substitute_dict)#.set_move_from_dict(_dict, True)
sucker_punch = move(sucker_punch_dict)#.set_move_from_dict(_dict, True)
sunny_day = move(sunny_day_dict)#.set_move_from_dict(_dict, True)
super_fang = move(super_fang_dict)#.set_move_from_dict(_dict, True)
superpower = move(superpower_dict)#.set_move_from_dict(_dict, True)
supersonic = move(supersonic_dict)#.set_move_from_dict(_dict, True)
surf = move(surf_dict)#.set_move_from_dict(_dict, True)
swagger = move(swagger_dict)#.set_move_from_dict(_dict, True)
swallow = move(swallow_dict)#.set_move_from_dict(_dict, True)
sweet_kiss = move(sweet_kiss_dict)#.set_move_from_dict(_dict, True)
sweet_scent = move(sweet_scent_dict)#.set_move_from_dict(_dict, True)
swift = move(swift_dict)#.set_move_from_dict(_dict, True)
switcheroo = move(switcheroo_dict)#.set_move_from_dict(_dict, True)
swords_dance = move(swords_dance_dict)#.set_move_from_dict(_dict, True)
synchronoise = move(synchronoise_dict)#.set_move_from_dict(_dict, True)
synthesis = move(synthesis_dict)#.set_move_from_dict(_dict, True)
#t
tackle = move(tackle_dict)
tail_glow = move(tail_glow_dict)#.set_move_from_dict(_dict, True)
tail_slap = move(tail_slap_dict)#.set_move_from_dict(_dict, True)
tail_whip = move(tail_whip_dict)
tailwind = move(tailwind_dict)#.set_move_from_dict(_dict, True)
take_down = move(take_down_dict)#.set_move_from_dict(_dict, True)
taunt = move(taunt_dict)#.set_move_from_dict(_dict, True)
techno_blast = move(techno_blast_dict)#.set_move_from_dict(_dict, True)
teeter_dance = move(teeter_dance_dict)#.set_move_from_dict(_dict, True)
telekinesis = move(telekinesis_dict)#.set_move_from_dict(_dict, True)
teleport = move(teleport_dict)#.set_move_from_dict(_dict, True)
thief = move(thief_dict)#.set_move_from_dict(_dict, True)
thousand_arrows = move(thousand_arrows_dict)#.set_move_from_dict(_dict, True)
thousand_waves = move(thousand_waves_dict)#.set_move_from_dict(_dict, True)
thrash = move(thrash_dict)#.set_move_from_dict(_dict, True)
thunder = move(thunder_dict)#.set_move_from_dict(_dict, True)
thunder_fang = move(thunder_fang_dict)#.set_move_from_dict(_dict, True)
thunder_punch = move(thunder_punch_dict)#.set_move_from_dict(_dict, True)
thunder_shock = move(thunder_shock_dict)
thunder_wave = move(thunder_wave_dict)#.set_move_from_dict(_dict, True)
thunderbolt = move(thunderbolt_dict)#.set_move_from_dict(_dict, True)
tickle = move(tickle_dict)#.set_move_from_dict(_dict, True)
topsy_turvy = move(topsy_turvy_dict)#.set_move_from_dict(_dict, True)
torment = move(torment_dict)#.set_move_from_dict(_dict, True)
toxic = move(toxic_dict)#.set_move_from_dict(_dict, True)
toxic_spikes = move(toxic_spikes_dict)#.set_move_from_dict(_dict, True)
transform = move(transform_dict)#.set_move_from_dict(_dict, True)
tri_attack = move(tri_attack_dict)#.set_move_from_dict(_dict, True)
trick = move(trick_dict)#.set_move_from_dict(_dict, True)
trick_or_treat = move(trick_or_treat_dict)#.set_move_from_dict(_dict, True)
triple_kick = move(triple_kick_dict)#.set_move_from_dict(_dict, True)
trump_card = move(trump_card_dict)#.set_move_from_dict(_dict, True)
twineedle = move(twineedle_dict)#.set_move_from_dict(_dict, True)
twister = move(twister_dict)#.set_move_from_dict(_dict, True)
#u
u_turn = move(u_turn_dict)#.set_move_from_dict(_dict, True)
uproar = move(uproar_dict)#.set_move_from_dict(_dict, True)
#v
v_create = move(v_create_dict)#.set_move_from_dict(_dict, True)
vacuum_wave = move(vacuum_wave_dict)#.set_move_from_dict(_dict, True)
venom_drench = move(venom_drench_dict)#.set_move_from_dict(_dict, True)
venoshock = move(venoshock_dict)#.set_move_from_dict(_dict, True)
vice_grip = move(vice_grip_dict)#.set_move_from_dict(_dict, True)
vine_whip = move(vine_whip_dict)#.set_move_from_dict(_dict, True)
vital_throw = move(vital_throw_dict)#.set_move_from_dict(_dict, True)
volt_switch = move(volt_switch_dict)#.set_move_from_dict(_dict, True)
volt_tackle = move(volt_tackle_dict)#.set_move_from_dict(_dict, True)
#w
wake_up_slap = move(wake_up_slap_dict)#.set_move_from_dict(_dict, True)
water_gun = move(water_gun_dict)#.set_move_from_dict(_dict, True)
water_pledge = move(water_pledge_dict)#.set_move_from_dict(_dict, True)
water_pulse = move(water_pulse_dict)#.set_move_from_dict(_dict, True)
water_shuriken = move(water_shuriken_dict)#.set_move_from_dict(_dict, True)
water_sport = move(water_sport_dict)#.set_move_from_dict(_dict, True)
water_spout = move(water_spout_dict)#.set_move_from_dict(_dict, True)
waterfall = move(waterfall_dict)#.set_move_from_dict(_dict, True)
weather_ball = move(weather_ball_dict)#.set_move_from_dict(_dict, True)
whirlwind = move(whirlwind_dict)#.set_move_from_dict(_dict, True)
whirlpool = move(whirlpool_dict)#.set_move_from_dict(_dict, True)
wide_guard = move(wide_guard_dict)#.set_move_from_dict(_dict, True)
wild_charge = move(wild_charge_dict)#.set_move_from_dict(_dict, True)
will_o_wisp = move(will_o_wisp_dict)#.set_move_from_dict(_dict, True)
wing_attack = move(wing_attack_dict)#.set_move_from_dict(_dict, True)
wish = move(wish_dict)#.set_move_from_dict(_dict, True)
withdraw = move(withdraw_dict)#.set_move_from_dict(_dict, True)
wonder_room = move(wonder_room_dict)#.set_move_from_dict(_dict, True)
wood_hammer = move(wood_hammer_dict)#.set_move_from_dict(_dict, True)
work_up = move(work_up_dict)#.set_move_from_dict(_dict, True)
worry_seed = move(worry_seed_dict)#.set_move_from_dict(_dict, True)
wrap = move(wrap_dict)#.set_move_from_dict(_dict, True)
wring_out = move(wring_out_dict)#.set_move_from_dict(_dict, True)
#x
x_scissor = move(x_scissor_dict)#.set_move_from_dict(_dict, True)
#y
yawn = move(yawn_dict)#.set_move_from_dict(_dict, True)
#z
zap_cannon = move(zap_cannon_dict)#.set_move_from_dict(_dict, True)
zen_headbutt = move(zen_headbutt_dict)#.set_move_from_dict(_dict, True)
#
#
# DEBUG MOVES
Stun_dict = {
'name': "Stun",
'type': constants.type_dark,
'category': constants.move_category_physical,
'effects': ["{} {} on {}".format(constants.inflict, constants.status_flinch, constants.pkm_foe)],
'description': "",
'power': 40,
'accuracy': 100,
'pp': 15
}
Sleeper_dict = {
'name': "Sleeper",
'type': constants.type_psychic,
'category': constants.move_category_status,
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_sleep, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
Freeze_dict = {
'name': "Freeze",
'type': constants.type_ice,
'category': constants.move_category_status,
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_freeze, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
Poison_dict = {
'name': "Poison",
'type': constants.type_poison,
'category': constants.move_category_status,
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_poison, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
Badly_Poison_dict = {
'name': "Badly Poison",
'type': constants.type_poison,
'category': constants.move_category_status,
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_badly_poison, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
Burn_dict = {
'name': "Burn",
'type': constants.type_fire,
'category': constants.move_category_status,
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_burn, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
Paralyze_dict = {
'name': "Paralyze",
'type': constants.type_electric,
'category': constants.move_category_status,
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_paralysis, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 100,
'pp': 15
}
Confuse_dict = {
'name': "Confuse",
'type': constants.type_ghost,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_confusion, constants.pkm_foe)],
'power': None,
'accuracy': 100,
'pp': 15
}
Infatuate_dict = {
'name': "Infatuate",
'type': constants.type_ghost,
'category': constants.move_category_status,
'description': "",
'effects': ["{} {} on {} ".format(constants.inflict, constants.status_attracted, constants.pkm_foe)],
'power': None,
'accuracy': 100,
'pp': 15
}
Trapper_dict = {
'name': "Trapper",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.inflict, constants.status_partially_trapped, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 90,
'pp': 20
}
Entrapper_dict = {
'name': "Entrapper",
'type': constants.type_normal,
'category': constants.move_category_status,
'effects': ["{} {} {}".format(constants.inflict, constants.status_partially_trapped, constants.pkm_foe)],
'description': "",
'power': None,
'accuracy': 90,
'pp': 20
}
#
Stun = move(Stun_dict)
Sleep = move(Sleeper_dict)
Freeze = move(Freeze_dict)
Poison = move(Poison_dict)
Badly_poison = move(Badly_Poison_dict)
Burn = move(Burn_dict)
Paralyze = move(Paralyze_dict)
Confuse = move(Confuse_dict)
Infatuate = move(Infatuate_dict)
Trapper = move(Trapper_dict)
Entrapper = move(Entrapper_dict)
#
#
#