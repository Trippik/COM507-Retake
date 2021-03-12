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
        self.c = tk.Canvas(self, width=400, height=400)
        self.c.pack()
        self.set = 10
        self.sim = Simulation([10,10], 3, 2)
        self.f_index = 0 # index so we know which frame to draw next
        # array to hold our frame data,
        # you'll probably need this to hold more than
        # just a set of coordinates to draw a line...
        self.f_data = [0, 0, 40, 40] 

        for num in range(0, 400, 5): # make up a set of fake data
            self.f_data.append([num, num, num+10, num+10])

    def iterate(self):
        results = self.sim.run(1)
        final = []
        for result in results:
            agent_type = result[0]
            coordinates = result[1]
            data_0 = self.f_data[0] + (self.set * coordinates[0])
            data_1 = self.f_data[1] + (self.set * coordinates[1])
            data_2 = self.f_data[2] + (self.set * coordinates[0])
            data_3 = self.f_data[3] + (self.set * coordinates[1])
            final = final + [[agent_type,[data_0, data_1, data_2, data_3]],]
        return(final)

    def next_frame(self):
        results = self.iterate()
        self.c.delete('all') # clear canvas
        for result in results:
            agent_type = result[0]
            data = result[1]
            if(agent_type is Spaceship):
                fill_colour = "black"
            elif(agent_type is Rock):
                fill_colour = "dark violet"
            elif(agent_type is Rover):
                fill_colour = "dark green"
            self.c.create_rectangle(data[0], data[1], data[2], data[3], outline="black", fill=fill_colour) # draw new frame data
        self.f_index += 1 # increment frame index
        if (self.f_index >= len(self.f_data)): # check and wrap if at end of sequence
            self.f_index = 0
        self.c.after(50, self.next_frame) # call again after 50ms

if __name__ == "__main__":
    app = Gui()
    app.next_frame() # called manually once to start animation
    # could be started with 'after' instead if desired
    app.mainloop()