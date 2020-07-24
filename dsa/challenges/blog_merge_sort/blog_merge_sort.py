def merge_sort(my_list):
    if len(my_list) > 1:
        mid = len(my_list) // 2 #
        left = my_list[:mid] # :stop at mid
        right = my_list[mid:] # start at mid :

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0

        # Iterator for the main list
        k = 0

        while i < len(left) and j < len(right): # ensures each list hasnt ended
            if left[i] < right[j]:
              # The value from the left half has been used
              my_list[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                my_list[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            my_list[k] = left[i] # new index at k itteration is now value at left i
            i += 1
            k += 1

        while j < len(right):
            my_list[k]=right[j]
            j += 1
            k += 1
    return my_list

if __name__ == "__main__":
    my_list = [54,26,93,17,77,31,44,55,20]
    merge_sort(my_list)
    print(my_list)




