def insert_shift_array(arr, val):
    return_arr = []
    middle = 0
    # set middle value
    if len(arr) % 2 == 0:
        middle = len(arr) / 2
    else:
        middle = len(arr) / 2 + 0.5

    # append val
    for i in range(len(arr) + 1):    # arr has new val so arr+1
        if i < middle:               # index left of middle
            return_arr.append(arr[i])
        elif i == middle:            # if index is the middle value append val and index
            return_arr.append(val)
            return_arr.append(arr[i])
        elif i > middle and i < len(arr):  # index to the right of middle
            return_arr.append(arr[i])
    return return_arr
