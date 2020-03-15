import unittest

def mergeSortedList(leftList, rightList):
    # since list is already sorted, step one index at a time in both lists
    # compare and append smaller of the two into a new list
    # when one list runs out, copy the rest of the longer list as it is already sorted

    # complexity is O(n)
    print("mergeSortedList invoked with " + str(leftList) + " and " + str(rightList))
    l_Idx, r_Idx = 0, 0
    result = []
    while (l_Idx < len(leftList)) and (r_Idx < len(rightList)):
        # while indices of both lists are lower than the shorter list
        # step one at a time and copy smallest value to result
        if leftList[l_Idx] < rightList[r_Idx]:
            result.append(leftList[l_Idx])
            l_Idx += 1
            #print("L incremented to " + str(l_Idx))
        else:
            result.append(rightList[r_Idx])
            r_Idx += 1
            #print("R incremented to " + str(r_Idx))


    # if leftList runs out of indices, append remaining items to result
    for r in range(r_Idx, len(rightList)):
        result.append(rightList[r])


    # if rightList runs out of indices, append remaining items to result
    for l in range(l_Idx, len(leftList)):
        result.append(leftList[l])

    return result

# very important - divide and conquer of unsorted list
# 37.53 https://www.youtube.com/watch?v=6LOwPhPDwVc

# Complexity O(n*logn)

def merge_sort(myList):
    # base case
    if len(myList) < 2:
        print("list less than 2 " + str(myList))
        return myList[:]
    else:
        # divide list by calling itself
        middle = len(myList)//2
        print("----- mid point = " + str(middle) + " ------ list = " + str(myList[:middle]))
        left  = merge_sort(myList[:middle])
        print("Left  = " + str(left))
        right = merge_sort(myList[middle:])
        print("Right = " + str(right))

        # now conquer with merge sorted list
        return mergeSortedList(left, right)


print(merge_sort([9, 4, 0, 1, 6, 10, 1, 8]))


my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]
# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
#print(merge_lists(my_list, alices_list))
#print(mergeSortedList(my_list, alices_list))
#print(mergeSortedList([1, 3, 5, 7], [4, 8, 9]))

class Test(unittest.TestCase):
    def test_sample_list(self):
        actual = mergeSortedList([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19])
        expected = [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
        self.assertEqual(actual, expected)
    def test_empty_list1(self):
        actual = mergeSortedList([], [1, 5, 8, 12, 14, 19])
        expected = [1, 5, 8, 12, 14, 19]
        self.assertEqual(actual, expected)
    def test_different_sized_list(self):
        actual = mergeSortedList([3, 4, 6], [1, 5, 8, 12, 14, 19])
        expected = [1, 3, 4, 5, 6, 8, 12, 14, 19]
        self.assertEqual(actual, expected)

#unittest.main(verbosity=2)
