from random import choice

s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
def choose_word(t):
    """
    Chooses a pseudo-random word from a string input.
    """
    r = choice([i for i in range(0,len(t.split())-1)])
    return t.split()[int(r)]
rand_word=choose_word(s)
print(rand_word)