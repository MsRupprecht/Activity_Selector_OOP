# This is where the activity class will live with all its objects

class Activity():
    def __init__(self,name, location, theme, energy, weight):
        self.name = name
        self.location = location
        self.theme = theme
        self.energy = energy
        self.weight = weight  # NOT SURE HOW YET, BUT WOULD BE NICE TO PUT IN
    
    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location
    
    def get_theme(self):
        return self.theme
    
    def get_energy(self):
        return self.energy
    
    def get_weight(self):
        return self.weight
    
    def set_name(self, name):
        self.name = name
    
    def set_location(self, location):
        self.location = location
    
    def set_theme(self, theme):
        self.theme = theme
    
    def set_energy(self, energy):
        self.energy = energy
    
    def set_weight(self, weight):
        self.weight = weight
    
    def __str__(self):
        return f"{self.name}"
    
