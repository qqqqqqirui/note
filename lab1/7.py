def sumDigit(number):
    try:
        assert len(str(number))<=3
    except:AssertionError
    l=list(map(int, list(str(number))))
    return sum(l)
