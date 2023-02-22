import math 

def area(n,l):
  a=float((pow(l,2)*n)/(4*math.tan(180/n)))
  return a

print(abs(area(6,3)))  