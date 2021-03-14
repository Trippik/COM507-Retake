#-----IMPORT NECESSARY CLASSES AND LIBRARIES-----
from agent import Agent
from rover import Rover

#SPACESHIP CLASS
class Spaceship(Agent):
    def __init__(self, ship_position):
        self.inventory = []
        self.collected_rocks = []
        super().__init__(ship_position[0], ship_position[1])
    
    #Scan specifc cell for rover, if found empty inventory and recharge
    def scan(self, targets):
        agents = self.environment.get_agents()
        for target in targets:
            for agent in agents:
                agent_coor = agent.getter()
                if((target == agent_coor) and (type(agent) is Rover)):
                    if(agent.inventory != None):
                        print("Rock Delivered to Spaceship")
                        self.inventory = self.inventory + [agent.inventory, ]
                        agent.inventory = None
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
        print("Spaceship Scanning")
        self.scan_charge()

#-----TESTING OF SPACESHIP CLASS-----
#import mars
#test_mars = mars.Mars()
#test_mars.set_size(5,5)
#test_ship = Spaceship([0,0])
#test_ship.set_environment(test_mars)
#test_rover = rover.Rover([1,1], test_ship.getter(), 20)
#test_rover.set_environment(test_mars)
#print(test_rover.battery_level)
#test_ship.scan_charge()
#print(test_rover.battery_level)
#test_rover.move([-1,0], 2)
#print(test_rover.battery_level)
#test_ship.scan_charge()
#print(test_rover.battery_level)