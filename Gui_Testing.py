import tkinter
from spaceship import Spaceship
from rover import Rover
from rock import Rock
import time

class gui:
    def __init__(self, sim, canvas_size):
        self.sim = sim
        sim_dimensions = self.sim.mars.get_size()
        width = canvas_size[0]
        height = canvas_size[1]
        block_x = width / sim_dimensions[0]
        block_y = height / sim_dimensions[1]
        self.block_size = [block_x, block_y]
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, bg="saddle brown", height=height, width=width)
        self.graphics = []
        self.build_graphics()
        self.canvas.pack()
        self.animation()
        self.window.mainloop()
    
    def initial_block_coor_generate(self, location):
        top_coor = [location[0] * self.block_size[0], location[1] * self.block_size[1]]
        bottom_coor = [top_coor[0] + self.block_size[0], top_coor[1] + self.block_size[1]]
        return((top_coor, bottom_coor))
    
    def block_coor_generate(self, location):
        coor = [location[0] * self.block_size[0], location[1] * self.block_size[1]]
        return(coor)

    def build_graphics(self):
        agents = self.sim.mars.get_agents()
        for agent in agents:
            location = agent.getter()
            coors = self.initial_block_coor_generate(location)
            top_coor = coors[0]
            bottom_coor = coors[1]
            if(type(agent) is Spaceship):
                new_graphic = self.canvas.create_rectangle(top_coor[0], top_coor[1], bottom_coor[0], bottom_coor[1], outline="black", fill="slate gray")
                print("Built a Spaceship")
            elif(type(agent) is Rover):
                new_graphic = self.canvas.create_rectangle(top_coor[0], top_coor[1], bottom_coor[0], bottom_coor[1], outline="black", fill="green3")
                print("Built a Rover")
            elif(type(agent) is Rock):
                new_graphic = self.canvas.create_rectangle(top_coor[0], top_coor[1], bottom_coor[0], bottom_coor[1], outline="dark violet", fill="dark violet")
                print("Built a Rock")
            self.graphics = self.graphics + [(new_graphic, agent),]
    
    def animation(self):
        self.sim.run(1)
        for item in self.graphics:
            if(type(item[1]) is Rover):
                location = item[1].getter()
                print(str(item[1]) + " moved")
                coor = self.block_coor_generate(location)
                self.canvas.move(item, coor[0], coor[1])
                self.canvas.update()
        self.window.after(2000, self.animation)
