def even(n):
    for i in range(n):
        if(i%2==0):
            yield i

k=int(input())
for i in even(k):
    print(i)

