import re

txt=input()
x=re.findall('[A-Z][a-z]*',txt)

list=[]
for i in x:
 list.append(i.lower())

print(*list, sep='_')