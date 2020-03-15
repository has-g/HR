import unittest

def searchInSortedList(myList, e):
    if len(myList) == 0:
        # empty list
        return False
    elif (e > myList[-1]) or (e < myList[0]):
        # element is greater than the last element in the list, not here
        # or element is smaller than the smallest element in the list
        return False

    mid = len(myList) // 2
    print("mid = " + str(mid) + " element = " + str(myList[mid]))

    if myList[mid] == e:
        print("Found at mid value ")
        return True
    elif myList[mid] > e:
        # left zone
        print("search left < " + str(myList[:mid]))
        return searchInSortedList(myList[:mid], e)
    elif myList[mid] < e:
        # right zone
        print("search right > " + str(myList[mid:]))
        return searchInSortedList(myList[mid:], e)
    else:
        print("else block?? why?")

    print("end of the queue from list " + str(myList))
    #return False


class Test(unittest.TestCase):
    def test_zero_list(self):
        actual = searchInSortedList([], 3)
        expected = False
        self.assertEqual(actual, expected)

    def test_mid_list(self):
        actual = searchInSortedList([3, 4, 6, 10, 11, 15], 6)
        expected = True
        self.assertEqual(actual, expected)

unittest.main(verbosity=2)


#myList = [3, 4, 6, 10, 11, 15]
#print(myList)
#print(searchInSortedList(myList, 6))