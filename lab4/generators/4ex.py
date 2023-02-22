def squares(a,b):
    for i in range(a,b+1):
        yield i*i

for d in squares(5,20):
    print(d)