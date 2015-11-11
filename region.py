'''


'''
import os
import time
from random import randint
from constants import constants
from trainer import trainer
from trainerclass import *
from inventory import *
from pokedex import pokedex
from pokemon_dicts import *
from pokemon_kanto_dicts import *
from pokemon_johto_dicts import *
from pokemon_hoenn_dicts import *
from pokemon_sinnoh_dicts import *
from pokemon_unova_dicts import *
from pokemon import pokemon
from items import *
from cmd_interface import cmd_interface

class feature():
	def __init__(self):
		self.name = ""
		self.description = ""
		def __str__(self):
			return "{0}: {1}".format(self.name, self.description)

class area():
	def __init__(self, name="-- Name --", desc="-- Desc --"):
		self.name = name
		self.description = desc
		self.features = []
		self.paths = {} # areas
		self.encounters = []
		self.trainers = []
		self.wild_pokemon = []
	def connect_areas(self, zone, direction1=constants.north, direction2=constants.south): 
		if zone is None: return
		self.paths[direction1] = zone
		zone.paths[direction2] = self
		
	def display(self):
		text =  "{0}: {1}\n".format(self.name,self.description)
		for feature in self.features:
			text += "- {0}\n".format(feature.name)
		#text += "\n"
		for key in self.paths.keys():
			text += "- {0}: {1}\n".format(key, self.paths[key].name, self.paths[key].description)
		return text

class region():
	def __ini__(self):
		self.name = ""
		self.current_area = None
		self.areas = []
	def set_area(self, area_list = None):
		if area_list is None:
			return None
		self.areas = area_list
		return 1
	def move_to_adjacent_area(self, area_name):
		for path in self.current_area.paths:
			if path.name.lower() == area_name.lower():
				self.current_area = path
				print "Moving to adjacent area: {}".format(path.name)
				return True
	def display_map(self):
		if len(self.areas) > 0:
			for area in self.areas:
				print area.display()
				#print "\n"
		else:
			print "No Areas in region!"

