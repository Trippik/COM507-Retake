from simulation import Simulation
from Gui_Testing import gui
import time

sim = Simulation([10,10], 4, 20)
window = gui(sim, [600,600])
window.refresh_items()
window.draw()
sim.run(1)
time.sleep(5)
window.refresh_items
window.draw()