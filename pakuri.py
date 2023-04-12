class Pakuri:

    def __init__(self, species):
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

    # getter
    def get_species(self):
        return self.species

    # setter
    def set_species(self, new_species):
        self.species = new_species

    # getter
    def get_attack(self):
        return self.attack

    # getter
    def get_defense(self):
        return self.defense

    # getter
    def get_speed(self):
        return self.speed

    # setter
    def set_attack(self, new_attack):
        self.attack = new_attack

    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3

    # less than
    def __lt__(self, other):
        return self.species < other.species

    # equal
    def __eq__(self, other):
        return self.species == other.species
