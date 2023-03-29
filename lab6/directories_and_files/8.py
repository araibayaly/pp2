import os 
os.chdir("/Users/lord/Desktop/pp2/lab6/pp_practice")

open("todelete.txt", 'a').close()
print(os.listdir())

p="/Users/lord/Desktop/pp2/lab6/pp_practice"
os.remove(p)

print(os.listdir())