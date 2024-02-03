# Solve the problem from the third set here
# 15. Generate the largest perfect number smaller than
# a given natural number n. If such a number does not exist,
# a message should be displayed.

def div_sum(n):  # calculates the sum of divisors
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s


def perfect_check(n, x):  # checks if the number is perfect
    global found
    if found == 0:
        s = div_sum(n)
        if s == n:
            found += 1
            print("Largest perfect number lower that is", n)


found = 0
n = int(input("Insert number:"))
while found == 0 and n != 1:  # searches for perfect numbers lower
    n = n-1  # than the given number
    perfect_check(n, found)
if found == 0:
    print("There's no natural perfect number lower than the given number")


"""""

perfect = (2305843008139952128, 137438691328,
           8589869056, 33550336, 8128, 496, 28, 6)  # the first 8 perfect numbers
number = int(input('Type number:'))
i = 0
ver = 0
while ver == 0 and i != 8:  # iterates through the perfect numbers tuple
    if number > perfect[i]:  # if the given number is bigger than a perfect number,
        ver = 1  # it displays the appropiate message
        print("Largest perfect number lower than", number, "is", perfect[i])
    else:
        i += 1
if ver == 0:
    print("There's no natural perfect number lower than", number)
"""
