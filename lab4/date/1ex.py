import datetime 

def fivedays():
  x = datetime.datetime.now()
  y = datetime.datetime(x.year, x.month, x.day - 5)
  print(y)

fivedays()