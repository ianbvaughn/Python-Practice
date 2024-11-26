# A decorator is effectively a way to create functionality that can be extended to children functions.
# For example, let's say that we wanted to log every function called. Instead of copying the same lines of code
# to every function, we could just create a decorator which executes this same code, along with the function
# being passed to it.

# Decorator

def outer_func(func): #passing a function as a parameter. this is the function we want to decorate
    def inner_func(): #this is the function that will execute
        print("Start Wrapper.")
        func() #this is our parameter function
        print("End Wrapper.")
    return inner_func #we're returning the function to be executed.

# Method 1

def say_hi(): #defining a function that is going to be decorated
    print("Function being decorated.")

test = outer_func(say_hi) #outer_func is a function that when executed, will execute the inner function.
test() #this is us executing outer_func, which will run the inner function with our parameter function (say_hi)

# Method 2

@outer_func #defining the decorator (wrapper function) that we want to use
def say_bye(): #defining a function that is going to be decorated
    print("Another function being decorated.")

say_bye()