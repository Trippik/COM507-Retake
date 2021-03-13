#-----IMPORT NECESSARY CLASSES AND LIBRARIES-----
from agent import Agent
from rock import Rock

#ROVER CLASS
class Rover(Agent):
    def __init__(self, rover_position, ship_position, battery_level):
        self.battery_level = battery_level
        self.ship_position = ship_position
        self.inventory = None
        self.mode = 0
        super().__init__(rover_position[0], rover_position[1])

    #Move rover along defined vector and deplete battery
    def move(self, vector, battery_change):
        if(self.battery_level > battery_change):
            current_loc = self.getter()
            new_x = current_loc[0] + vector[0]
            new_y = current_loc[1] + vector[1]
            self.setter(new_x, new_y)
            self.battery_level = self.battery_level - battery_change
    
    #If in collection mode collect rock at current coordinates
    def collect(self):
        if(self.mode == 0):
            for agent in self.environment.get_agents():
                if(type(agent) is Rock):
                    if (agent.getter() == self.getter()):
                        self.inventory = agent
                        self.mode = 1
    
    def scan(self, targets, item):
        agents = self.environment.get_agents()
        results = ()
        for target in targets:
            for agent in agents:
                if((target == agent.getter()) and (type(agent) is item)):
                    results = results + (target,)
        return(results)

    def look(self, item):
        rover_loc = self.getter()
        targets = []
        x = rover_loc[0]
        y = rover_loc[1]
        x_target_m = x - 1
        y_target_m = x - 1
        targets = targets + [(x, y_target_m), (x_target_m, y), (x_target_m, y_target_m),]
        x_target_p = x + 1
        y_target_p = x + 1
        targets = targets + [(x, y_target_p), (x_target_p, y), (x_target_p, y_target_p),]
        targets = targets + [(x_target_m, y_target_p), (x_target_p, y_target_m)]
        results = self.scan(targets, item)
        return(results)
    
    def direction_determine(self, value):
        final = 0
        if(value > 1):
            final = 1
        elif(value < 1):
            final = -1
        return(final)

    def act(self):
        vector = []
        if(self.mode == 0):
            self.collect()
            rock_coor = self.look(Rock)
            if(rock_coor != ()):
                vector = [rock_coor[0][0], rock_coor[0][1]]
            else:
                vector = [1,1]
            vector = [1,1]
        elif(self.mode == 1):
            rover_loc = self.getter()
            x_raw = self.ship_position[0] - rover_loc[0]
            y_raw = self.ship_position[1] - rover_loc[1]
            x = self.direction_determine(x_raw)
            y = self.direction_determine(y_raw)
            vector = [x,y]
        self.move(vector, 1)

#-----TESTING OF ROVER CLASS-----
#test_rover = Rover([1,1], [0,1], 100)
#test_rover.move([1, -1], 3)
#test_rover.move([1, -1], 3)
#test_rover.move([1, -1], 3)
#test_rover.move([1, -1], 3)
#print(test_rover.getter())
#print(test_rover.battery_level)
#print(type(test_rover).__name__)