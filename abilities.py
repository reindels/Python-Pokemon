from constants import constants
from ability_dicts import *
class ability():
    def __init__(self, ad=None):
        self.name = constants.empty
        self.enabled = True
        self.generation_introduced = 3
        self.effect = 'No Effect'
        self.effect_description = "This text describes an abilty."
        self.out_of_battle_effect = "No Effect"
        self.out_of_battle_effect_description = "This text describes an abilty outside of battle."
        if ad is not None:
            self._set(ad=ad)
    def _set(self, ad=None):
        if ad is None:
            return
        self.name = ad.get('name')
        self.generation_introduced = ad.get('generation')
        self.effect = ad.get('effect')
        self.effect_description = ad.get('effect description')
        self.out_of_battle_effect = ad.get('oob effect')
        self.out_of_battle_effect_description = ad.get('oob effect description')
    def __str__(self):
        return self.name + ", gen: " + str(self.generation_introduced)
    def copy(self):
        new_abil = ability()
        new_abil.name = self.name
        new_abil.generation_introduced = self.generation_introduced
        new_abil.effect = self.effect
        new_abil.effect_description = self.effect_description
        new_abil.out_of_battle_effect = self.out_of_battle_effect
        new_abil.out_of_battle_effect_description = self.out_of_battle_effect_description
        return new_abil
