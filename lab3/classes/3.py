class Rectangle():
    def __init__(self, length, width):
     self.length = length
     self.width = width
    
    def area(self):
        Area = self.width * self.length
        print(Area)

shape = Rectangle(7,4) 
shape.area() 