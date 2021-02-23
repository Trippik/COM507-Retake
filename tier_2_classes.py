#-----IMPORT NECESSARY CLASSES AND LIBRARIES-----
import base_classes
from random import seed
from random import randint


#-----BASIC FUNCTIONS-----
def generate_coordinates(max_x, max_y):
    rand_x = randint(0, max_x)
    rand_y = randint(0, max_y)
    return([rand_x, rand_y])


#-----CLASSES-----
#MARS CLASS
class Mars(base_classes.Environment):
    pass


#ROVER CLASS
class Rover(base_classes.Agent):
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
        elif(self.mode == 1):
            rover_loc = self.getter()
            x_raw = self.ship_position[0] - rover_loc[0]
            y_raw = self.ship_position[1] - rover_loc[1]
            x = self.direction_determine(x_raw)
            y = self.direction_determine(y_raw)
            vector = [x,y]
        self.move(vector, 1)



#ROCK CLASS
class Rock(base_classes.Agent):
    def __init__(self, rock_position, energy):
        self.energy = energy
        super().__init__(rock_position[0], rock_position[1])
    
    #Drop energy level by set amount
    def energy_drop(self, drop_rate):
        if(self.energy > drop_rate):
            self.energy = self.energy - drop_rate
    
    def act(self):
        self.energy_drop(2)


#SPACESHIP CLASS
class Spaceship(base_classes.Agent):
    def __init__(self, ship_position):
        self.inventory = []
        super().__init__(ship_position[0], ship_position[1])
    
    #Scan specifc cell for Rover, if found empty inventory and recharge
    def scan(self, targets):
        agents = self.environment.get_agents()
        for target in targets:
            for agent in agents:
                agent_coor = agent.getter()
                if((target == agent_coor) and (type(agent) is Rover)):
                    if(agent.inventory != None):
                        self.inventory = self.inventory + [agent.inventory, ]
                        agent.mode = 0
                agent.battery_level = 100

    #Scan all cells within a 1 cell radius of the ship
    def scan_charge(self):
        ship_loc = self.getter()
        x = ship_loc[0]
        y = ship_loc[1]
        targets = ()
        x_target_m = x - 1
        y_target_m = x - 1
        targets = targets + ([x, y_target_m], [x_target_m, y], [x_target_m, y_target_m],)
        x_target_p = x + 1
        y_target_p = x + 1
        targets = targets + ([x, y_target_p], [x_target_p, y], [x_target_p, y_target_p],)
        targets = targets + ([x_target_m, y_target_p], [x_target_p, y_target_m],)
        self.scan(targets)
    
    def act(self):
        self.scan_charge()


#SIMULATION CLASS
class Simulation:
    def __init__(self, mars_size, no_rovers, no_rocks):
        self.mars = Mars()
        self.mars.set_size(mars_size[0], mars_size[1])
        ship_coor = generate_coordinates(mars_size[0], mars_size[1])
        self.ship = Spaceship(ship_coor)
        self.ship.set_environment(self.mars)
        while(no_rovers > 0):
            rover_coor = generate_coordinates(mars_size[0], mars_size[1])
            rover = Rover(rover_coor, ship_coor, 100)
            rover.set_environment(self.mars)
            no_rovers = no_rovers - 1
        while(no_rocks > 0):
            rock_coor = generate_coordinates(mars_size[0], mars_size[1])
            rock = Rock(rock_coor, 50)
            rock.set_environment(self.mars)
            no_rocks = no_rocks - 1
    
    #Complete 1 cycle of actions on all agents in simulation
    def run(self, loops):
        agents = self.mars.get_agents()
        while(loops > 0):
            for agent in agents:
                agent.act()
            loops = loops - 1
        

#-----TESTING OF MARS CLASS-----
#test_mars = Mars()
#test_mars.set_size(5,5)
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

#-----TESTING OF SIMULATION CLASS-----
test_sim = Simulation([5,5], 1, 100)
test_sim.run(10)
print(str(test_sim.ship.inventory))
