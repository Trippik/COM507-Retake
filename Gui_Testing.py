import tkinter
from spaceship import Spaceship
from rover import Rover
from rock import Rock

class gui:
    def __init__(self, sim, canvas_size):
        self.sim = sim
        sim_dimensions = self.sim.mars.get_size()
        width = canvas_size[0]
        height = canvas_size[1]
        block_x = width / sim_dimensions[0]
        block_y = height / sim_dimensions[1]
        self.block_size = [block_x, block_y]
        self.top = tkinter.Tk()
        self.C = tkinter.Canvas(self.top, bg="saddle brown", height=height, width=width)
    
    def block_coor_generate(self, location):
        top_coor = [location[0] * self.block_size[0], location[1] * self.block_size[1]]
        bottom_coor = [top_coor[0] + self.block_size[0], top_coor[1] + self.block_size[1]]
        return((top_coor, bottom_coor))

    def refresh_items(self):
        self.C.delete(all)
        agents = self.sim.mars.get_agents()
        for agent in agents:
            location = agent.getter()
            raw = self.block_coor_generate(location)
            top_coor = raw[0]
            bottom_coor = raw[1]
            if(type(agent) is Spaceship):
                self.C.create_rectangle(top_coor[0], top_coor[1], bottom_coor[0], bottom_coor[1],outline="slate gray", fill="slate gray")
            elif(type(agent) is Rover):
                self.C.create_rectangle(top_coor[0], top_coor[1], bottom_coor[0], bottom_coor[1],outline="green3", fill="green3")
            elif(type(agent) is Rock):
                self.C.create_rectangle(top_coor[0], top_coor[1], bottom_coor[0], bottom_coor[1],outline="dark violet", fill="dark violet")

    
    def draw(self):
        self.C.pack()
        self.top.mainloop()