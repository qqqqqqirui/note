def cube_root(N):
    if N == 0:
        return 0
    elif N < 0:
        return None
    guess = 1
    while guess**3 <= N:
        if guess**3 == N:
            return guess
        guess += 1
    return N

print(cube_root(27))
