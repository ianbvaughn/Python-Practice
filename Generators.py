def fib(limit):
    a,b=0,1
    while b<limit:
        yield b #on each iteration, returns current value of 'b'
        a,b=b,a+b

for i in fib(10):
    print(i)