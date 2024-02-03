import timeit
import math

# Euclidean Algorithm for GCD
def euclidean_gcd(a, b):
    # The loop continues until b becomes 0
    while b:
        # Swap the values of a and b
        a, b = b, a % b
    # Return the gcd
    return a

# Binary GCD Algorithm for GCD
def binary_gcd(a, b):
    # Base cases for recursion
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    # If a is even
    if a % 2 == 0:
        # If b is odd
        if b % 2 == 1:
            return binary_gcd(a // 2, b)
        else:
            # Both a and b are even
            return binary_gcd(a // 2, b // 2) * 2
    # If b is even
    if b % 2 == 0:
        return binary_gcd(a, b // 2)
    # If a is greater than b
    if a > b:
        return binary_gcd((a - b) // 2, b)
    # If b is greater than a
    return binary_gcd(a, (b - a) // 2)

# Extended Euclidean Algorithm for GCD for arbitrary size numbers
def extended_euclidean_gcd(a, b):
    # Base case for recursion
    if a == 0:
        return (b, 0, 1)
    else:
        # Recursive call
        g, x, y = extended_euclidean_gcd(b % a, a)
        # Return the gcd and the coefficients of Bézout's identity
        return (g, y - (b // a) * x, x)

# Comparative running-time analysis
inputs = [(0, 678), (999, 1111), (1234, 8910), (12345, 98765),
          (10**10, 2**20), (10**5, 2**10), (10**10, 2**10), (10**20, 2**10),
          (10**30, 2**10), (10**40, 2**10)]

algorithms = [euclidean_gcd, binary_gcd, extended_euclidean_gcd]

# Loop over all algorithms
for algo in algorithms:
    print(f"Timing for {algo.__name__} algorithm:")
    # Loop over all input pairs
    for a, b in inputs:
        # Compute the gcd
        result = algo(a, b)
        # Measure the time taken
        time_taken = timeit.timeit(lambda: algo(a, b), number=1000)
        # If the result is a tuple (for extended_euclidean_gcd)
        if isinstance(result, tuple):
            print(f"GCD of {a} and {b}: {result[0]}, Time taken: {time_taken:.6f} seconds")
        else:
            # For euclidean_gcd and binary_gcd
            print(f"GCD of {a} and {b}: {result}, Time taken: {time_taken:.6f} seconds")
    print()
