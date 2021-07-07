class Agent:
    def __init__(self,locations,virus_type):
        self.population = virus_type.initial_population
        self.locations = locations
        self.default_health = virus_type.default_health
        self.healths = [self.default_health for _ in range(self.population)]
        self.vision = virus_type.vision
        self.code = virus_type.code

    def remove(self):
        new_locations = []
        new_healths = []
        removed_locations = []
        for idx in range(len(self.healths)):
            if self.healths[idx] != 0:
                new_locations.append(self.locations[idx])
                new_healths.append(self.healths[idx])
            else:
                removed_locations.append(self.locations[idx])
                self.population = self.population - 1
        self.healths = new_healths
        self.locations = new_locations
        return removed_locations

    def decrease_health(self):
        new_healths = []
        for health in self.healths:
            health = health - 1
            new_healths.append(health)
        self.healths = new_healths

    def increase_health(self,idx):
        self.healths[idx] += self.default_health

    def update_location(self,idx,new_location):
        self.locations[idx] = new_location

    def add(self,location,health):
        self.locations.append(location)
        self.healths.append(health)
        self.population += 1

    def sanity(self):
        return (len(self.locations) == len(self.healths) and self.population == len(self.locations))

    


