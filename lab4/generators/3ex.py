def divby3and4(n):
  i=0
  while i <= n :
    if (i%3==0 and i%4==0) :
      yield i
    i=+1
print(list(divby3and4(60)))