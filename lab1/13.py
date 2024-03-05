def longerString(s1, s2):
    if len(s1)>len(s2):
        print(s1)
        return len(s1)-len(s2)
    elif len(s1)<len(s2):
        print(s2)
        return len(s2)-len(s1)
    else:
        return 0