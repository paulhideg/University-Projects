# Solve the problem from the second set here
# 9. The palindrome of a number is the number obtained by
# reversing the order of its digits.

# First, i converted the input given to a string
n = str(input("Enter a number:"))
print(n[::-1])  # This is a common and idiomatic way to reverse a string / list,
# and since the palindrome of a number is the number written backwards,
# this approach was the first that came to my mind
