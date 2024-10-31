def factorial(x):
    y = x
    while x>1:
        y *= x-1
        x-=1
    return y

a = int(input('Enter a positive integer: '))
b = factorial(a)
print('The factorial of ' + str(a) + ' is ' + str(b))