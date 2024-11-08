# 1. insert_front(list[]): add value to front of list, should mutate the original list.

def insert_front(a,val):
    """Inserts value to 0 index of list"""
    a.insert(0,val)
b = [1,2,3]
insert_front(b,4)
print(b)

# 2. delete_last(list[]): delete last value of list

def delete_last(a):
    """Delete last value of list"""
    del a[len(a)-1]
c = [1,2,3]
delete_last(c)
print(c)