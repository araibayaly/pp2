import os 
p="/Users/lord/Desktop/pp2/lab6/pp_practice"
if os.access(p, os.F_OK):
    dir, f = os.path.split(p)
    print(f"The directory portion of the path is: {dir}")
    print(f"The filename portion of the path is: {f}")

else:
    print(f"The path {p} does not exist")