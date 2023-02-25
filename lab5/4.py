import re 

txt=str(input())
x=re.findall("[A-Z][a-z]*",txt)
list=[]
for i in x:
    if len(i) > 2 :
        list.append(i)
if list:
    print(list)
    print("Match found!")
   
else:
    print("Match not found.")
