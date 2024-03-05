def even(a,b,c):
    l=list(map(lambda x:(x+1)%2, [a,b,c]))
    return sum(l)
