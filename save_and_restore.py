import pickle
import glob, os
from os import listdir
from os.path import isfile, join
import shutil
from utilities import *
#
def check_trainer(trainer_name=None, path=None):
    if trainer_name is not None:
        trainer = load_trainer(trainer_name=trainer_name, path=path)
        print trainer.get_from_load()
        #save_trainer(trainer=trainer, path=path)
#
def check_pokemon(pokemon_nickname=None,pokemon_name=None, path=None):
    if pokemon_nickname is not None and pokemon_name is not None :
        pokemon = load_pokemon(pokemon_nickname=None, pokemon_name=None, path=path)
        print pokemon.get_pokemon_full_stats()
        #save_pokemon(pokemon=pokemon, path=path)
#
def save_trainer(trainer=None, path=None):
    if trainer is None:
        return
    file_path = 'trainer\\'
    if path is not None:
        file_path = path
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_path = file_path+trainer.name+".pkl"
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'wb') as output:
        pickle.dump(trainer, output, 1)#pickle.HIGHEST_PROTOCOL)
    #print "Data for trainer {} as been saved".format(trainer.name)

#
def save_pokemon(pokemon=None, trainer=None, path=None):
    trainer_name = ''
    if pokemon is None:
        return
    if trainer is not None:
        trainer_name += trainer.name+"_"
    file_path = 'pokemon\\'
    if path is not None:
        file_path = path
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    file_path = file_path+trainer_name+pokemon.nickname+"_"+pokemon.name+".pkl"
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'wb') as output:
        pickle.dump(pokemon, output, pickle.HIGHEST_PROTOCOL)
    #print "Data for pokemon {} as been saved".format(pokemon.nickname)

#
def load_trainer(trainer_name=None, path=None):
    if trainer_name is None:
        return
    file_path = 'trainer\\'
    if path is not None:
        file_path = path
    file_path = file_path+trainer_name+".pkl"
    #print "loading: {}".format(file_path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as input:
            trainer = pickle.load(input)
        return trainer        
    else:
        print "{} does not exist".format(file_path)
        return None
#
def load_pokemon(pokemon_nickname=None, pokemon_name=None, trainer=None, path=None):
    if pokemon_nickname is None:
        return
    if pokemon_name is None:
        return
    if trainer is not None:
        trainer_name += trainer.name+"_"
    file_path = 'pokemon\\'
    if path is not None:
        file_path = path
    file_path = file_path+trainer_name+pokemon_nickname+"_"+pokemon_name+".pkl"
    if os.path.exists(file_path):
        with open(file_path, 'rb') as input:
            pokemon = pickle.load(input)
            return pokemon
    else:
        print "{} does not exist".format(file_path)
        return None
def get_pokemon_for_evolution(pokemon_name=None, path='pokemon'):
    if pokemon_name is None:
        return None
    #print pokemon_name
    cwd = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(cwd,path)
    #print file_path
    all_files = get_files_in_directory(file_path)
    #print all_files
    pokemon_pickle = None
    for file in all_files:
        if pokemon_name in file:
            pokemon_pickle = file
            #print pokemon_pickle
    if pokemon_pickle is None:
        return None
    file_path = os.path.join(file_path,pokemon_pickle)
    #print file_path
    if os.path.exists(file_path):
        with open(file_path, 'rb') as input:
            pokemon = pickle.load(input)
            #print "found {}".format(pokemon.name)
            return pokemon
    else:
        print "{} does not exist".format(file_path)
        return None
#
#
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
#
def get_files_in_directory(dir_path):
    return [f for f in listdir(dir_path) if isfile(join(dir_path, f))]