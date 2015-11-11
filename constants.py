#
from pokemon_type import pokemon_type

class constants():
    prompt = ">>>"
    empty = ' --- '
    
    #
    crit_damage_multiplier = 1.5
    #
    btl_opt_attack = "Attack"
    btl_opt_pokemon = "Pokemon"
    btl_opt_switch = "Switch"
    btl_opt_items = "Items"
    btl_opt_call = "Call"
    btl_opt_flee = "Flee"
    wild_pokemon_options = [btl_opt_attack, btl_opt_flee]
    trainer_battle_options = [btl_opt_attack, btl_opt_pokemon, btl_opt_items,  btl_opt_call]
    encounter_options = [btl_opt_attack, btl_opt_pokemon, btl_opt_items,  btl_opt_call, btl_opt_flee]
    priority_list_keys = ['8','7','6','5','4','3','2','1','0','-1','-2','-3','-4','-5','-6','-7']
    #battle_priority = {'8': [], '7': [], '6': [], '5': [], '4': [], '3': [], '2': [], '1': [], '0': [], '-1': [], '-2': [], '-3': [], '-4': [], '-5': [], '-6': [], '-7': []}
    #
    custom_region = ''
    regions = ['National', 'Local', custom_region, 'Kanto', 'Johto', 'Hoenn', 'Orre', 'Sinnoh', 'Unova', 'Kalos']
    base_region_number = {'National': 0, custom_region: 0, 'Kanto': 0, 'Johto': 0, 'Hoenn': 0, 'Orre': 0, 'Sinnoh': 0, 'Unova': 0, 'Kalos': 0}
    base_prize_money = 'base prize money'
    age_inexperienced = "Youth"
    age_young = "Young"
    age_veteran = "age_"
    age_experienced = "age_"
    age_middle_age = "age_"
    age_seasoned = "age_"
    age_ = "age_"
    #
    divider_small = '----------------------------------\n' # 34
    divider_large = '------------------------------------------------\n' # 48
    hit_bar = 20
    max_level = 100
    #
    battle_type_unoffical_singles = 'Unofficial Singles' # all 6 pokemon
    battle_type_wild_pokemon_encounter = 'Wild Pokemon Encounter' # all 6 pokemon for the trainer
    #Later
    battle_type_unoffical_doubles = 'Unofficial Doubles' # all 6 pokemon, 2 pokemon out per trainer
    battle_type_offical_singles = 'Official Singles' # 3 pokemon per trainer
    battle_type_offical_doubles = 'Official Doubles' # 4 pokemon per trainer
    battle_type_offical_singles = 'Wild Horde Encounter' # all 6 pokemon for the trainer with, 2-4 pokemon on the field on each side 
    #
    stage_accuracy = 'accuracy stage'
    stage_evasion = 'evasion stage'
    stage_critical = 'critical stage'
    base_hp = 'base hp'
    iv_hp = 'hp iv'
    ev_hp = 'hp ev'
    base_attack = 'base attack'
    iv_attack = 'attack iv'
    ev_attack = 'attack ev'
    nature_attack = 'attack nature'
    stage_attack = 'attack stage'
    
    base_defense = 'base defense'
    iv_defense = 'defense iv'
    ev_defense = 'defense ev'
    nature_defense = 'defense nature'
    stage_defense = 'defense stage'
    
    base_special_attack = 'base special attack'
    iv_special_attack = 'special attack iv'
    ev_special_attack = 'special attack ev'
    nature_special_attack = 'special attack nature'
    stage_special_attack = 'special attack stage'
    
    base_special_defense = 'base special defense'
    iv_special_defense = 'special defense iv'
    ev_special_defense = 'special defense ev'
    nature_special_defense = 'special defense nature'
    stage_special_defense = 'special defense stage'
    
    base_speed = 'base speed'
    iv_speed = 'speed iv'
    ev_speed = 'speed ev'
    nature_speed = 'speed nature'
    stage_speed = 'speed stage'
    hold_item = 'hold item'
    
    all_stat_format = {
    stage_accuracy: 0, stage_evasion: 0, stage_critical: 0,
    base_hp: 0, iv_hp: 0, ev_hp: 0,
    base_attack: 0, iv_attack: 0, ev_attack: 0, nature_attack: 0, stage_attack: 0,
    base_defense: 0, iv_defense: 0, ev_defense: 0, nature_defense: 0, stage_defense: 0,
    base_special_attack: 0, iv_special_attack: 0, ev_special_attack: 0, nature_special_attack: 0, stage_special_attack: 0,
    base_special_defense: 0, iv_special_defense: 0, ev_special_defense: 0, nature_special_defense: 0, stage_special_defense: 0,
    base_speed: 0, iv_speed: 0, ev_speed: 0, nature_speed: 0, stage_speed: 0
    }
    ev_yield_format = {
    'hp ev': 0, 'attack ev': 0, 'defense ev': 0, 
    'special attack ev': 0, 'special defense ev': 0, 'speed ev': 0
    }
    pokedex_entries = {'generation 1': empty, 'generation 2': empty, 'generation 3': empty, 
    'generation 4': empty, 'generation 5': empty, 'generation 6': empty, 
    'generation x': empty}
    #
    nat_lonely = 'Lonely'
    nat_brave = 'Brave' 
    nat_adament = 'Adamant' 
    nat_naughty = 'Naughty'
    nat_bold = 'Bold' 
    nat_relaxed = 'Relaxed' 
    nat_docile = 'Docile'#
    nat_impish = 'Impish' 
    nat_lax = 'Lax'
    nat_modest = 'Modest' 
    nat_mild = 'Mild' 
    nat_quiet = 'Quiet' 
    nat_rash = 'Rash'
    nat_quirky = 'Quirky'#
    nat_timid = 'Timid' 
    nat_hasty = 'Hasty' 
    nat_jolly = 'Jolly' 
    nat_naive = 'Naive'
    nat_calm = 'Calm' 
    nat_bashful = 'Bashful'#
    nat_gentle = 'Gentle' 
    nat_sassy = 'Sassy' 
    nat_carful = 'Careful'
    nat_hardy = 'Hardy'#
    #
    base_happiness = 70
    low_happiness = 35
    max_happiness = 255
    #
    male = 'Male'
    female = 'Female'
    neutor = 'Neutor'
    genderless = 'Genderless'
    all_male = [100.0,0.0]
    mostly_male = [75,25]
    equal_male_female = [50.0,50.0]
    mostly_female = [25,75]
    all_female = [100.0,0.0]
    neutral = [0.0,0.0]
    # MOVE EFFECTS
    move_category_physical = "Physical"
    move_category_special = "Special"
    move_category_status = "Status"
    # MOVE EFFECTS
    high_crit_ratio = "High critical hit ratio."
    assign_priority = "Assign Priority"
    first_turn_only = "First Turn Only"
    recoil_damage = "User receives recoil damage."
    swithces = "Switches"
    pkm_all_other = "All Other Pokemon"
    pkm_all_in_party = "All Party Pokemon"
    pkm_all_allies = "All Allies"
    weight = "Weight"
    pkm_foe = 'Foe'
    pkm_ally = 'Ally'
    pkm_self = 'User'
    reduces = 'Reduces'
    increases = 'Increases'
    
    by_1_stages = '1 Stage'
    by_2_stages = '2 Stages'
    by_3_stages = '3 Stages'
    by_4_stages = '4 Stages'
    by_5_stages = '5 Stages'
    by_6_stages = '6 Stages'
    by_1_stage = '1 Stage'
    by_2_stage = '2 Stages'
    by_3_stage = '3 Stages'
    by_4_stage = '4 Stages'
    by_5_stage = '5 Stages'
    by_6_stage = '6 Stages'
    
    random_stat = "Random Stat"
    all_stats = "All Stats"
    attack = 'Attack'
    defense = 'Defense'
    speed = 'Speed'
    special_attack = 'Special Attack'
    special_defense = 'Special Defense'
    accuracy = 'Accuracy'
    evasion = 'Evasion'
    crit_ratio = "Critical hit ratio"
    weather = "Weather"
    w_clear = "Normal"
    w_sunny = "Sunny"
    w_intense_sun = " Intense Sun"
    w_rainy = "Rain"
    w_intense_rain = "Intense Rain"
    w_sandstorm = "Sandstorm"
    w_hail = "Hail"
    w_windy = "Wind"
    w_fog = "Fog"
    
    recovers = 'Recover'
    hit_points = 'Hit Points'
    damage_delt = "Damage Delt"
    ignores = "Ignores"
    full = "Full"
    three_quarters = "Three-Quarters"
    two_thirds = "Two-Thirds"
    half = "Half"
    third = "Third"
    quarter = "Quarter"
    eighth = "Eighth"
    sixteenth = "Sixteenth"
    health = 'Health'
    remove = 'Remove'
    status_infliction = 'Status Conditions'
    reset_status = 'Reset Status'
    inflict = 'Inflict'
    set_amount_of_damage = "Set Damage"
    bestow = 'Bestow'
    status_all_negative = "All Negative"
    switches_opponent = "Switches Opponent"
    switches_ally = "Switches Ally"
    transfer_stats_changes = "Transfer Stat Changes"
    doubles_if_hit = "Power doubles if user took damage first"
    if_damaged = "If Damaged"
    must_have_status = "Must Have Status"
    doubles = "Doubles"
    power = "Power"
    priority = "Priority"
    switches = "Switches"
    stores_energy = "Stores Energy"
    one_hit_ko = "One-Hit-KO"
    remove_stat_changes = "Remove Stat Changes"
    disables_move = "Disables Move"
    always_crit = "Always results in a critical hit."
    trap_effects = "Trap Effects"
    reverse_stats = "Reverse Stats"
    repeat_then_become_confused = "attacks for 2-3 turns but then becomes confused."# User attacks for 2-3 turns but then becomes confused.
    
    #Negative status
    status_paralysis = 'Paralysis' # {constants.status_paralysis: '25% chance to Fail Attack'} # chance to not attack
    status_paralysis_chance = 25
    plz = 'PLZ'
    status_poison = 'Poison' # {constants.status_poison: none}
    status_badly_poison = 'Badly Poisoned' # {constants.status_badly_poison: 1} # damage multiplier, increases per turn
    psn = 'PSN'
    status_sleep = 'Sleep' # {constants.status_sleep: [5-1]} # turns left to effect
    slp = 'SLP'
    status_burn = 'Burn' # {constants.status_burn: None}
    brn = 'BRN'
    status_freeze = 'Freeze' # {constants.status_freeze: '20% chance to Remove'} # chance to self remove
    status_freeze_chance = 20
    frz = 'FRZ'
    status_flinch = 'Flinch' # {constants.status_flinch: 0} # turns left to effect, skips a pokemon's turn
    status_confusion = 'Confusion' # {constants.status_confusion: '25% chance to Hurt Self'} # chance to attack self
    status_confusion_chance = 25
    status_cursed = 'Curse' # {constants.status_cursed : None}
    status_attracted = 'Infatuation' # {constants.status_attracted: '50% chance to Fail Attack'}
    status_attracted_chance = 50
    status_trapped = "Trapped" # {constants.status_trapped: None} # cannot retreat or switch, unlessa move permits
    status_recoil_damage = "Recoil Damage" # not a status, but deals damage to self when hits foe
    status_hurt_self = "Hurt Self" # not a status, but a result of confusion , deals damage to self
    status_perish_song = "Perish Song" # {constants.status_perish_song: [4-0]} # if a pokemon is still out when this counter reaches 0, it faints at the end of the round
    status_heal_block = "Heal Block" # {constants.status_heal_block: None} #
    status_partially_trapped = "Partially Trapped" # {constants.status_partially_trapped: [2-5], 'move': "name"} # cannot escape, usually takes damage
    status_leech_seed = "Leech Seed" # {constants.status_leech_seed: None} #
    status_taunted = "Taunted" # {constants.status_taunted: None} #
    status_levitation = "Levitation" # {constants.status_levitation: None} # immune to ground type attacks, hazards, and subject to garunteed hits (evasion is lowest value).
    status_torment = "Torment" # {constants.status_torment: None} # cannot use the same move twice in a row
    status_embargo = "Embargo" # {constants.status_embargo: None}
    status_encore = "Encore" # {constants.status_encore: move, 'turns': 3}
    status_mist = "Mist" # {constants.status_encore: move, 'turns': 3}
    status_recharge = "Recharging"
    status_user_faints = "User faints."
    status_fainted = 'Fainted' # {constants.status_fainted: None}
    # Positive status conditions
    status_safeguard = "Safeguard" # {constants.status_safeguard: 5}
    status_reflect = "Reflect" # {constants.status_reflect: 5}
    status_light_screen = "Light Screen" # {constants.status_light_screen: 5}
    status_aqua_ring = "Aqua Ring" # {constants.status_aqua_ring: None}
    status_protected = "Protected" # {constants.status_protected: None} # cannot take damage
    status_bracing = "Bracing" # {constants.status_bracing: None} # cannot faint, leaving only 1 hp left
    status_charging = "Charging" # {constants.status_charging: "Move Name"} # does not attack this round
    status_focusing = "Focusing" # {constants.status_focusing: "Move Name"} # does not attack this round, dealing damage will disrupt attack
    #? status_glowing = "Glowing" # {constants.status_glowing: None} charging for sky attack
    #? status_whipping_up_wind = "Whipping up a Whirwind" # {constants.status_whipping_up_wind: None} charging for razor wind
    #? status_taking_sunlight = "Taking in Sunlight" # {constants.status_taking_sunlight: None} charging for solar beam
    status_bide = "Bide" # {constants.status_bide: 0, 'turns': 2}
    status_rooted = "Rooted" # {constants.status_rooted: None}
    status_magic_coat = "Magic Coat" # {constants.status_magic_coat: None}
    status_magnetic_levitation = "Magnetic Levitation" # {constants.status_magnetic_levitation: None} # immune to ground type attacks, hazards
    status_minimized = "Minimized" # {constants.status_minimized: None}, incraese users evasion, takes double damage from trampling moves
    status_recharging = "Recharging" # {constants.status_recharging: 1} # pokemon cannot attack the next round
    status_digging = "Digging" # {constants.: None}
    status_flying = "Flying" # {constants.status_flying: 0}
    status_diving = "Diving" # {constants.: None}
    status_shadow_force = "Shadow Force" # {constants.status_shadow_force: None}
    status_semi_invulnerable = "Semi-invulnerable" # {constants.status_semi_invulnerable: None}, most moves will not affect the user for a turn
    status_substituted = "Substituted" # {constants.: None}
    status_taking_aim = "Taking Aim" # {constants.: None}
    status_withdraw = "Withdrawn" # {constants.status_withdraw: None}
    status_defense_curl = "Defense Curl" # {constants.status_defense_curl: None}
    status_charged = "Charged" # {constants.status_charged: None}
    status_destiny_bond = "Destiny Bond" #{constants.status_charged: None}
    status_rage = "Rage" #{constants.status_rage: 0}
    status_stockpile = "Stockpile" # {constants.status_stockpile: 1}
    status_tailwind = "Tailwind" # {constants.status_tailwind: None, 'turns': 4}
    status_normal = 'Normal' # {constants.status_normal: None}
    status_trick_room = "Trick Room" # {constants.status_trick_room: None, 'turns': 5}
    status_wide_guard = "Wide Gaurd" # {constants.status_wide_guard: None}
    status_nightmare = "Nightmare" # {constants.status_nightmare: None}
    #Item Types
    item_type_medicine = 'Medicine'
    item_type_vitamin = 'Vitamin'
    item_type_berry = 'Berry'
    item_type_key_item = 'Key Item'
    item_type_poke_ball = 'Poke Ball'
    item_type_tm_hm = 'TM HM'
    item_type_held_item = 'Held Item'
    item_type_general = 'General'
    item_type_mail = 'Mail'
    # if I want to use size to limit nventory
    item_size_diminutive = 1 # hold Many in your hand, < 1 inch^3
    item_size_tiny = 2 # hold several in your hand, ~ 1 inch^3
    item_size_small = 4 # hold one in your hand, ~ 2-8 inch^3
    item_size_medium = 8 # hold with two hands, ~ 8-16 inch^3
    item_size_large = 16 # 
    item_size_very_large = 32 # 
    item_size_hefty = 64 # 
    item_size_massive = 128 # impossible to hold in an inventory
    item_weight_berry = 1.0/10 # 
    item_weight_poke_block = 1.0/5 # 
    #item_weight_ = 0 # 

    #
    max_party_size = 6
    max_moves = 4
    must_delete_move_first = "Must delete move first."
    # EXP Growth rates
    growthrate_erratic = 'Erratic'
    growthrate_fast = 'Fast'
    growthrate_medium_fast = 'Medium Fast'
    growthrate_medium_slow = 'Medium Slow'
    growthrate_slow = 'Slow'
    growthrate_fluctuating = 'Fluctuating'
    #
    # MAP CONSTANTS
    #directions
    north = "North"
    south = "South"
    east = "East"
    west = "West"
    # 
    #terrain Types
    city = "City"
    town = "Town"
    village = "Village"
    field = "Field"
    forest = "Forest"
    woods = "Woods"
    swamp = "Swamp"
    desert = "Desert"
    mountain = "Mountain"
    volcano = "Volcano"
    cave = "Cave"
    cavern = "Cavern"
    lake = "Lake"
    ocean = "Ocean"
    ocean_floor = "Ocean"
    river = "River"

    # route types
    field_route = "Field Route"
    forest_route = "Forest Route"
    mountain_route = "Mountain Route"
    ocean_floor_route = "Ocean Floor Route"
    rural_route = "Rural Route"
    urban_route = "Urban Route"
    valley_route = "Valley Route"
    water_route = "Water Route"
    #BUILDINGS - Can enter in and out of        # typical rooms
    house = "House"                             # enterance, hall, kitchen, bedroom, livingroom, stairs, 
    school = "School"                           # enterance, hall, cafeteria, classroom, office, storeroom, stairs, elevator
    office_building = "Office Building"         # enterance, hall, office, breakroom, storeroom, stairs, elevator, 
    museum = "Museum"                           # enterance, hall, frontdesk, hall, exhibit, office, library, cafeteria, shop, storeroom, stairs, elevator 
    lab = "Laboratory"                          # enterance, hall, library, cafeteria, lab, office, storeroom, pokemoncenter, stairs, elevator
    pkm_stadium = "Pokemon Stadium"             # enterance, hall, frontdesk, shop, pokemoncenter, waitingroom, stadium, stands, storeroom, stairs, elevator
    pkm_gym = "Pokemon Gym"                     # enterance, hall, stadium, stands, puzzle, stairs, elevator
    pkm_center = "Pokemon Center"               # enterance, hall, pokemoncenter, stairs, elevator
    pkm_mart = "Pokemon Mart"                   # enterance, hall, shop, stairs, elevator
    dept_store = "Department Store"             # enterance, hall, shop, stairs, elevator
    mall = "Shopping Mall"                      # enterance, hall, shop (multiple), stairs, elevator
    cave = "Cave"                               # enterance, hall, cavern, lake, pit, ladder, stairs, elevator
    # ROOMS

    #
    #
