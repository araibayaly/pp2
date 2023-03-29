import os 
p="/Users/lord/Desktop/pp2/lab6/pp_practice"

if os.access(p, os.F_OK):
    print(f"The path '{p}'exists")
else:
   print(f"The path {p} does not exist")

if os.access(p, os.R_OK):
    print(f"The path {p} is readable")
else:
    print(f"The path {p} is not readable")

if os.access(p, os.W_OK):
    print(f"The path {p} is writable")
else:
    print(f"The path {p} is not writable")

if os.access(p, os.X_OK):
    print(f"The path {p} is executable")
else:
    print(f"The path {p} is not executable")