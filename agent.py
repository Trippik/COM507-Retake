from location import Location

class Agent:
    def __init__(self, x, y):
        self.location = Location(x, y)
    
    def getter(self):
        return(self.location.getter())
    
    def setter(self, new_x, new_y):
        self.location.setter(new_x, new_y)
    
    def set_environment(self, environment):
        self.environment = environment
        self.environment.set_agents(self)