#
    type_unknown = pokemon_type()
#
    type_normal = pokemon_type()
    type_normal.name = 'Normal'
    type_normal.weaknesses = ['Fighting']
    type_normal.resistances = []
    type_normal.immunities = ['Ghost']
    #
    type_fire = pokemon_type()
    type_fire.name = 'Fire'
    type_fire.weaknesses = ['Water', 'Ground', 'Rock']
    type_fire.resistances = ['Fire', 'Grass', 'Ice', 'Bug', 'Steel', 'Fairy']
    type_fire.immunities = []
    #
    type_water = pokemon_type()
    type_water.name = 'Water'
    type_water.weaknesses = ['Electric', 'Grass']
    type_water.resistances = ['Fire','Water','Ice','Steel']
    type_water.immunities = []
    #
    type_electric = pokemon_type()
    type_electric.name = 'Electric'
    type_electric.weaknesses = ['Ground']
    type_electric.esistances = ['Electric', 'Flying', 'Steel']
    type_electric.immunities = []
    #
    type_grass = pokemon_type()
    type_grass.name = 'Grass'
    type_grass.weaknesses = ['Fire', 'Ice', 'Poison', 'Flying', 'Bug']
    type_grass.resistances = ['Water', 'Electric', 'Grass', 'Ground']
    type_grass.immunities = []
    #
    type_ice = pokemon_type()
    type_ice.name = 'Ice'
    type_ice.weaknesses = ['Fire', 'Fighting', 'Rock', 'Steel']
    type_ice.resistances = ['Ice']
    type_ice.immunities = []
    #
    type_fighting = pokemon_type()
    type_fighting.name = 'Fighting'
    type_fighting.weaknesses = ['Flying', 'Psychic', 'Fairy']
    type_fighting.resistances = ['Bug', 'Rock', 'Dark']
    type_fighting.immunities = []
    #
    type_poison = pokemon_type()
    type_poison.name = 'Poison'
    type_poison.weaknesses = ['Ground', 'Psychic']
    type_poison.resistances = ['Grass', 'Fighting', 'Poison', 'Bug', 'Fairy']
    type_poison.immunities = []
    #
    type_ground = pokemon_type()
    type_ground.name = 'Ground'
    type_ground.weaknesses = ['Water', 'Grass', 'Ice']
    type_ground.resistances = ['Rock', 'Poison']
    type_ground.immunities = ['Electric']
    #
    type_flying = pokemon_type()
    type_flying.name = 'Flying'
    type_flying.weaknesses = ['Electric', 'Rock', 'Ice']
    type_flying.resistances = ['Grass', 'Fighting', 'Bug']
    type_flying.immunities = ['Ground']
    #
    type_psychic = pokemon_type()
    type_psychic.name = 'Psychic'
    type_psychic.weaknesses = ['Bug', 'Ghost', 'Dark']
    type_psychic.resistances = ['Fighting', 'Psychic']
    type_psychic.immunities = []
    #
    type_bug = pokemon_type()
    type_bug.name = 'Bug'
    type_bug.weaknesses = ['Fire', 'Flying', 'Rock']
    type_bug.resistances = ['Grass', 'Fighting', 'Ground']
    type_bug.immunities = []
    #
    type_rock = pokemon_type()
    type_rock.name = 'Rock'
    type_rock.weaknesses = ['Water', 'Grass', 'Fighting', 'Ground', 'Steel']
    type_rock.resistances = ['Normal', 'Fire', 'Poison', 'Flying']
    type_rock.immunities = []
    #
    type_ghost = pokemon_type()
    type_ghost.name = 'Ghost'
    type_ghost.weaknesses = ['Ghost', 'Dark']
    type_ghost.resistances = ['Poison', 'Bug']
    type_ghost.immunities = ['Normal', 'Fighting']
    #
    type_dragon = pokemon_type()
    type_dragon.name = 'Dragon'
    type_dragon.weaknesses = ['Ice', 'Dragon', 'Fairy']
    type_dragon.resistances = ['Fire','Water','Electric','Grass']
    type_dragon.immunities = []
    #
    type_dark = pokemon_type()
    type_dark.name = 'Dark'
    type_dark.weaknesses = ['Fighting', 'Bug', 'Fairy']
    type_dark.resistances = ['Ghost','Dark']
    type_dark.immunities = ['Psychic']
    #
    type_steel = pokemon_type()
    type_steel.name = 'Steel'
    type_steel.weaknesses = ['Fire', 'Fighting', 'Ground']
    type_steel.resistances = ['Normal', 'Grass', 'Ice', 'Flying' ,'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy']
    type_steel.immunities = ['Poison']
    #
    type_fairy = pokemon_type()
    type_fairy.name = 'Fairy'
    type_fairy.weaknesses = ['Poison','Steel']
    type_fairy.resistances = ['Fighting', 'Bug', 'Dark']
    type_fairy.immunities = ['Dragon']
    #item = ''
    #
    #item = ''
    #item = ''
    #item = ''
    #item = ''