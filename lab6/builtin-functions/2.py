a = input()
up = 0
low = 0
for i in a:
  up+=int(i.isupper())
  low+=int(i.islower())

print(up, low, sep="\n")
