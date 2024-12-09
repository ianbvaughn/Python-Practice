def selection_sort(arr):
    """Sort a list using the selection sort algorithm."""
    for j in range(len(arr)):
        for i in range(j+1,len(arr)):
            if arr[i]<arr[j]:
                arr[j],arr[i]=arr[i],arr[j]
    return arr