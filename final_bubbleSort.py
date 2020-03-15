import unittest

def bubbleSort(arr):
    # find length of array
    arrlen = len(arr)
    # check limits with empty array or single element array
    if arrlen <= 1:
        return arr

    # do it n times

    for j in range(arrlen - 1):
        # for every element in array go over and swap
        for i in range(arrlen - 1):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
        print("> " + str(arr))


bubbleSort([2, 5, 1, 0, 6, 9, 0])
bubbleSort([13, 10])
print(bubbleSort([]))

