class Point():
    def __init__(self, x0, y0):
        self.x= x0
        self.y= y0
    
    def show(self):
        print(self.x, self.y)
    
    def move(self, x1, y1):
        x = self.x + x1
        y = self.y + y1
        print(x,y)
    
    def dist(self, x2, y2):
        dist_x=x2-self.x
        dist_y=y2-self.y
        print((dist_x**2 + dist_y**2)**0.5)

point1 = Point(2,5)
point1.show()
point1.move(3,1)
point1.dist(7,8)

    