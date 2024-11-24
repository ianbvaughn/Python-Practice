def factorial(x):
    y = x
    while x>1:
        y *= x-1
        x-=1
    return y