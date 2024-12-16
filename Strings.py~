#1. Write a function called last_char that takes a string parameter and returns the last letter of that string.
"""
def last_char(a):
 return a[-1]

str = input("Enter a string: ")
print(last_char(str))
"""

#2. Write a function called midstring that takes a string parameter and returns a copy of that string minus its first and last letters. 
# If the string passed in has only has 1 or 2 letters, the function should return the empty string "".
"""
def midstring(a):
 b = a[1:]
 return b[:-1]

str = input("Enter a string: ")
print(midstring(str))
"""
#3. Write a function called sort_two_strings that takes two string parameters and returns a single string of both of them in dictionary order, ignoring case. 
# For example, if the strings "aardvark" and "Zebra" are passed, it should return "aardvark Zebra".
"""
def sort_two_strings(a,b):
 a_lower = a.lower()
 b_lower = b.lower()
 c = ''
 if a_lower<b_lower:
  c=a+b
 elif a_lower>b_lower:
  c=b+a
 else:
  c=a+b
 return c

str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
print(sort_two_strings(str1,str2))
"""
#4. A palindrome is a string that reads the same forward or backward. Write a function called is_pal that takes a string parameter and returns True if that string is a palindrome, but returns False otherwise.
def is_pal(a):
 k = 0
 for i in a:
  if i == a[-1-k]:
   continue
  else:
   print(a + ' is not a palindrome')
   break
  k+=1
 
str = input("Enter a string: ")
is_pal(str)