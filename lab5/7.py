import re

txt=input()
x=re.split('_',txt)
camel=[]

for i in x:
  camel.append(i.title())

print(*camel, sep='')