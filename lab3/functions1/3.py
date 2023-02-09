def sol(heads, legs):
    for chicks in range(heads + 1):
        rabs = heads - chicks
        if chicks*2 + rabs*4 == legs:
            return(chicks, rabs)
    return (None, None)
    
heads=int(input())
legs=int(input())
print(sol(heads, legs))