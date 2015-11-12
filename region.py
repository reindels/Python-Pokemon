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
	def __init__(self, name="-- Feature Name --", desc="-- Feature Desc --"):
		self.name = name
		self.description = desc
		self.type = {}
	def __str__(self):
		text = "{0}: {1}".format(self.name, self.description)
		for key in self.type.keys():
			if key is constants.exit:
				text += " - Exit: {0}\n".format(self.type[key].name)
		return text
	def set_type(self, key, param):
		self.type[key] = param
		return self


class room():
	def __init__(self, name="-- Name --", desc="-- Desc --"):
		self.name = name
		self.description = desc
		self.features = []
		self.paths = {} # areas
		self.encounters = []
		self.trainers = []
		self.wild_pokemon = []
	def add_feature(self, feature):
		self.features.append(feature)
		return self
	def connect_areas(self, zone, direction1=constants.north, direction2=constants.south): 
		if zone is None: return
		self.paths[direction1] = zone
		if direction2 is not None:
			zone.paths[direction2] = self
		return self
	def display(self, include_features=False):
		text =  "{0} ({1}).\n".format(self.name,self.description)
		if include_features:
			text += "Features:\n"
			for feature in self.features:
				text += "- {0}\n".format(feature)
		#text += "\n"
		text += "Paths:\n"
		for key in self.paths.keys():
			text += "- {0}: {1}\n".format(key, self.paths[key].name, self.paths[key].description)
		return text

class area():
	def __ini__(self):
		self.name = ""
		self.current_area = None
		self.areas = []
	def set_area(self, area_list = None):
		if area_list is None:
			return None
		self.areas = area_list
		return 1
	def display_current(self):
		print "Currently in the " + self.current_area.display(True)

	def move_to_adjacent_area(self, direction):
		direction = direction.lower()
		direction = direction[0].upper() + direction[1:]
		#print direction
		if direction in self.current_area.paths.keys():
			self.current_area = self.current_area.paths[direction]
		else:
			print "direction {} not available.".format(direction)
		return self
	def display_map(self):
		if len(self.areas) > 0:
			for area in self.areas:
				print area.display()
				#print "\n"
		else:
			print "No Areas in region!"

