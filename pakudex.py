from pakuri import Pakuri


class Pakudex:

    def __init__(self, capacity=20):
        self.capacity = capacity  # initial value is 0
        self.pakuris = []  # store a list of pakuri objects
        self.size = 0  # keep track of the number of concrete pakuri

    # species vs. pakuri objects

    def get_size(self):
        return self.size

    def get_capacity(self):
        return self.capacity

    # pakuris but make it a list
    def get_species_array(self):
        return None if self.size == 0 else [i.species for i in self.pakuris]

    # pakuris but make it a sorted list
    def sort_pakuri(self):
        self.pakuris.sort()

    # gets stats for pakuri
    def get_stats(self, species):
        # loop through self.pakuris to look at each pakuri object
        #   compare pakuri.species == species
        #   if true, return [pakuri.attack, pakuri.defense, pakuri.speed]
        element = Pakuri(species)
        if element in self.pakuris:
            stats = [element.attack, element.defense, element.speed]
            return stats
        else:
            return None

    # adds pakuri to pakuri class
    def add_pakuri(self, species):

        # 1. check duplicates -> return false
        # loop through self.pakuris to look at each pakuri object
        #   compare pakuri.species == species

        obj_species = Pakuri(species)

        if obj_species not in self.pakuris:
            self.pakuris.append(obj_species)
            self.size += 1
            return True
        print('Error: Pakudex already contains this species!')
        return False

    # function to change pakuri stats
    def evolve_species(self, species):
        if species in self.pakuris:
            Pakuri.evolve(species)
            return True
        if species not in self.pakuris:
            return False
