def primes(N):
    if N < 2:
        return
    for num in range(2, N + 1):
        if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
            print(num)


primes(20) 
