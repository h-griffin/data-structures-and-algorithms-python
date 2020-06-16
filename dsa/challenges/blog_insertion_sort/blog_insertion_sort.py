
def insertion_sort(array):

    for idx in range(1, len(array)):
        position = idx
        temp = array[idx]

        #check left less than val to move right // then move temp position left
        while position > 0 and array[position - 1] > temp:
            array[position] = array[position - 1]
            position = position - 1

        array[position] = temp
        
    return array


if __name__ == "__main__":
    sort = insertion_sort([8, 4, 23, 42, 16, 15])
    print(sort)


