from constants import constants

class item():
    def __init__(self, item_dict):
        self.name = 'Potion'
        self.type = constants.item_type_medicine
        # constants.item_type_medicine = 'Medicine'
        # constants.item_type_vitamin = 'Vitamin'
        # constants.item_type_berry = 'Berry'
        # constants.item_type_key_item = 'Key Item'
        # constants.item_type_poke_ball = 'Poke Ball'
        # constants.item_type_tm_hm = 'TM HM'
        # constants.item_type_held_item = 'Held Items'
        # constants.item_type_general = 'General'
        # constants.item_type_mail = 'Mail'
        self.price = 300
        self.message = None
        self.effects = []
        self.description = "Heals a Pokemon's HP by 20"
        self.ball_modifier = None
        self.create_item_from_dict(item_dict=item_dict)
        
    #
    def get_sell_back_price(self):
        return int(round(self.price / 2.0))
    #
    def create_item_from_dict(self, item_dict=None):
        if item_dict is None:
            return None
        self.name = item_dict.get('name')
        self.type = item_dict.get('type')
        self.price = item_dict.get('price')
        self.effects = item_dict.get('effect')
        self.description = item_dict.get('description')
        self.ball_modifier = item_dict.get('ball modifier') # 1-4
        self.message = item_dict.get('message')
        #
    #
    def __str__(self):
        return self.name + " (" + self.type + "): $" + str(self.price)
    #
    def copy(self):
        copy_item = item()
        copy_item.name = self.name
        copy_item.type = self.type 
        copy_item.price = self.price 
        copy_item.effects = self.effects
        copy_item.description = self.description
        copy_item.ball_modifier = self.ball_modifier
        return copy_item
    def get_recover_amount(self):
        return 80
#
# poke balls
custom_ball_dict = {'name': 'Custom Ball', 
'type': constants.item_type_poke_ball, 
'price': 1200, 'ball modifier': 3, 
'description': "A custom-made Poke Ball used to capture Pokemon." 
}
poke_ball_dict = {'name': 'Poke Ball', 
'type': constants.item_type_poke_ball, 
'price': 200, 'ball modifier': 1, 
'description': "A device used to capture Pokemon." 
}
great_ball_dict = {'name': 'Great Ball', 
'type': constants.item_type_poke_ball, 
'price': 600, 'ball modifier': 1.5, 
'description': "A good Poke Ball used to capture Pokemon." 
}
ultra_ball_dict = {'name': 'Ultra Ball', 
'type': constants.item_type_poke_ball, 
'price': 1200, 'ball modifier': 2, 
'description': "A high-quality Poke Ball used to capture Pokemon." 
}
master_ball_dict = {'name': 'Master Ball', 
'type': constants.item_type_poke_ball, 
'price': 1000000, 'ball modifier': constants.empty, 
'description': "A custom-made Poke Ball that guaruntees capture of any Pokemon." 
}
#Potions
fresh_water_dict = {'name': 'Fresh Water', 
'type': constants.item_type_medicine, 
'effect': ["Pokemon Recover 80 hp"],
'price': 300, 'description': "A pokemon medicine that heals a Pokemon by 80 HP." 
}
revive_dict = {'name': 'Revive', 
'type': constants.item_type_medicine, 
'effect': ["Revives Pokemon to Half HP"],
'price': 300, 'description': "A medicine that revives a fainted pokemon to half its full HP." 
}
potion_dict = {'name': 'Potion', 
'type': constants.item_type_medicine, 
'effect': ["Pokemon Recover 20 hp"],
'price': 300, 'description': "A pokemon medicine that heals a Pokemon by 20 HP." 
}
superpotion_dict = {'name': 'Super Potion', 
'type': constants.item_type_medicine, 
'effect': ["Pokemon Recover 50 hp"],
'price': 600, 'description': "A pokemon medicine that heals a Pokemon by 50 HP." 
}
full_heal_dict = {'name': 'Full Heal', 
'type': constants.item_type_medicine, 
'effect': ["{} {} {} on Pokemon".format(constants.remove, constants.status_all_negative, constants.status_infliction)],
'price': 1000, 'description': "A spray bottle whose contents remove negative status conditions from Pokemon." 
}
full_restore_dict = {'name': 'Full Restore', 
'type': constants.item_type_medicine, 
'effect': ["{} {} {}".format(constants.remove, constants.status_all_negative, constants.status_infliction), 
"Pokemon Recover 9999 hp"],
'price': 3000, 'description': "A spray bottle whose contents remove negative status conditions from Pokemon and fully heals them." 
}
#General Items
escape_rope_dict = {'name': 'Escape Rope', 
'type': constants.item_type_general, 
'effect': "Exit Dungeon",
'price': 450, 'description': "A rope that you can tie off at a dungeon entrance.  If you get lost, follow it to find the entrance." 
}
#Vitamin Items
protein_dict = {'name': 'Protein', 
'type': constants.item_type_vitamin, 
'effect': ["Add 10 EV to a Pokemon's ATTACK Stat"],
'price': 9800, 'description': "Vitamins that boost Attack." 
}
#held Items
pink_bow_dict = {'name': 'Pink Bow', 
'type': constants.item_type_held_item, 
'effect': ["Boost Normal Type Attacks by x1.5"],
'price': 1000, 'description': "A cute pink bow that boost Normal type attacks when given to a pokemon to hold." 
}
#Berry Items
oran_berry_dict = {'name': 'Oran Bery', 
'type': constants.item_type_berry, 
'effect': ["Pokemon Recover 20 hp"],
'price': 10, 'description': "A pokemon medicine that heals a Pokemon by 10 HP." 
}
#TM & HM Items
HM_01_dict = {'name': 'HM 01 (Cut)', 
'type': constants.item_type_tm_hm, 
'effect': ["Pokemon Learns Move Cut"],
'price': 1000, 'description': "A Reuseable data disk that can teach pokemon the Hidden Move Cut." 
}
#Key Items
acro_bike_dict = {'name': 'Acro Bike', 
'type': constants.item_type_key_item, 
'effect': ["Allows Movement Through Bike Paths And Trick Bike Paths"],
'price': 10000, 'description': "A ligth weight bike that can perform tricky manuevers." 
}
#Mail Items
pika_mail_dict = {'name': 'Pika Mail', 
'type': constants.item_type_mail, 
'effect': ["Write A Message"],
'message': "Write a message here...",
'price': 30, 'description': "A Pikachu themed paper and envelope." 
}
# Evolution Items
water_stone_dict = {'name': 'Water Stone', 
'type': constants.item_type_key_item, 
'effect': ["Evolves certain Water-Type Pokemon"],
'price': 3000, 'description': "This clear blue stone radiates a cool watery aura and smells like the water were it was found. This stone could evolve certain Pokemon." 
}
thunder_stone_dict = {'name': 'Thunder Stone', 
'type': constants.item_type_key_item, 
'effect': ["Evolves certain Electric-Type Pokemon"],
'price': 3000, 'description': "This green-blue stone with yellow veins radiates an electrical aura and smells like a brewing thunderstorm.  This stone could evolve certain Pokemon." 
}
fire_stone_dict = {'name': 'Water Stone', 
'type': constants.item_type_key_item, 
'effect': ["Evolves certain Fire-Type Pokemon"],
'price': 3000, 'description': "This orange-red stone radiates a warm firey aura and smells like brimstone.  This stone could evolve certain Pokemon." 
}
moon_stone_dict = {'name': 'Moon Stone', 
'type': constants.item_type_key_item, 
'effect': ["Evolves certain Pokemon"],
'price': 3000, 'description': "This opaque pearly white stone radiates an aura like cold water.  This stone could evolve certain Pokemon." 
}
sun_stone_dict = {'name': 'Sun Stone', 
'type': constants.item_type_key_item, 
'effect': ["Evolves certain Pokemon"],
'price': 3000, 'description': "This bright yellow stone radiates a warm bright aura and smells like dried sunflowers.  This stone could evolve certain Pokemon." 
}
fey_stone_dict = {'name': 'Fey Stone', 
'type': constants.item_type_key_item, 
'effect': ["Evolves certain Pokemon"],
'price': 3000, 'description': "This sparkling pink stone radiates a warm aura and smells like a pinewoods.  This stone could evolve certain Pokemon." 
}


