import tkinter
from simulation import Simulation

def block_size(sim_dimensions, height, width):
    block_x = width / sim_dimensions[0]
    block_y = height / sim_dimensions[1]
    return([block_x, block_y])

sim_dimensions = [10,10]
sim = Simulation(sim_dimensions, 1, 1000)
top = tkinter.Tk()
height = 600
width = 600

C = tkinter.Canvas(top, bg="blue", height=height, width=width)
b = tkinter.Button(top, text="Cycle Simulation", command = sim.run(1))

coord = 10, 50, 240, 210
block_size = block_size(sim_dimensions, height, width)
arc = C.create_rectangle(0, 0, block_size[0], block_size[1],
    outline="#fb0", fill="#fb0")


C.pack()
b.pack()
top.mainloop()