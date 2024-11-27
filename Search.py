from time import time
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
my_arr = [i for i in range (10000)]
print(time())
index = binary_search(my_arr,5000,0,len(my_arr)-1)
print(index)
print(time())
index2 = linear_search(my_arr,10000)
end2 = time()
print(index2)
print(time())