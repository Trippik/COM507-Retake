import tkinter
from spaceship import Spaceship
from rover import Rover
from rock import Rock
import time

class Gui:
    def __init__(self, sim, canvas_size):
        self.sim = sim
        self.canvas_size = canvas_size
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window, bg="saddle brown", height=self.canvas_size[1], width=self.canvas_size[0])
        self.canvas.pack()
        self.window.mainloop()