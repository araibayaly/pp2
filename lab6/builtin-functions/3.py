a=input()
l=[i for i in a]
b=l.copy
b.reverse()
if b==a:
    print("Palindrome")
else:
    print("Not palindrome")