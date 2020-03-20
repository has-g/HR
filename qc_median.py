"""
find median in a stream

Assumptions:
1. optimising for speed or space? Speed
2. inputting values by hand?
3. sanity checks for inputted values? convert to value = float(value)
4.


input value
make a mList in memory,
every update with value; merge two sorted lists and update mList
    - sort() - python provided
    - merge two sorted lists O(nlogn)
    - split lists and rebalance O(n)?
                - split into two lists lower and upper
                    - maintain (insert into list) and rebalance the lists as items added
                        - (effectively half the insert length)
                    - equal lists: median = (lower(-1) + upper(0))/2
                    - unequal list: median = lower(-1) if lower, upper(0) if upper

print out median
"""

def mergeSortedLists(list1, list2):
    if len(list1) == 0: return list2
    if len(list2) == 0: return list1

    l1 = 0
    l2 = 0
    mylist = []
    for _ in range(len(list1) + len(list2)):
        if l1 == len(list1):
            # list1 exhausted, copy list2
            mylist.append(list2[l2])
            l2 += 1
        elif l2 == len(list2):
            # list2 exhausted, copy list1
            mylist.append(list1[l1])
            l1 += 1
        elif list1[l1] <= list2[l2]:
            mylist.append(list1[l1]) # O(1) time
            l1 += 1
        elif list1[l1] > list2[l2]:
            mylist.append(list2[l2]) # O(1) time
            l2 += 1
        else:
            print('no idea why im here')

    return mylist

def SortList(mylist):
    # complexity is O(n) in breaking down lists
    # merge sorted list is another O(logn)
    # combined is O(nlogn)
    if len(mylist) <= 1: return mylist

    lenlist = len(mylist)
    mid = lenlist//2

    # break it down to single digits
    left = SortList(mylist[:mid])
    right = SortList(mylist[mid:])

    return mergeSortedLists(left, right)

print(SortList([3, 6, 3, 5, 0, 33, 1, 5]))

def median(mylist):
    # edge cases: zero length list, median = None
    if len(mylist) == 0: return None

    if len(mylist) == 1: return mylist[0]

    mid = len(mylist)//2

    if len(mylist)%2 == 1:
        # odd list
        return mylist[mid]
    else:
        # even list
        a = mylist[mid]
        b = mylist[mid - 1]
        return (a + b)/2

gList = []
value = input('Input a number (hit return to exit):')
value = float(value)
gList.append(value)

while value != "":
    value = input('Input a number (hit return to exit):')
    value = float(value)
    gList.append(value)
    gList = SortList(gList)

    print(gList)
    print('median = ', median(gList))

