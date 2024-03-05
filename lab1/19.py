def sum_of_numbers(N):
    if N <= 0:
        return None
    total = sum(range(1, N + 1))
    return total

# Example usage:
print(sum_of_numbers(5)) 
