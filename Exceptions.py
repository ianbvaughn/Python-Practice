class CustomError(Exception):
    pass

try:
    raise NameError("Name Error")
except NameError:
    print("Exception")
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("You must enter an integer.")
except Exception as e:
    print(e)
finally:
    print("All exceptions have been handled.")