#
# ability = ability(ad=_dict)
#a,
adaptability = ability(ad=adaptability_dict)
aerilate = ability(ad=aerilate_dict)
aftermath = ability(ad=aftermath_dict)
air_lock = ability(ad=air_lock_dict)
analytic = ability(ad=analytic_dict)
anger_point = ability(ad=anger_point_dict)
anticipation = ability(ad=anticipation_dict)
arena_trap = ability(ad=arena_trap_dict)
aroma_veil = ability(ad=aroma_veil_dict)
aura_break = ability(ad=aura_break_dict)
#b,
bad_dreams = ability(ad=bad_dreams_dict)
battle_armor = ability(ad=battle_armor_dict)
big_pecks = ability(ad=big_pecks_dict)
blaze = ability(ad=blaze_dict)
bulletproof = ability(ad=bulletproof_dict)
#c,
cheek_pouch = ability(ad=cheek_pouch_dict)
chlorophyll = ability(ad=chlorophyll_dict)
clear_body = ability(ad=clear_body_dict)
cloud_nine = ability(ad=cloud_nine_dict)
color_change = ability(ad=color_change_dict)
competitive = ability(ad=competitive_dict)
compound_eyes = ability(ad=compound_eyes_dict)
contrary = ability(ad=contrary_dict)
cursed_body = ability(ad=cursed_body_dict)
cute_charm = ability(ad=cute_charm_dict)
#d,
damp = ability(ad=damp_dict)
dark_aura = ability(ad=dark_aura_dict)
defeatist = ability(ad=defeatist_dict)
defiant = ability(ad=defiant_dict)
delta_stream = ability(ad=delta_stream_dict)
desolate_land = ability(ad=desolate_land_dict)
download = ability(ad=download_dict)
drizzle = ability(ad=drizzle_dict)
drought = ability(ad=drought_dict)
dry_skin = ability(ad=dry_skin_dict)
#e,
early_bird = ability(ad=early_bird_dict)
effect_spore = ability(ad=effect_spore_dict)
#f,
fairy_aura = ability(ad=fairy_aura_dict)
filter = ability(ad=filter_dict)
flame_body = ability(ad=flame_body_dict)
flare_boost = ability(ad=flare_boost_dict)
flash_fire = ability(ad=flash_fire_dict)
flower_gift = ability(ad=flower_gift_dict)
flower_veil = ability(ad=flower_veil_dict)
forecast = ability(ad=forecast_dict)
forewarn = ability(ad=forewarn_dict)
friend_guard = ability(ad=friend_guard_dict)
frisk = ability(ad=frisk_dict)
fur_coat = ability(ad=fur_coat_dict)
#g,
gale_wings = ability(ad=gale_wings_dict)
gluttony = ability(ad=gluttony_dict)
gooey = ability(ad=gooey_dict)
grass_pelt = ability(ad=grass_pelt_dict)
guts = ability(ad=guts_dict)
#h,
harvest = ability(ad=harvest_dict)
healer = ability(ad=healer_dict)
heatproof = ability(ad=heatproof_dict)
heavy_metal = ability(ad=heavy_metal_dict)
honey_gather = ability(ad=honey_gather_dict)
huge_power = ability(ad=huge_power_dict)
hustle = ability(ad=hustle_dict)
hydration = ability(ad=hydration_dict)
hyper_cutter = ability(ad=hyper_cutter_dict)
#i,
ice_body = ability(ad=ice_body_dict)
illuminate = ability(ad=illuminate_dict)
illusion = ability(ad=illusion_dict)
immunity = ability(ad=immunity_dict)
imposter = ability(ad=imposter_dict)
infiltrator = ability(ad=infiltrator_dict)
inner_focus = ability(ad=inner_focus_dict)
insomnia = ability(ad=insomnia_dict)
intimidate = ability(ad=intimidate_dict)
iron_barbs = ability(ad=iron_barbs_dict)
iron_fist = ability(ad=iron_fist_dict)
#j,
justified = ability(ad=justified_dict)
#k,
keen_eye = ability(ad=keen_eye_dict)
klutz = ability(ad=klutz_dict)
#l,
leaf_guard = ability(ad=leaf_guard_dict)
levitate = ability(ad=levitate_dict)
light_metal = ability(ad=light_metal_dict)
lighting_rod = ability(ad=lighting_rod_dict)
limber = ability(ad=limber_dict)
liquid_ooze = ability(ad=liquid_ooze_dict)
#m,
magic_bounce = ability(ad=magic_bounce_dict)
magic_guard = ability(ad=magic_guard_dict)
magician = ability(ad=magician_dict)
magma_armor = ability(ad=magma_armor_dict)
magnetic_pull = ability(ad=magnetic_pull_dict)
marvel_scale = ability(ad=marvel_scale_dict)
mega_launcher = ability(ad=mega_launcher_dict)
minus = ability(ad=minus_dict)
mold_breaker = ability(ad=mold_breaker_dict)
moody = ability(ad=moody_dict)
motor_drive = ability(ad=motor_drive_dict)
moxie = ability(ad=moxie_dict)
multiscale = ability(ad=multiscale_dict)
multitype = ability(ad=multitype_dict)
mummy = ability(ad=mummy_dict)
#n,
natural_cure = ability(ad=natural_cure_dict)
no_guard = ability(ad=no_guard_dict)
normalize = ability(ad=normalize_dict)
#o,
oblivious = ability(ad=oblivious_dict)
overcoat = ability(ad=overcoat_dict)
overgrow = ability(ad=overgrow_dict)
own_tempo = ability(ad=own_tempo_dict)
#p,
parental_bond = ability(ad=parental_bond_dict)
pickpocket = ability(ad=pickpocket_dict)
pickup = ability(ad=pickup_dict)
pixilate = ability(ad=pixilate_dict)
plus = ability(ad=plus_dict)
poison_heal = ability(ad=poison_heal_dict)
poison_point = ability(ad=poison_point_dict)
poison_touch = ability(ad=poison_touch_dict)
prankster = ability(ad=prankster_dict)
pressure = ability(ad=pressure_dict)
primordial_sea = ability(ad=primordial_sea_dict)
protean = ability(ad=protean_dict)
pure_power = ability(ad=pure_power_dict)
#q,
quick_feet = ability(ad=quick_feet_dict)
#r,
rain_dish = ability(ad=rain_dish_dict)
rattled = ability(ad=rattled_dict)
reckless = ability(ad=reckless_dict)
refrigerate = ability(ad=refrigerate_dict)
regenerator = ability(ad=regenerator_dict)
rivalry = ability(ad=rivalry_dict)
rock_head = ability(ad=rock_head_dict)
rough_skin = ability(ad=rough_skin_dict)
run_away = ability(ad=run_away_dict)
#s,
sand_force = ability(ad=sand_force_dict)
sand_rush = ability(ad=sand_rush_dict)
sand_stream = ability(ad=sand_stream_dict)
sand_veil = ability(ad=sand_veil_dict)
sap_sipper = ability(ad=sap_sipper_dict)
scrappy = ability(ad=scrappy_dict)
serene_grace = ability(ad=serene_grace_dict)
shadow_tag = ability(ad=shadow_tag_dict)
shed_skin = ability(ad=shed_skin_dict)
sheer_force = ability(ad=sheer_force_dict)
shell_armor = ability(ad=shell_armor_dict)
shield_dust = ability(ad=shield_dust_dict)
simple = ability(ad=simple_dict)
skill_link = ability(ad=skill_link_dict)
slow_start = ability(ad=slow_start_dict)
sniper = ability(ad=sniper_dict)
snow_cloak = ability(ad=snow_cloak_dict)
snow_warning = ability(ad=snow_warning_dict)
solar_power = ability(ad=solar_power_dict)
solid_rock = ability(ad=solid_rock_dict)
soundproof = ability(ad=soundproof_dict)
speed_boost = ability(ad=speed_boost_dict)
stall = ability(ad=stall_dict)
stance_change = ability(ad=stance_change_dict)
static = ability(ad=static_dict)
steadfast = ability(ad=steadfast_dict)
stench = ability(ad=stench_dict)
sticky_hold = ability(ad=sticky_hold_dict)
storm_drain = ability(ad=storm_drain_dict)
strong_jaw = ability(ad=strong_jaw_dict)
sturdy = ability(ad=sturdy_dict)
suction_cups = ability(ad=suction_cups_dict)
super_luck = ability(ad=super_luck_dict)
swarm = ability(ad=swarm_dict)
sweet_veil = ability(ad=sweet_veil_dict)
swift_swim = ability(ad=swift_swim_dict)
symbiosis = ability(ad=symbiosis_dict)
synchronize = ability(ad=synchronize_dict)
#t,
tangled_feet = ability(ad=tangled_feet_dict)
technician = ability(ad=technician_dict)
telepathy = ability(ad=telepathy_dict)
teravolt = ability(ad=teravolt_dict)
thick_fat = ability(ad=thick_fat_dict)
tinted_lens = ability(ad=tinted_lens_dict)
torrent = ability(ad=torrent_dict)
tough_claws = ability(ad=tough_claws_dict)
toxic_boost = ability(ad=toxic_boost_dict)
trace = ability(ad=trace_dict)
traunt = ability(ad=traunt_dict)
turboblaze = ability(ad=turboblaze_dict)
#u,
unaware = ability(ad=unaware_dict)
unburden = ability(ad=unburden_dict)
unnerve = ability(ad=unnerve_dict)
#v,
victory_star = ability(ad=victory_star_dict)
vital_spirit = ability(ad=vital_spirit_dict)
volt_absorb = ability(ad=volt_absorb_dict)
#w,
water_absorb = ability(ad=water_absorb_dict)
water_veil = ability(ad=water_veil_dict)
weak_armor = ability(ad=weak_armor_dict)
white_smoke = ability(ad=white_smoke_dict)
wonder_guard = ability(ad=wonder_guard_dict)
wonder_skin = ability(ad=wonder_skin_dict)
#x,
#ability = ability(ad=_dict)
#y,
#ability = ability(ad=_dict)
#z
zen_mode = ability(ad=zen_mode_dict)


#
#