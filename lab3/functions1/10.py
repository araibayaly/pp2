def unique(l):
    uni = []
    for i in l:
        if i not in uni:
            uni.append(i)
    return uni

print(unique([1, 3, 3, 5, 6, 5]))