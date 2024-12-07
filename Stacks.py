s=[]
try:
    print(s[-1])
except IndexError as i:
    print(i,"Stack is Empty!")
print(s)