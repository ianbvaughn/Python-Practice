import math
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    arr = nums1 + nums2
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] <= arr[j + 1]:
                continue
            else:
                curr = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = curr
    if len(arr) % 2 == 1:
        print(arr[int(math.floor(len(arr) / 2))])
        return arr[int(math.floor(len(arr) / 2))]
    else:
        print(arr[int(len(arr)/2)-1])
        print(arr[int(len(arr)/2)])
        print((arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)])/2)
        return (arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)])/2
a1=[2,3]
a2=[1]
findMedianSortedArrays(a1,a2)