#-----IMPORT NECESSARY CLASSES AND LIBRARIES-----
import base_classes

class Mars(base_classes.Environment):
    pass

class Rover(base_classes.Agent):
    def __init__(self, rover_position, ship_position, battery_level):
        self.battery_level = battery_level
        self.ship_position = ship_position
        self.inventory = None
        super().__init__(rover_position[0], rover_position[1])
    
    def move(self, vector, battery_change):
        if(self.battery_level > battery_change):
            current_loc = self.getter()
            new_x = current_loc[0] + vector[0]
            new_y = current_loc[1] + vector[1]
            self.setter(new_x, new_y)
            self.battery_level = self.battery_level - battery_change

class Rock(base_classes.Agent):
    def __init__(self, rock_position, energy):
        self.energy = energy
        super().__init__(rock_position[0], rock_position[1])
    
    def energy_drop(self, drop_rate):
        if(self.energy > drop_rate):
            self.energy = self.energy - drop_rate

class Spaceship(base_classes.Agent):
    def __init__(self, ship_position):
        self.inventory = []
        super().__init__(ship_position[0], ship_position[1])
    
    def scan(self, targets):
        agents = self.environment.get_agents()
        for target in targets:
            for agent in agents:
                if((target == agent.getter()) and (type(agent).__name__) == Rover):
                    if(agent.inventory != None):
                        self.inventory = self.inventory + [agent.inventory, ]
                agent.battery_level = 100

    def scan_charge(self):
        ship_loc = self.getter()
        x = ship_loc[0]
        y = ship_loc[1]
        targets = []
        x_target_m = x - 1
        y_target_m = x - 1
        targets = targets + [(x, y_target_m), (x_target_m, y), (x_target_m, y_target_m),]
        x_target_p = x + 1
        y_target_p = x + 1
        targets = targets + [(x, y_target_p), (x_target_p, y), (x_target_p, y_target_p),]
        targets = targets + [(x_target_m, y_target_p), (x_target_p, y_target_m)]
        self.scan(targets)



#-----TESTING OF MARS CLASS-----
test_mars = Mars()
test_mars.set_size(5,5)
#print(test_mars.get_size())

#-----TESTING OF ROVER CLASS-----
#test_rover = Rover([1,1], [0,1], 100)
#test_rover.move([1, -1], 3)
#print(test_rover.getter())
#print(test_rover.battery_level)
#print(type(test_rover).__name__)

#-----TESTING OF SPACESHIP CLASS-----
#test_ship = Spaceship([0,0])
#test_ship.set_environment(test_mars)
#test_rover = Rover([1,1], test_ship.getter(), 20)
#test_rover.set_environment(test_mars)
#print(test_rover.battery_level)
#test_ship.scan_charge()
#print(test_rover.battery_level)
#test_rover.move([-1,0], 2)
#print(test_rover.battery_level)
#test_ship.scan_charge()
#print(test_rover.battery_level)
