import math

def square(N):
 x=math.floor(math.sqrt(N))
 for i in range(x):
    s=pow(i,2)
    yield s

for s in square(16):
    print(s)