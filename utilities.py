from random import randint
from constants import constants
import re
from os import listdir
from os.path import isfile, join

def is_int(var):
    return isinstance(var, int )
def generate_id():
        id = ""
        for i in range(4):
            id += str(randint(0,9))
        id += "-"
        for i in range(4):
            id += str(randint(0,9))
        id += "-"
        for i in range(4):
            id += str(randint(0,9))
        return id
def get_next_level_exp(growth_rate=constants.growthrate_medium_fast, level=5):
    if growth_rate is constants.growthrate_fast:
        return int(round(0.8 * (level * level * level)))
        
    if growth_rate is constants.growthrate_medium_fast:
        return int(round((level * level * level)))
        
    if growth_rate is constants.growthrate_medium_slow:
        return int(round(1.2*(level * level * level) - 15*(level * level) + 100*level - 140))
        
    if growth_rate is constants.growthrate_slow:
        return int(round(1.25 * (level * level * level)))
        
    if growth_rate is constants.growthrate_erratic:
        return int(round(0.6 * (level * level * level)))
        
    if growth_rate is constants.growthrate_fluctuating:
        return int(round(1.64 * (level * level * level)))
        
    else: # constants.growthrate_fluctuating or some bad value
        return int(round(1.64 * (level * level * level)))
    def get_exp_for_level_up(growth_rate=constants.growthrate_medium_fast, level=None):
        if level is None or level < 1:
            level = 1
        level_cubed = level*level*level
        level_squared = level*level
        #print "calculating for level {}".format(level)
        if growth_rate is constants.growthrate_fast:
            #print int(round(0.8 * (level-1 * level-1 * level-1)))
            return int(round(0.8 * level_cubed))
        if growth_rate is constants.growthrate_medium_fast:
            #print int(round((level-1 * level-1 * level-1))) 
            return int(round(level_cubed)) 
        if growth_rate is constants.growthrate_medium_slow:
            #print int(round(1.2*(level-1 * level-1 * level-1) - 15*(level-1 * level-1) + 100*(level-1) - 140))
            return int(round((1.2*level_cubed) - (15*level_squared) + (100*level) - 140))
        if growth_rate is constants.growthrate_slow:
            #print 
            return int(round(1.25 * level_cubed))
        if growth_rate is constants.growthrate_erratic:
            #print int(round(1.25 * (level-1 * level-1 * level-1)))
            return int(round(0.6 * level_cubed))
        if growth_rate is constants.growthrate_fluctuating:
            #print int(round(1.64 * (level-1 * level-1 * level-1)))
            return int(round(1.64 * level_cubed))
        else: # constants.growthrate_fluctuating or some bad value
            #print int(round(1.64 * (level-1 * level-1 * level-1)))
            return int(round(1.64 * level_cubed))
def get_int_from_string(text=None):
    if text is None:
        print "get_int_from_string: text is none"
        return None
    print text
    try:
        return int(re.search(r'\d+', text).group())
    except Exception as e:
        #print "expection in getting int form string: {}".format(str(e))
        return None
def get_ints_from_string(text=None):
    if text is None:
        return None
    try:
        return map(int, re.findall('\d+', s))
    except Exception as e:
        return None
def get_files_in_directory(dir_path):
    return [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

#