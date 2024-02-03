# Solve the problem from the first set here
# First Set
# Generate the first prime number larger than a given natural number n.

n = int(input("Enter a number: "))
ver = 0
s = n
while (ver != 1):
    s = s + 1
    r = 0
    i = 2
    i = int(i)
    for i in range(2, s):
        if (s % i) == 0:
            r = r + 1
    if (r == 0):  # if the number has no divisors, then it's a perfect number
        print(s)
        ver = 1
