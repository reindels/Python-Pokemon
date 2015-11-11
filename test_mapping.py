'''
'''
from region import region, area, feature
from constants import constants


def populate_map(the_region):
	'''		
	      [6]
	      [5]
	[4][3][2]
	      [1]
	      [0]

	'''
	zone0 = area(name="Pallet Town", desc=constants.town)
	zone1 = area(name="Route 1", desc=constants.field_route)
	zone2 = area(name="Viridian City", desc=constants.city)
	zone3 = area(name="Route 22", desc=constants.valley_route)
	zone4 = area(name="Indigo Platue", desc=constants.pkm_stadium)
	zone5 = area(name="Route 2", desc=constants.forest_route)
	zone6 = area(name="Viridian Forest", desc=constants.forest)
	zones = [zone0,zone1, zone2, zone3, zone4, zone5, zone6]
	zone0.connect_areas(zone1, constants.north, constants.south)
	zone1.connect_areas(zone2, constants.north, constants.south)
	zone2.connect_areas(zone3, constants.west, constants.east)
	zone3.connect_areas(zone4, constants.west, constants.east)
	zone2.connect_areas(zone5, constants.north, constants.south)
	zone5.connect_areas(zone6, constants.north, constants.south)
	the_region.current_area = zone0
	the_region.areas = zones


def main():
	test_map = region()
	test_map.name = "Test Area"
	populate_map(test_map)
	test_map.display_map()










main()