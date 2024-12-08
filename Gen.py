def generator():
    t=1
    print('First result is ',t)
    yield t #Pauses on first iteration.

    t+=1
    print('Second result is ',t)
    yield t

exec_gen = generator() #We've stored the function call as a variable.
next(exec_gen)
next(exec_gen)

my_other_generator = (num**2 for num in range(10)) #Creates generator object that we can iterate through.

def other_generator_alt():
    num=1
    while num<10:
        yield print(num**2)
        num+=1

e = other_generator_alt()

for j in e:
    try:
        next(e)
    except StopIteration:
        print("End of Iterable.")