#1. Create union function
def unionize(s,t):
    j=set()
    for k in s:
        j.add(k)
    for i in t:
        j.add(i)
    return j

#2. Create intersect function
def intersect(s,t):
    j=set()
    for k in s:
        if k in t:
            j.add(k)
    return j

#3. Create symmetric difference function
def sym_diff(s,t):
    a = unionize(s,t)
    b = intersect(s,t)
    return a-b