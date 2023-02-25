import re 

txt=str(input())
x=re.findall("[a-z]*_",txt)
print(x)
if x:
    print("Match found!")
else:
    print("Match not found.")
