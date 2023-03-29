import os 
po="/Users/lord/Desktop/pp2/lab6/pp_practice/list.txt"
pc="/Users/lord/Desktop/pp2/lab6/pp_practice/copy.txt"
with open(po, "r") as origin:
    with open(pc, "w") as copy:
        for l in origin:
            copy.write(l)

with open(pc, 'r') as copy:
    print(copy.read())