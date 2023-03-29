import os 
p="/Users/lord/Desktop/pp2/lab6/pp_practice"
fad=os.listdir(p)
for i in fad:
    if os.path.isdir(os.path.join(p, i)):
     print(i)
print()

for i in fad:
    print(i)

for i in fad:
    if os.path.isfile(os.path.join(p,i)):
        print(i)
