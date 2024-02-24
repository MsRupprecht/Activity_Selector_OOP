## This is where the activity class will live with all its objects

## Creating the activity class
class Activity():

    def __init__(self,name, location, theme, energy):
        self.name = name
        self.location = location
        self.theme = theme
        self.energy = energy
            
    def get_name(self):
        return self.name
    
    def get_location(self):
        return self.location
    
    def get_theme(self):
        return self.theme
    
    def get_energy(self):
        return self.energy
    
    def set_name(self, name):
        self.name = name
    
    def set_location(self, location):
        self.location = location
    
    def set_theme(self, theme):
        self.theme = theme
    
    def set_energy(self, energy):
        self.energy = energy
    
    def __str__(self):
        return f"{self.name}"
    
    def set_list(self, list):
        list.append(self)
    
    def get_available_themes(main_list, sub_list):
        for activity in main_list:
            if activity.theme not in sub_list:
                sub_list.append(activity.theme)