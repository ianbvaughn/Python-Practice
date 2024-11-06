# 1. every_other: takes list param, returns list that contains every other element, starting with first element.
"""
Use step iteration and list comprehension.
We're only returning even elements, so we can just use mod(2).
"""
def every_other(s):
    return s[::2]
p = ["parsley","sage","rosemary","thyme"]
print(every_other(p))

# 2. array_sum: takes list of string, returns total number of characters in all strings
"""
for s in list, return sum of len(s).
"""
def array_sum(s):
    x = 0
    for i in s:
        x += len(i)
    return x
r = ["Wayne", "Katie", "Daryl", "Dan"]
print(array_sum(r))

# 3. rev_string_list: takes list of string, returns list that contains reverse of each strings
# Use list comprehension.
"""
Need to use list comprehension to iterate through each element of list.
"""
def rev_string_list(s):
    x = [n[::-1] for n in s]
    return x
r = ["Wayne", "Katie", "Daryl", "Dan"]
print(rev_string_list(r))

# 4. contain_string: takes list of string, and target string, returns list of strings from original list that contain target string.
# Use list comprehension.
def contain_string(a,b):
    return [n for n in a if b in n]
f = ['cats', 'tacks', 'scat', 'stack']
g = 'cat'
print(contain_string(f,g))