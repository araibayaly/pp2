import re 

string=str(input())
x=re.findall(r"\ba\w*b",string)

if x:
    print(x)
    print("Match found!")
else:
    print("Match not found.")