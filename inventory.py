from constants import constants
from items import *

class inventory():
    def __init__(self):
        #item_type_general = 'General'
        #item_type_medicine = 'Medicine'
        #item_type_vitamin = 'Vitamin'
        #item_type_held_item = 'Held Item'
        #item_type_poke_ball = 'Poke Ball'
        #item_type_tm_hm = 'TM HM'
        #item_type_berry = 'Berry'
        #item_type_key_item = 'Key Item'
        #item_type_mail = 'Mail'
        self.trainer = None
        self.general_items = {}
        self.medicine_items = {}
        self.vitamin_items = {}
        self.held_items = {}
        self.poke_balls_items = {}
        self.tm_hm_items = {}
        self.berry_items = {}
        self.key_items = {}
        self.mail = {}
    #
    def set_owner(self, trainer=None):
        if trainer is None:
            return self
        self.trainer = trainer
        return self
    def add_items(self, item, count):
        if item.type is constants.item_type_general:
            for item_in_pack in self.general_items.keys():
                if item.name is item_in_pack:
                    self.general_items[item_in_pack]['count'] += count
                    return "{0} x{1} added to inventory".format(item.name, count)
            self.general_items[item.name]={'count': count, 'item': item}
            return "{0} x{1} added to inventory".format(item.name, count)
            
        elif item.type is constants.item_type_medicine:
            for item_in_pack in self.medicine_items.keys():
                if item.name is item_in_pack:
                    self.medicine_items[item_in_pack]['count'] += count
                    return "{0} x{1} added to inventory".format(item.name, count, )
            self.medicine_items[item.name]={'count': count, 'item': item}
            return "{0} x{1} added to inventory".format(item.name, count)
        
        elif item.type is constants.item_type_vitamin:
            for item_in_pack in self.vitamin_items.keys():
                if item.name is item_in_pack:
                    self.vitamin_items[item_in_pack]['count'] += count
                    return "{0} x{1} added to inventory".format(item.name, count, )
            self.vitamin_items[item.name]={'count': count, 'item': item}
            return "{0} x{1} added to inventory".format(item.name, count)
        
        elif item.type is constants.item_type_held_item:
            for item_in_pack in self.held_items.keys():
                if item.name is item_in_pack:
                    self.held_items[item_in_pack]['count'] += count
                    return "{0} x{1} added to inventory".format(item.name, count, )
            self.held_items[item.name]={'count': count, 'item': item}
            return "{0} x{1} added to inventory".format(item.name, count)
        
        elif item.type is constants.item_type_poke_ball:
            for item_in_pack in self.poke_balls_items.keys():
                if item.name is item_in_pack:
                    self.poke_balls_items[item_in_pack]['count'] += count
                    return "{0} x{1} added to inventory".format(item.name, count, )
            self.poke_balls_items[item.name]={'count': count, 'item': item}
            return "{0} x{1} added to inventory".format(item.name, count)
        
        elif item.type is constants.item_type_tm_hm:
            for item_in_pack in self.tm_hm_items.keys():
                if item.name is item_in_pack:
                    self.tm_hm_items[item_in_pack]['count'] += count
                    return "{0} x{1} added to inventory".format(item.name, count, )
            self.tm_hm_items[item.name]={'count': count, 'item': item}
            return "{0} x{1} added to inventory".format(item.name, count)
        
        elif item.type is constants.item_type_berry:
            for item_in_pack in self.berry_items.keys():
                if item.name is item_in_pack:
                    self.berry_items[item_in_pack]['count'] += count
                    return "{0} x{1} added to inventory".format(item.name, count, )
            self.berry_items[item.name]={'count': count, 'item': item}
            return "{0} x{1} added to inventory".format(item.name, count)
        elif item.type is constants.item_type_mail:
            for item_in_pack in self.mail.keys():
                if item.name is item_in_pack:
                    self.mail[item_in_pack]['count'] += count
                    return "{0} x{1} added to inventory".format(item.name, count, )
            self.mail[item.name]={'count': count, 'item': item}
            return "{0} x{1} added to inventory".format(item.name, count)
        else: # if item.type is constants.item_type_key_item:
            for item_in_pack in self.key_items.keys():
                if item.name is item_in_pack:
                    self.key_items[item_in_pack]['count'] += count
                    return "{0} x{1} added to inventory".format(item.name, count, )
            self.key_items[item.name]={'count': count, 'item': item}
            return "{0} x{1} added to inventory".format(item.name, count)
        return True
    def get_item(self, item_name=None):
        if item_name is None:
            return None
        print item_name
        for item_in_pack in self.general_items.keys():
            print item_in_pack
            if item_name.lower() in item_in_pack.lower() and item_name[0].lower() == item_in_pack[0].lower():
                return self.general_items[item_in_pack].get('item')
        for item_in_pack in self.medicine_items.keys():
            if item_name.lower() in item_in_pack.lower() and item_name[0].lower() == item_in_pack[0].lower():
                    return self.medicine_items[item_in_pack].get('item')
        #
        for item_in_pack in self.vitamin_items.keys():
            print item_in_pack
            if item_name.lower() in item_in_pack.lower() and item_name[0].lower() == item_in_pack[0].lower():
                return self.vitamin_items[item_in_pack].get('item')
        #
        for item_in_pack in self.held_items.keys():
            print item_in_pack
            if item_name.lower() in item_in_pack.lower() and item_name[0].lower() == item_in_pack[0].lower():
                return self.held_items[item_in_pack].get('item')
        #
        for item_in_pack in self.poke_balls_items.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0].lower() == item_in_pack[0].lower():
                return self.poke_balls_items[item_in_pack].get('item')
        #
        for item_in_pack in self.tm_hm_items.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0].lower() == item_in_pack[0].lower():
                return self.tm_hm_items[item_in_pack].get('item')
        #
        for item_in_pack in self.berry_items.keys():
            #print item_in_pack
            if item_name.lower() in item_in_pack.lower() and item_name[0].lower() == item_in_pack[0].lower():
                return self.berry_items[item_in_pack].get('item')
        #
        for item_in_pack in self.mail.keys():
            #print item_in_pack
            if item_name.lower() in item_in_pack.lower() and item_name[0].lower() == item_in_pack[0].lower():
                return self.mail[item_in_pack].get('item')
        #
        for item_in_pack in self.key_items.keys():
            #print item_in_pack
            if item_name.lower() in item_in_pack.lower() and item_name[0].lower() == item_in_pack[0].lower():
                return self.key_items[item_in_pack].get('item')
        #
        return None
    def use_items(self, item_name, count):
        item = None
        #print item_name
        for item_in_pack in self.general_items.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0] is item_in_pack[0]:
                item = self.general_items[item_in_pack].get('item')
                if item is not None:
                    self.general_items[item_in_pack]['count'] -= count
        for item_in_pack in self.medicine_items.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0] is item_in_pack[0]:
                item = self.medicine_items[item_in_pack].get('item')
                if item is not None:
                    self.medicine_items[item_in_pack]['count'] -= count
        #
        for item_in_pack in self.vitamin_items.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0] is item_in_pack[0]:
                item = self.vitamin_items[item_in_pack].get('item')
                if item is not None:
                    self.vitamin_items[item_in_pack]['count'] -= count
        for item_in_pack in self.held_items.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0] is item_in_pack[0]:
                item = self.held_items[item_in_pack].get('item')
                if item is not None:
                    self.held_items[item_in_pack]['count'] -= count
        #
        for item_in_pack in self.poke_balls_items.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0] is item_in_pack[0]:
                item = self.poke_balls_items[item_in_pack].get('item')
                if item is not None:
                    self.poke_balls_items[item_in_pack]['count'] -= count
        for item_in_pack in self.tm_hm_items.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0] is item_in_pack[0]:
                item = self.tm_hm_items[item_in_pack].get('item')
                if item is not None:
                    self.tm_hm_items[item_in_pack]['count'] -= count
        for item_in_pack in self.berry_items.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0] is item_in_pack[0]:
                item = self.berry_items[item_in_pack].get('item')
                if item is not None:
                    self.berry_items[item_in_pack]['count'] -= count
        #
        for item_in_pack in self.mail.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0] is item_in_pack[0]:
                item = self.mail[item_in_pack].get('item')
                if item is not None:
                    self.mail[item_in_pack]['count'] -= count
        for item_in_pack in self.key_items.keys():
            #print item_in_pack
            if item_name in item_in_pack and item_name[0] is item_in_pack[0]:
                item = self.key_items[item_in_pack].get('item')
                #if item is not None:
                    #self.key_items[item_in_pack]['count'] -= count
        #
        return item   
    def display_inventory(self, pocket='all'):
        pack_str = 'Pack: \n'
        if pocket.lower() == "all" or pocket.lower() in "general":
            pack_str += "General:  \n"
            for item in self.general_items.keys():
                if self.general_items[item]['count'] > 0:
                    pack_str += " - {0}: x{1} \n".format(item, self.general_items[item]['count'])
        
        if pocket.lower() == "all" or pocket.lower() in "medicine":
            pack_str += "Medicine:  \n"   
            for item in self.medicine_items.keys():
                if self.medicine_items[item]['count'] > 0:
                    pack_str += " - {0}: x{1} \n".format(item, self.medicine_items[item]['count'])
        
        if pocket.lower() == "all" or pocket.lower() in "vitamins":
            pack_str += "Vitamins:  \n"    
            for item in self.vitamin_items.keys():
                if self.vitamin_items[item]['count'] > 0:
                    pack_str += " - {0}: x{1} \n".format(item, self.vitamin_items[item]['count'])
        
        if pocket.lower() == "all" or pocket.lower() in "held":
            pack_str += "Held Items:  \n"    
            for item in self.held_items.keys():
                if self.held_items[item]['count'] > 0:
                    pack_str += " - {0}: x{1} \n".format(item, self.held_items[item]['count'])
        
        if pocket.lower() == "all" or pocket.lower() in "pokeballs":     
            pack_str += "Pokeballs:  \n"    
            for item in self.poke_balls_items.keys():
                if self.poke_balls_items[item]['count'] > 0:
                    pack_str += " - {0}: x{1} \n".format(item, self.poke_balls_items[item]['count'])
        
        if pocket.lower() == "all" or pocket.lower() in "machines":
            pack_str += "Machines:  \n"    
            for item in self.tm_hm_items.keys():
                if self.tm_hm_items[item]['count'] > 0:
                    pack_str += " - {0}: x{1} \n".format(item, self.tm_hm_items[item]['count'])
            
        if pocket.lower() == "all" or pocket.lower() in "berries":
            pack_str += "Berries:  \n"    
            for item in self.berry_items.keys():
                if self.berry_items[item]['count'] > 0:
                    pack_str += " - {0}: x{1} \n".format(item, self.berry_items[item]['count'])
        
        if pocket.lower() == "all" or pocket.lower() in "mail":        
            pack_str += "Mail:  \n"
            for item in self.mail.keys():
                if self.mail[item]['count'] > 0:
                    pack_str += " - {0}: x{1} \n".format(item, self.mail[item]['count'])
        
        if pocket.lower() == "all" or pocket.lower() in "key":        
            pack_str += "Key Items:  \n"    
            for item in self.key_items.keys():
                pack_str += " - {0} \n".format(item)
                
        return pack_str + "\n"