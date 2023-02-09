class Shape() :
    def __init__ (self):
        self.area=0
    
    def area_1(self):
        print(self.area)

class Square():
    def __init__(self, a):
        self.a=a

    def area_2(self):
        self.area=self.a*self.a
        print(self.area)

house1=Shape()
house1.area_1()
house2=Square(10)
house2.area_2()