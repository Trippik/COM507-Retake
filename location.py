class Location:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def getter(self):
        return([self.x, self.y])

    def setter(self, new_x, new_y):
        self.x = new_x
        self.y = new_y