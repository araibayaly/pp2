import re 

string=input()
x=re.sub('\s|,|\.',':',string)

print(x)