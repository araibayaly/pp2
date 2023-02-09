from itertools import permutations 

def per(string):
    pers = [''.join(p) for p in permutations(string)]
    return pers

in_string=input("Enter string:")
res=per(in_string)
print("Permutations of the given string:")
for perm in res:
    print(perm)