# PROBLEM 1
# Write a recursive function called 'Countdown' that takes a positive integer, and returns a string.
# The string returned counts down from the number passed in the parameter, down to 1.
# If 5  is passed, it should return the string "5 4 3 2 1".
# Use string concatenation to build return value.

def countdown(x):
    while x>1:
        return str(x) + ' ' + countdown(x-1)
    return str(x)

b = countdown(5)
print(b)

# PROBLEM 2
# Write a recursive function called 'Countup' that takes a positive integer parameter, and returns a string.
# The string returned counts up from 1 to that number.
# If 5 is passed, it should return the string "1 2 3 4 5".

def countup(x):
    while x>1:
        return countup(x-1) + ' ' + str(x)
    return str(x)

b = countup(5)
print(b)

# PROBLEM 3
# Write a recursive function called 'sum_countup' that takes integer paramter, and returns the sum of all integers
# from 1 to that number
# Input: 5; Output: 15 (1 + 2 + 3 + 4 + 5)

def sum_countup(x):
    while x>1:
        return sum_countup(x-1) + x
    return x

b = sum_countup(5)
print(b)