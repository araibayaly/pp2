def pal(word):
    if word == word[::-1]:
     return True
    else: 
      return  False
    
word = str(input())
print(pal(word))
