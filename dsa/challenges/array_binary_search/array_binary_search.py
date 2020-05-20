# def binary_search(arr, key):
#     if key < len(arr) and key >= 0:
#         return arr[key]
#     elif key >= len(arr) or key < 0:
#         return -1


def binary_search(arr, key):
    lower_bound = 0
    upper_bound = len(arr) - 1

    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) / 2
        key_at_midpoint = arr[midpoint]

        if key < key_at_midpoint:
            upper_bound = midpoint - 1
        elif key > key_at_midpoint:
            lower_bound = midpoint + 1
        elif key == key_at_midpoint:
            return midpoint
        break


print(binary_search([1, 2, 3, 4, 5], 2))