#BASIC General INVENTORY

test_inv_dict = {
constants.item_type_general: {
'Escape Rope': {'count': 1, 'item': item(escape_rope_dict)}
},
constants.item_type_vitamin: {
'Protein': {'count': 1, 'item': item(protein_dict)}
},
constants.item_type_medicine:{
'Potion': {'count': 5, 'item': item(potion_dict)},
'Super Potion': {'count': 1, 'item': item(superpotion_dict)},
'Fresh Water': {'count': 1, 'item': item(fresh_water_dict)},
'Full Heal': {'count': 1, 'item': item(full_heal_dict)},
'Revive': {'count': 1, 'item': item(revive_dict)},
},
constants.item_type_poke_ball:{
'Poke Ball': {'count': 50, 'item': item(poke_ball_dict)},
'Great Ball': {'count': 50, 'item': item(great_ball_dict)},
'Ultra Ball': {'count': 50, 'item': item(ultra_ball_dict)},
'Master Ball': {'count': 5, 'item': item(master_ball_dict)},
'Custom Ball': {'count': 5, 'item': item(custom_ball_dict)}
},
constants.item_type_held_item: {
'Pink Bow': {'count': 1, 'item': item(pink_bow_dict)}
},
constants.item_type_berry: {
'Oran berry': {'count': 1, 'item': item(oran_berry_dict)}
},
constants.item_type_tm_hm: {
'HM 01 (Cut)': {'count': 1, 'item': item(HM_01_dict)}
},
constants.item_type_key_item: {
'Acro Bike': {'count': 1, 'item': item(acro_bike_dict)}
},
constants.item_type_mail: {
'Pika Mail': {'count': 1, 'item': item(pika_mail_dict)}
}
}






#
#
#
#