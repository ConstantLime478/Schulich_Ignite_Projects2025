class Player:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        
    def move(self, x_change, y_change):
        self.x += x_change
        self.y += y_change

        