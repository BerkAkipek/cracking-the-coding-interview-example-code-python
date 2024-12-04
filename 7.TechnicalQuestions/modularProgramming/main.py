def swap_min_max(arr):
    min_ind = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_ind]:
            min_ind = i
    max_ind = 0
    for j in range(len(arr)):
        if arr[i] > arr[max_ind]:
            max_ind = i
    temp = arr[min_ind]
    arr[min_ind] = arr[max_ind]
    arr[max_ind] = temp

# This function swaps the minimum and maximum values in array.
# Whole logic in a function generalize it make it more modular.

def swap(arr, ind1, ind2):
    arr[ind1], arr[ind2] = arr[ind2], arr[ind1]


def find_min_index(arr):
    min_ind = 0
    for i in range(len(arr)):
        if arr[i] < arr[min_ind]:
            min_ind = i
    return min_ind


def find_max_index(arr):
    max_ind = 0
    for i in range(len(arr)):
        if arr[i] > arr[max_ind]:
            max_ind = i
    return max_ind

# This wil reduce the whole function smaller chunks of elements which can be easily tested.
