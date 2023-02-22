import datetime 

def fivedays():
  x = datetime.datetime.now()
  i=0
  for i in range(3) :
   y = datetime.datetime(x.year, x.month, x.day - 1+i)
   print(y)
   i=+1

fivedays()