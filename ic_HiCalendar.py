import unittest

def HiCalendar(myList):
    # sort out on first index
    myListSorted = sorted(myList, key=lambda x: x[0])

    print(myListSorted)

    lengthofList = len(myListSorted)

    # create a new list
    myNewList = []
    skipIndex = -1

    for x in range(0, lengthofList-1):
        if x == skipIndex:
            continue

        CurrCalItem = myListSorted[x]
        NextCalItem = myListSorted[x+1]

        print('Index(' + str(x) + ") current item = " + str(CurrCalItem))

        # if current calendar items 'end' time extends beyond next calendar item's 'start' time
        if CurrCalItem[1] >= NextCalItem[0]:
            # meeting within meeting: if current calendar items 'end' time extends even beyond next calendar item's 'end' time
            if CurrCalItem[1] > NextCalItem[1]:
                newEndTime = CurrCalItem[1]
            else:
                newEndTime = NextCalItem[1]
            myTuple = (CurrCalItem[0], newEndTime)
            myNewList.append(myTuple)
            skipIndex = x+1
        else:
            myNewList.append(CurrCalItem)
            #myNewList.append(NextCalItem)


    return(myNewList)

#myList = [(0,1), (3,5), (4,8), (10,12), (9,10)]
#HiCalendar(myList)

# Tests

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = HiCalendar([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)
    def test_meetings_touch(self):
        actual = HiCalendar([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)


    def test_meeting_contains_other_meeting(self):
        actual = HiCalendar([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)


    def test_meetings_stay_separate(self):
        actual = HiCalendar([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

"""
        def test_multiple_merged_meetings(self):
            actual = HiCalendar([(1, 4), (2, 5), (5, 8)])
            expected = [(1, 8)]
            self.assertEqual(actual, expected)

        def test_meetings_not_sorted(self):
            actual = HiCalendar([(5, 8), (1, 4), (6, 8)])
            expected = [(1, 4), (5, 8)]
            self.assertEqual(actual, expected)

        def test_one_long_meeting_contains_smaller_meetings(self):
            actual = HiCalendar([(1, 10), (2, 5), (6, 8), (9, 10), (10, 12)])
            expected = [(1, 12)]
            self.assertEqual(actual, expected)

        def test_sample_input(self):
            actual = HiCalendar([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
            expected = [(0, 1), (3, 8), (9, 12)]
            self.assertEqual(actual, expected)

"""


unittest.main(verbosity=1)
