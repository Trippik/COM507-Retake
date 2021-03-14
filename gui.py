import tkinter as tk
from spaceship import Spaceship
from rover import Rover
from rock import Rock
from simulation import Simulation
import time

class Gui(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Mars Simulation")
        self.canvas_size = [400, 400]
        self.c = tk.Canvas(self, width=self.canvas_size[0], height=self.canvas_size[1])
        self.c.pack()
        self.set = 10
        self.sim_size = [10,10]
        self.sim = Simulation(self.sim_size, 3, 25)
        self.f_index = 0 # index so we know which frame to draw next
        # array to hold our frame data,
        # you'll probably need this to hold more than
        # just a set of coordinates to draw a line...
        self.icon_dimension = [0, 0, 40, 40] 

        for num in range(0, 400, 5): # make up a set of fake data
            self.icon_dimension.append([num, num, num+10, num+10])

    def iterate(self):
        results = self.sim.run(1)
        final = []
        print("Ship Inventory: " + str(len(self.sim.ship.inventory)) + "/25")
        print("Collected Rocks: " + str(len(self.sim.ship.collected_rocks)) + "/25")
        for result in results:
            agent_type = result[0]
            coordinates = result[1]
            data_0 = ((self.canvas_size[0] / self.sim_size[0]) * coordinates[0]) + self.icon_dimension[0]
            data_1 = ((self.canvas_size[1] / self.sim_size[1]) * coordinates[1]) + self.icon_dimension[1]
            data_2 = ((self.canvas_size[0] / self.sim_size[0]) * coordinates[0]) + self.icon_dimension[2]
            data_3 = ((self.canvas_size[1] / self.sim_size[1]) * coordinates[1]) + self.icon_dimension[3]
            final = final + [[agent_type,[data_0, data_1, data_2, data_3]],]
        return(final)

    def next_frame(self):
        results = self.iterate()
        self.c.delete('all') # clear canvas
        for result in results:
            agent = result[0]
            data = result[1]
            if(type(agent) is Spaceship):
                fill_colour = "black"
            elif(type(agent) is Rock):
                fill_colour = "dark violet"
                if(agent in self.sim.ship.inventory):
                    fill_colour = "white"
            elif(type(agent) is Rover):
                fill_colour = "dark green"
            self.c.create_rectangle(data[0], data[1], data[2], data[3], outline="black", fill=fill_colour) # draw new frame data
        
        self.f_index += 1 # increment frame index
        if (self.f_index >= len(self.icon_dimension)): # check and wrap if at end of sequence
            self.f_index = 0
        self.c.after(2000, self.next_frame) # call again after 50ms

if __name__ == "__main__":
    app = Gui()
    app.next_frame() # called manually once to start animation
    # could be started with 'after' instead if desired
    app.mainloop()