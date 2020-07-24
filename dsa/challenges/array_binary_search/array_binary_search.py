
def binary_search(arr,x):
    low = 0
    high = len(arr)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:    #is x at mid
            low = mid + 1
        elif arr[mid] > x:  #if x greater dont look left
            high = mid -1
        else:               #if x smaller dont look right
            return mid
    return -1



