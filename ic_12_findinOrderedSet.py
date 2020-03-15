"""
Suppose we had a list ↴ of nn integers sorted in ascending order.
How quickly could we check if a given integer is in the list?

In an ordered set we can do a search of O(log n) since we can split
the set and search in each half
"""

def contains(mylist, num):
    listlen = len(mylist)
    if listlen == 1 and mylist[0] == num: return True

    l = 0
    r = listlen - 1

    while l <= r:
        mid = l + (r - l)//2
        print('mid = ' + str(mid))
        if num == mylist[mid]:
            return True
        elif num > mylist[mid]:
            # right side
            l = mid + 1
        elif num < mylist[mid]:
            r = mid - 1
        else:
            print('whoa!')
            return False
    print('exhausted while loop')
    return False

#print(contains([-100, -55, -45, -1, 3, 5, 7, 9, 40, 41, 42, 44, 55], -100))
print(contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
