#-----IMPORT NECESSARY CLASSES AND LIBRARIES-----
import base_classes.agent as agent

#ROCK CLASS
class Rock(agent.Agent):
    def __init__(self, rock_position, energy):
        self.energy = energy
        super().__init__(rock_position[0], rock_position[1])
    
    #Drop energy level by set amount
    def energy_drop(self, drop_rate):
        if(self.energy > drop_rate):
            self.energy = self.energy - drop_rate
    
    def act(self):
        self.energy_drop(2)
