#-----IMPORT NECESSARY CLASSES AND LIBRARIES-----
from random import seed
from random import randint
from mars import Mars
from rock import Rock
from rover import Rover
from spaceship import Spaceship

#SIMULATION CLASS
class Simulation:
    def __init__(self, mars_size, no_rovers, no_rocks):
        self.mars = Mars()
        self.mars.set_size(mars_size[0], mars_size[1])
        ship_coor = [5,5]
        self.mars_size = mars_size
        self.ship = Spaceship(ship_coor)
        self.ship.set_environment(self.mars)
        while(no_rovers > 0):
            rover_coor = self.generate_coordinates()
            rover_new = Rover(rover_coor, self.ship, 100)
            rover_new.set_environment(self.mars)
            no_rovers = no_rovers - 1
        while(no_rocks > 0):
            rock_coor = self.generate_coordinates()
            rock_new = Rock(rock_coor, 50)
            rock_new.set_environment(self.mars)
            no_rocks = no_rocks - 1
    
    def generate_coordinates(self):
        rand_x = randint(0, (self.mars_size[0] - 2))
        rand_y = randint(0, (self.mars_size[1] - 2))
        return([rand_x, rand_y])

    #Complete 1 cycle of actions on all agents in simulation
    def run(self, loops):
        agents = self.mars.get_agents()
        while(loops > 0):
            for agent in agents:
                agent.act()
            loops = loops - 1
        agents = self.mars.get_agents()
        results = []
        for agent in agents:
            agent_location = agent.getter()
            results = results + [(agent, agent_location),]
        return(results)

#-----TESTING OF SIMULATION CLASS-----
#test_sim = Simulation([5,5], 1, 1000)
#test_sim.run(10)
#print(str(test_sim.ship.inventory))
#input()