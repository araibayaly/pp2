 
class string():

    def __init__(self, string):
       self.a = string
    
    def getString(self):
        print(self.a)

    def printString(self):
        b=self.a
        print(b.upper())

a=input()
word = string(a)
word.getString()
word.printString()
