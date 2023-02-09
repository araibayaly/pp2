def rev_sen(sent):
    return " ".join(sent.split()[::-1])

s=str(input())
print(rev_sen(s))