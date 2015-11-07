from constants import constants

class pokedex():
    def __init__(self, dex_dict=None, trainer=None):
        
        self.creator = 'The Professor'
        self.version = '1.0'
        self.mode = 'Local'
        self.region = 'Orre'
        self.trainer_name = None
        self.trainer_id = None
        self.max_entries = 150
        self.max_number_pokemon_national = 721
        self.pokemon_seen = 0
        self.pokemon_obtained = 0
        # self.entries = {}
        self.local_entries = {}
        self.national_entries = {}
        index = 0
        for entry in range(self.max_entries):
            index += 1
            self.local_entries[index] = {"name": ' --- ', "seen": False, "obtained": False, "data": ' --- '}
        index = 0
        for entry in range(self.max_number_pokemon_national):
            index += 1
            self.national_entries[index] = {"name": ' --- ', "seen": False, "obtained": False, "data": ' --- '}
        self.set_license(trainer)
    #
    def set_pokedex(self, dex_dict=None, trainer=None):
        if dex_dict is None:
            return False
        self.creator = dex_dict.get('creator')
        self.version = dex_dict.get('version')
        self.mode = dex_dict.get('mode')
        self.max_entries = dex_dict.get('max entries')
        self.max_number_pokemon_national = 721
        self.pokemon_seen = dex_dict.get('seen')
        self.pokemon_obtained = dex_dict.get('obtained')
        # self.entries = {}
        self.local_entries = dex_dict.get('local entries')
        self.national_entries = dex_dict.get('national entries')
        if trainer is not None:
            self.set_license(trainer=trainer)
        return self
    #    
    def set_license(self, trainer=None):
        if trainer is None:
            return self
        self.trainer_name = trainer.name
        self.trainer_id = trainer.trainer_id
        self.region = trainer.region_of_origin
        return self
    def set_modes(self, mode=None):
        if mode is None:
            return self
        if mode.lower() is constants.regions[0].lower():
            self.mode = constants.regions[0]
            return self
        if mode.lower() is constants.regions[1].lower():
            self.mode = constants.regions[1]
            return self
        return self
    #
    #
    def get_pokedex_entries(self, start=None, end=None, search_by='seen', mode=None):
        if start is None:
            start = 1
        if mode is None: 
            mode = self.mode
        if mode is 'National' and end is None:
            end = self.max_number_pokemon_national
        elif mode is 'Local' and (end is None or end > self.max_entries):
            end = self.max_entries
        else:
            end = self.max_entries
        if start > end:
            return "ERROR: beginning index {} > end index {}".format(start, end)
        
        
        entries = "POKEDEX ENTRIES: {} - {} [{}] Search by: {}\n".format(start, end, mode.upper(), search_by.upper())
        row = "- {0:5} {1:10} {2:20}\n"
        if mode is 'Local':
            for entry in self.local_entries.keys():
                seen_obtained = " --- "
                if self.national_entries.get(entry).get('seen'):
                    seen_obtained = "Seen"
                if self.national_entries.get(entry).get('obtained'):
                    seen_obtained = "Obtained"
                # SEEN
                if search_by.lower() in 'seen':
                    if self.local_entries.get(entry).get('seen') is True:
                        entries += row.format(str(entry)+":", seen_obtained, self.local_entries.get(entry).get('name'))
                # OBTAINED
                elif search_by.lower() in 'obtained':
                    if self.local_entries.get(entry).get('obtained') is True:
                        entries += row.format(str(entry)+":", seen_obtained, self.local_entries.get(entry).get('name'))
                # BY TYPE
                elif 'type' in search_by.lower() or 'types' in search_by.lower():
                    try:
                        search_by_type = search_by.split()[0]
                        type = search_by.split()[1]
                        if type in self.local_entries.get(entry).get('types').get('name'):
                            entries += row.format(str(entry)+":", seen_obtained, self.local_entries.get(entry).get('name'))
                    except Expection:
                        return " FAILED SEARCH BY TYPE.  MISSING AN ARGUMENT< THE TYPE."
                # ALL
                else:
                    if entry >= start and entry <= end:
                        entries += row.format(str(entry)+":", seen_obtained, self.local_entries.get(entry).get('name'))
        else: 
            for entry in self.national_entries.keys():
               
                seen_obtained = "Unknown"
                if self.national_entries.get(entry).get('seen'):
                    seen_obtained = "Seen"
                if self.national_entries.get(entry).get('obtained'):
                    seen_obtained = "Obtained"
                # SEEN
                if search_by.lower() in 'seen':
                    if self.national_entries.get(entry).get('seen') is True:
                        entries += row.format(str(entry)+":", seen_obtained, self.national_entries.get(entry).get('name'))
                # OBTAINED
                elif search_by.lower() in 'obtained':
                    if self.national_entries.get(entry).get('obtained') is True:
                        entries += row.format(str(entry)+":", seen_obtained, self.national_entries.get(entry).get('name'))
                # BY TYPE
                elif 'type' in search_by.lower() or 'types' in search_by.lower():
                    try:
                        search_by_type = search_by.split()[0]
                        type = search_by.split()[1]
                        if type in self.national_entries.get(entry).get('types').get('name'):
                            entries += row.format(str(entry)+":", seen_obtained, self.national_entries.get(entry).get('name'))
                    except Expection:
                        return " FAILED SEARCH BY TYPE.  MISSING AN ARGUMENT< THE TYPE."
                # ALL
                else:
                    if entry >= start and entry <= end:
                        entries += row.format(str(entry)+":", seen_obtained, self.national_entries.get(entry).get('name'))
                
        entries += "\n{0:10}{1:10}\n".format('SEEN:', str(self.pokemon_seen))
        entries += "{0:10}{1:10}\n".format('OBTAINED:', str(self.pokemon_obtained))
        return entries
    #    
    def get_pokemon_entry(self, pokemon=None):
        if pokemon is None:
            return "NO POKEMON GIVEN. "
        line = "{0:15} {1:25}\n"
        line_evolve = "{0:10} by {1} with {2}\n"
        entry = line.format('ENTRY FOR', pokemon.name)
        entry += constants.divider_small
        entry += line.format('NAME',self.national_entries[pokemon.local_numbers['National']].get('name'))
        entry += line.format('LOCAL No. ',str(pokemon.local_numbers['Local']))
        entry += line.format('NATIONAL No. ',str(pokemon.local_numbers['National']))
        
        index = 0
        if self.national_entries[pokemon.local_numbers['National']].get('types') is not None:
            for type in self.national_entries[pokemon.local_numbers['National']].get('types'):
                index += 1
                entry += line.format('TYPE'+str(index),type.name)
        entry += line.format('SPECIES',self.national_entries[pokemon.local_numbers['National']].get('species'))
        entry += line.format('HEIGHT', self.national_entries[pokemon.local_numbers['National']].get('height'))
        entry += line.format('WEIGHT', self.national_entries[pokemon.local_numbers['National']].get('weight'))
        if self.national_entries[pokemon.local_numbers['National']].get('evolution') is not None:
            for evolution in self.national_entries[pokemon.local_numbers['National']].get('evolution'):  # list
                for pokemon_name in evolution.keys():  # dict
                    for method in evolution.get(pokemon_name):  # dict
                        entry += line_evolve.format('EVOLUTION', pokemon_name, evolution.get(pokemon_name), evolution.get(pokemon_name).get(method))
        else:
            entry += line_evolve.format('None', '', '')
        entry += "\n"
        if self.national_entries[pokemon.local_numbers['National']].get('seen'):
            entry += line.format('SEEN:', 'Yes')
        else:
            entry += line.format('SEEN:', 'No')
        if self.national_entries[pokemon.local_numbers['National']].get('obtained'):
            entry += line.format('OBTAINED:', 'Yes')
        else:
            entry += line.format('OBTAINED:', 'No')
        entry += constants.divider_small
        return entry
    #    
    def can_store_data(self):
        if len(self.local_entries) <= self.max_entries:
            return True
        return False
    #    
    def get_pokedex_metadata(self):
        meta_data = constants.divider_large
        meta_data += "--- {0:20}{1:20} ---\n".format('POKEDEX DATA','')
        meta_data += "--- {0:20}{1:20} ---\n".format('CREATOR:', str(self.creator))
        meta_data += "--- {0:20}{1:20} ---\n".format('VERSION:', str(self.version))
        meta_data += "--- {0:20}{1:20} ---\n".format('POKEDEX MODE:', str(self.mode))
        meta_data += "--- {0:20}{1:20} ---\n".format('POKEDEX REGION:', str(self.region))
        meta_data += "--- {0:20}{1:20} ---\n".format('TRAINER:', str(self.trainer_name))
        meta_data += "--- {0:20}{1:20} ---\n".format('TRAINER ID:', str(self.trainer_id))
        meta_data += "--- {0:20}{1:20} ---\n".format('MAX DATA STORAGE ', str(self.max_entries)+" entries")
        meta_data += "--- {0:20}{1:20} ---\n".format('SEEN:', str(self.pokemon_seen))
        meta_data += "--- {0:20}{1:20} ---\n".format('OBTAINED:', str(self.pokemon_obtained))
        meta_data += constants.divider_large
        #meta_data += "{0:20}{1:20}\n".format(':', )
        return meta_data
    #
    def add_obtained_entry(self, pokemon=None):
        if pokemon is None:
            return False
        # National
        if not self.national_entries[pokemon.local_numbers['National']]['seen']:
            self.pokemon_seen += 1
        if not self.national_entries[pokemon.local_numbers['National']]['obtained']:
            self.pokemon_obtained += 1
            self.national_entries[pokemon.local_numbers['National']]['name'] = pokemon.name
            self.national_entries[pokemon.local_numbers['National']]['types'] = pokemon.types
            self.national_entries[pokemon.local_numbers['National']]['name'] = pokemon.name
            self.national_entries[pokemon.local_numbers['National']]['species'] = pokemon.species
            self.national_entries[pokemon.local_numbers['National']]['height'] = pokemon.height
            self.national_entries[pokemon.local_numbers['National']]['weight'] = pokemon.weight
            self.national_entries[pokemon.local_numbers['National']]['data'] = pokemon.pokedex_entry # 
            self.national_entries[pokemon.local_numbers['National']]['seen'] = True
            self.national_entries[pokemon.local_numbers['National']]['obtained'] = True
            self.national_entries[pokemon.local_numbers['National']]['evolution'] = pokemon.evolution
        
        # Local
        if not self.local_entries[pokemon.local_numbers['Local']]['obtained']:
            #self.pokemon_obtained += 1
            self.local_entries[pokemon.local_numbers['Local']]['name'] = pokemon.name
            self.local_entries[pokemon.local_numbers['Local']]['types'] = pokemon.types
            self.local_entries[pokemon.local_numbers['Local']]['name'] = pokemon.name
            self.local_entries[pokemon.local_numbers['Local']]['species'] = pokemon.species
            self.local_entries[pokemon.local_numbers['Local']]['height'] = pokemon.height
            self.local_entries[pokemon.local_numbers['Local']]['weight'] = pokemon.weight
            self.local_entries[pokemon.local_numbers['Local']]['data'] = pokemon.pokedex_entry # 
            self.local_entries[pokemon.local_numbers['Local']]['seen'] = True
            self.local_entries[pokemon.local_numbers['Local']]['obtained'] = True
            self.local_entries[pokemon.local_numbers['Local']]['evolution'] = pokemon.evolution
        
        
        return True
    #
    def add_seen_entry(self, pokemon=None):
        if pokemon is None:
            return False
        if not self.national_entries[pokemon.local_numbers['National']].get('seen'):
            self.pokemon_seen += 1
            self.local_entries[pokemon.local_numbers['Local']] = {"name": pokemon.name, "seen": True, "obtained": False, "data": ' Capture this Pokemon to get all Pokedex data.'}
            self.national_entries[pokemon.local_numbers['National']] = {"name": pokemon.name, "seen": True, "obtained": False, "data": ' Capture this Pokemon to get all Pokedex data.'}
            return True
        return False
    #
    #
#











