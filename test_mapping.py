'''
'''
from region import room, area, feature
from constants import constants


def populate_map(the_map):
	'''		
	      [6]
	      [5]
	[4][3][2]
	      [1]
	      [0]
	'''
	zone0 = room(name="Pallet Town", desc=constants.town)
	zone1 = room(name="Route 1", desc=constants.field_route)
	zone2 = room(name="Viridian City", desc=constants.city)
	zone3 = room(name="Route 22", desc=constants.valley_route)
	zone4 = room(name="Indigo Platue", desc=constants.pkm_stadium)
	zone5 = room(name="Route 2", desc=constants.forest_route)
	zone6 = room(name="Viridian Forest", desc=constants.forest)
	zones = [zone0,zone1, zone2, zone3, zone4, zone5, zone6]
	zone0.connect_areas(zone1, constants.north, constants.south)
	zone1.connect_areas(zone2, constants.north, constants.south)
	zone2.connect_areas(zone3, constants.west, constants.east)
	zone3.connect_areas(zone4, constants.west, constants.east)
	zone2.connect_areas(zone5, constants.north, constants.south)
	zone5.connect_areas(zone6, constants.north, constants.south)
	the_map.current_area = zone0
	the_map.areas = zones
def create_pokemon_center(the_map):
	'''
	   [2]
	[ ][1][ ]
 	   [0]
	'''
	zone0 = room(name="Front Door", desc=constants.enterance)
	zone0.add_feature(feature("Phone Booth","Prop"))
	zone1 = room(name="Waiting Room", desc=constants.lounge) # includes PC feature
	zone1.add_feature(feature("Table","Prop")).add_feature(feature("Chairs","Prop"))
	zone1.add_feature(feature("Television","Prop")).add_feature(feature("Bookshelf","Prop"))
	zone2 = room(name="Center Desk", desc=constants.frontdesk) # where Nurse Joy and other staff meet trainers
	zone2.add_feature(feature("Nurse","Person")).add_feature(feature("Notice Board","Prop"))
	zone2.add_feature(feature("Healing Machine","Prop"))
	zone0.connect_areas(zone1, constants.north, constants.south)
	zone1.connect_areas(zone2, constants.north, constants.south)
	zones = [zone0,zone1,zone2]
	the_map.current_area = zone0
	the_map.areas = zones
	

def main():
	test_map = area()
	test_map.name = "Test Area"
	create_pokemon_center(test_map)
	test_map.display_map()
	test_map.display_current()
	print "================================="
	test_map.move_to_adjacent_area("North")
	test_map.move_to_adjacent_area("nORTH")
	test_map.display_current()
	print "================================="
	test_map.move_to_adjacent_area("south")
	test_map.display_current()
	print "================================="
	test_map.move_to_adjacent_area("east")
	test_map.display_current()
	print "================================="








main()