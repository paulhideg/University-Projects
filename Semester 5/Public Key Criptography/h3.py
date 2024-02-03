#Implement the following algorithm:
#Pollard's p algorithm. The implicit function will be f(x) = x^2 + 1,
#but it will also allow the use of a function f given by the user.

# Implementing Pollard's p algorithm
#
# Parameters:
# f (function): The function to be used for the algorithm.
# x0 (int): The initial value of x.
# y0 (int): The initial value of y.
# n (int): The number to be factored.
#
# Returns:
# int: The factor of n.

import math

def pollard_p(f, x0, y0, n):
    """
    This function implements Pollard's p algorithm.
    
    Parameters:
    f (function): The function to be used for the algorithm.
    x0 (int): The initial value of x.
    y0 (int): The initial value of y.
    n (int): The number to be factored.
    
    Returns:
    int: The factor of n.
    """
    
    # Defining the initial values
    x = x0
    y = y0
    d = 1
    
    # The algorithm
    while d == 1:
        x = f(x) % n
        y = f(f(y)) % n
        d = math.gcd(abs(x - y), n)
        #print(d)
    
    # Checking if the factor is trivial
    if d == n:
        return None
    # if factor is nontrivial, return it
    else:
        return d
    

# Testing the function
n = 8051
f = lambda x: (x ** 2 + 1) % n
x0 = 2
y0 = 2

factor = pollard_p(f, x0, y0, n)
print("n = "+ str(n))
print(f"Factor: {factor}")
