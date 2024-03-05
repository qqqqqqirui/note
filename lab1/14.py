def intervalPlus(a,b,x):
    if x<a and x<b:
        return -1
    elif x<a and x>b:
        return 0
    elif x>a and x<b:
        return 0
    elif x>a and x>b:
        return 1