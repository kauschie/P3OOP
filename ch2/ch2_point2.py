import math

class Point():
    def __init__(self, x=0, y=0):
        """Initialize the poisition of a new point. The x and y
        coordinates can be specified. If they are not, the
        poinit defaults to the origin."""
        self.move(x,y)
    
    def move(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0,0)
    
    def calculate_distance(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        pythreturn distance