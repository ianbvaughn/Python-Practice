# Example of recursion at play

def countdown(n):
    if n<=0:
        print('Blast off!')
    else:
        print(n)
        countdown(n-1)

countdown(5)

class Point:
    """Represents a point in 2D space"""
    #define methods and variables

blank = Point()
blank.x = 3 #attributes are values assigned to an instance
print(blank.x)