class Point():
    # the x=0 specifies a default value for the parameter
    def __init__(self, x=0, y=0):
        self.move(x,y)

    def move(self, x, y):
        self.x = x
        self.y = y
    
    def reset(self):
        self.move(0, 0)
    
# constructing a Point
point = Point(3,5)
print(point.x, point.y)