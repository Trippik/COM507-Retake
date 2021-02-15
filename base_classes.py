# -----BASE CLASSES-----
class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getter(self):
        return([self.x, self.y])

    def setter(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
class Agent:
    def __init__(self, x, y):
        self.location = Location(x, y)
    
    def getter(self):
        return(self.location.getter())
    
    def setter(self, new_x, new_y):
        self.location.setter(new_x, new_y)
    
    def set_environment(self, environment):
        self.environment = environment

class Environment:
    def set_size(self, x, y):
        self.size = [x,y]

    def get_size(self):
        return(self.size)
    
    def set_agents(self, agents):
        self.agents = agents
    
    def get_agents(self):
        return(self.agents)
    
    def clear_environment(self):
        self.agents = None

#-----TESTING CODE-----    
#test_agent = Agent(1, 1)
#test_environment = Environment()
#test_environment.set_size(5,5)
#print(test_environment.get_size())
#test_environment.set_agents([test_agent,])
#print(test_environment.get_agents())
#print(test_environment.get_agents()[0].getter())
#test_environment.clear_environment()
#print(test_environment.get_agents())