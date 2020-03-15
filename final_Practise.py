def binarySearch(mylist, l, r, val):

    # if zero length, don't bother
    if len(mylist) == 0: return False

    # while l <= r, iterate
    while l <= r:
        mid = l + (r - l) // 2
        print("l = " + str(l) + ", r = " + str(r) + ", mid = " + str(mid))
        # if mid value matches, return True
        if (mylist[mid] == val): return True
        elif (mylist[mid] < val): l = mid + 1
        else: r = mid - 1

    # return False, after recursing
    return False


#print(binarySearch([0, 4, 5, 7, 8, 9, 10, 12], 0, 7, 13))
#print(binarySearch([], 0, 0, 13))


def bubbleSort(myList):

    # walk through list
    for i in range(len(myList)):
        # look at i and i+1 element, swap
        idx = 0
        activeLen = len(myList) - 1
        while idx < activeLen:
            if myList[idx] > myList[idx + 1]:
                temp = myList[idx]
                myList[idx] = myList[idx + 1]
                myList[idx + 1] = temp
            idx += 1
        print(myList)


bubbleSort([1, 4, 2, 10, 2, 8, 9, 5])