from time import time
import math

my_arr = [i for i in range (10000)]

def binary_search(arr,target,low,high):
    mid=(low+high)//2
    if arr[mid]==target:
        return mid
    elif target<arr[mid]:
        return binary_search(arr,target,low,mid-1)
    elif target>arr[mid]:
        return binary_search(arr,target,mid+1,high)

def linear_search(arr,target):
    for i in arr:
        if i==target:
            return i
    return -1

def jump_search(arr,target):
    n=len(arr)
    m=int(math.sqrt(n))
    prev,curr=0,0
    while curr<=n and arr[curr]<=target:
        prev=curr
        curr+=m
    for i in range(prev,curr):
        if arr[i]==target:
            return i
    return -1

index = binary_search(my_arr,1000,0,len(my_arr)-1)
index2 = linear_search(my_arr,1000)
index3 = jump_search(my_arr,1000)
print(index)
print(index2)
print(index3)