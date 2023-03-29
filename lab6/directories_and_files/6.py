import os
p="/Users/lord/Desktop/pp2/lab6/pp_practice/folder"
up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for l in up:
  os.chdir(p)
  open(l+".txt", 'a').close()