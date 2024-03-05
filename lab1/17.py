def printNumbers(N):
    if N <= 0:
        print("Error: N must be a positive integer.")
        return
    for i in range(N + 1):
        print(i)
printNumbers(5)
