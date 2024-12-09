def logger(i):
    def _orig_logs():
        print("Verbosity Level: ", i)
    return _orig_logs #The inner function is what gets returned! Now, I can execute it with the params of my choice
                      #whenever I want.

level_3_logger = logger(3)
level_3_logger()

def logs(i):
    return print("Verbosity Level: ", i)

level_3_logger = logs(3) #This doesn't accomplish the same thing, since 'logs' doesn't return anything!