import re 

match=[]
txt=str(input())
x=re.findall("ab*",txt)

for i in x:
  k=str(i).count('b')
  if k>=0 and k<=3:
     match.append(i)
  
if match:
    print(match)
    print("Match found!")
else:
    print("Match not found!")