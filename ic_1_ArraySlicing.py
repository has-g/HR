import unittest

def ReverseString(myList):

    listLength = len(myList)

    # do an int division to floor the value
    midvalue = listLength//2
    #print('midvalue = ' + str(midvalue) + ' listLength = ' + str(listLength))

    for item in range(0, midvalue):
        # copy away to temp location, and assign new value from other idx + mid
        temp = myList[item]
        myList[item] = myList[listLength - 1 - item]
        # copy temp to offset value
        myList[listLength - 1 - item] = temp
        #print('swapping ' + temp + ' from(' + str(item) + ') to (' + str(listLength - 1 - item) + ')')

    print(myList)

ReverseString(['s', 't', 'r', 'i', 'n', 'g'])
ReverseString(['s', 'n', 'a', 'r', 'e'])
ReverseString(['s'])
ReverseString([])

class Test(unittest.TestCase):
    def test_even_string(self):
        actual = ReverseString(['s', 't', 'r', 'i', 'n', 'g'])
        expected = ['g', 'n', 'i', 'r', 't', 's']
        self.assertEqual(actual, expected)
#unittest.main(verbosity=1)