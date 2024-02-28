import functools
def quadProd3(a, b, c):
    newlist=list(map(lambda x: pow(x, 2), [a, b, c]))
    result=functools.reduce((lambda m, n: m*n), newlist)
    return result
print(quadProd3(1, 2, 3))