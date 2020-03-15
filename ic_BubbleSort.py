#import unittest

def bubbleSort(myList):
    # complexity O(n**2) = quadratic
    flag = False

    while not flag:
        print(myList)
        flag = True
        for idx in range(1, len(myList)):
            if myList[idx] < myList[idx-1]:
                flag = False
                # swap
                temp = myList[idx -1]
                myList[idx - 1] = myList[idx]
                myList[idx] = temp
                print("Dealt with swapping " + str(myList[idx-1]) + " with " + str(myList[idx]))



def bubbleSort2(myList):
    activelen = len(myList)
    count = 0
    for i in range(activelen):
        print("> " + str(myList) + " count(" + str(count) + ")" + " activelen = " + str(activelen))
        for idx in range(1, len(myList)):
            if myList[idx] < myList[idx-1]:
                # swap
                temp = myList[idx -1]
                myList[idx - 1] = myList[idx]
                myList[idx] = temp
            count += 1

        activelen -= 1



'''
class Test(unittest.TestCase):
    def test_case_regular(self):
        actual = bubbleSort([1, 6, 9, 4, 3, 8])
        expected = [1, 3, 4, 6, 8, 9]
        self.assertEqual(actual, expected)

unittest.main(verbosity=1)
'''
#myList = [10, 6, 9, 4, 3, 8, 4, 2, 1]
myList = [1, 3, 5, 7, 2, 6, 25, 18, 13]
bubbleSort(myList)
#bubbleSort2(myList)
