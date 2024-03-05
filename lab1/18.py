def factorial(N):
    if N < 0:
        return None
    result = 1
    for i in range(1, N + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120 (5!)
