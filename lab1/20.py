def sum_of_digits(N):
    if N <= 0:
        return None
    total = sum(int(digit) for digit in str(N))
    return total

# Example usage:
print(sum_of_digits(12345))
