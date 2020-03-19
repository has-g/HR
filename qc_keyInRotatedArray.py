"""
1. Search in Rotated Sorted Array

2. practice a regular binary search as well

[0, 2, 5, 6, 8, 9, 11]
|       |            |
l       m           r

# mid = l + (r - l)//2
# l = 0, r = len(list) - 1
# while l < r:
# if x < list[mid]: this is lower half, move right pointer to mid
# if x > list[mid]: x is in upper half, move left pointer to mid
# if x == list[mid]: return index
# else: all exhausted return -1
"""

def binSearch(x, mylist):
    if len(mylist) == 0:
        print('empty, x does not exist in empty list')
        return -1
    # x isn't an int

    l = 0
    r = len(mylist) - 1

    while l < r:
        mid = l + (r - l)//2

        if x < mylist[mid]:
            # if x < list[mid]: this is lower half, move right pointer to mid
            r = mid - 1
        elif x > mylist[mid]:
            # if x > list[mid]: x is in upper half, move left pointer to mid
            l = mid + 1
        elif x == mylist[mid]:
            # if x == list[mid]: return index
            return mid
        else:
            # else: all exhausted return -1
            print('why am i here?')

    return -1

print(binSearch(2, [0, 2, 5, 6, 8, 9, 11]))
print(binSearch(33, [0, 2, 5, 6, 8, 9, 11]))

print("------------------")
"""
[8, 9, 11, 13, 17, 21, 0, 2, 5, 6]
 ^              ^                ^
 l              m                r

# if list[m] > list[r]: then lower half is ok, inflection is to the right, so move l to m
[8, 9, 11, 13, 17, 21, 0, 2, 5, 6]
                ^         ^     ^
                l         m     r
# if list[m] < list[l]: then lower half is not ok, inflection point to left, move r to m
[8, 9, 11, 13, 17, 21, 0, 2, 5, 6]
                ^   ^    ^
                l   m    r
# if list[m] == list[l]: return m
"""

def checkRotationPoint(mylist):
    # zero length list
    if len(mylist) == 0: return -1

    # single item list
    if len(mylist) == 1: return 0

    # two item list, return whichever is less
    if len(mylist) == 2: return min(mylist[0], mylist[1])

    l = 0
    r = len(mylist) - 1

    while l < r:
        m = l + (r - l)//2
        if m == r:
            print('found r ', m)
            return m
        elif m == l:
            print('found l ', m)
            return m + 1
        elif mylist[m] > mylist[r]:
            l = m
            print('l<', l, " r=", r, " m=", m)
        elif mylist[m] < mylist[r]:
            r = m
            print('l=', l, " r<", r, " m=", m)
        else: print('not sure why?')

    return -1

mylist = [9, 11, 13, 14, 17, 21, 1, 2, 5, 6]
a = checkRotationPoint(mylist)
print('key[', a, '] = ', mylist[a])

#print(checkRotationPoint([0, 2, 5, 6, 8, 9, 11, 13, 14, 17, 21]))
#print(checkRotationPoint([2, 5, 6, 8, 9, 11, 13, 14, 17, 21, 0]))
"""
[8, 9, 11, 13, 14, 17, 21, 0, 2, 5]
 ^              ^                ^
                ^       ^        ^
                        ^  ^     ^
                        ^  ^
"""