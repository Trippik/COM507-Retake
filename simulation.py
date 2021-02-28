#-----IMPORT NECESSARY CLASSES AND LIBRARIES-----
from random import seed
from random import randint
import mars
import rock
import rover
import spaceship

#-----BASIC FUNCTIONS-----
def generate_coordinates(max_x, max_y):
    rand_x = randint(0, max_x)
    rand_y = randint(0, max_y)
    return([rand_x, rand_y])

#SIMULATION CLASS
class Simulation:
    def __init__(self, mars_size, no_rovers, no_rocks):
        self.mars = mars.Mars()
        self.mars.set_size(mars_size[0], mars_size[1])
        ship_coor = generate_coordinates(mars_size[0], mars_size[1])
        self.ship = spaceship.Spaceship(ship_coor)
        self.ship.set_environment(self.mars)
        while(no_rovers > 0):
            rover_coor = generate_coordinates(mars_size[0], mars_size[1])
            rover_new = rover.Rover(rover_coor, ship_coor, 100)
            rover_new.set_environment(self.mars)
            no_rovers = no_rovers - 1
        while(no_rocks > 0):
            rock_coor = generate_coordinates(mars_size[0], mars_size[1])
            rock_new = rock.Rock(rock_coor, 50)
            rock_new.set_environment(self.mars)
            no_rocks = no_rocks - 1
    
    #Complete 1 cycle of actions on all agents in simulation
    def run(self, loops):
        agents = self.mars.get_agents()
        while(loops > 0):
            for agent in agents:
                agent.act()
            loops = loops - 1

#-----TESTING OF SIMULATION CLASS-----
#test_sim = Simulation([5,5], 1, 1000)
#test_sim.run(10)
#print(str(test_sim.ship.inventory))
