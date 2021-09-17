def sort_array(source_array):
    sortOdd_array = []
    for val in source_array:
        if val % 2 != 0:
            #odd
            sortOdd_array.append(val)

    sortOdd_array.sort()
    sortOdd_counter = 0
    retval_array = []

    for val in source_array:
        if val % 2 != 0:
            #odd
            retval_array.append(sortOdd_array[sortOdd_counter])
            sortOdd_counter += 1
        else:
            #even
            retval_array.append(val)
    return retval_array