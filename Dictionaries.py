#1. Create a dictionary which maps numbers in English->Spanish
eng_to_span={
    "one":"uno",
    "two":"dos",
    "three":"tres",
    "four":"quatro",
    "five":"cinco",
    "six":"seis",
    "seven":"siete",
    "eight":"ocho",
    "nine":"nueve",
    "ten":"diez"
}
#2. Create a function which prints all key-value pairs of a dictionary param.
def print_dict(d):
    for i,k in d.items():
        print(i,k)
#3. Create a function which returns a dictionary of the perfect squares of all integers from 1 to n inclusive.
def some_squares(n):
    s = {}
    for j in range(1,n+1):
        s[j]=pow(j,2)
    return s