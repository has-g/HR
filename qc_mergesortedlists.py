'''
6. Coding problem: Merge 2 sorted list.

**** see ic_1_GirlScoutCookie_mergeSubLists

7. Follow up: Merge k sorted list.  


1. two lists
2. each sorted low to high
3. What are we optimising for? Rumtime?
4. equal lengths or unequal
5. Zero sized lists
6.
'''

def mergeSortedLists(l1, l2):
    global a
    a = l1 + l2 # fixed length space O(1)
    a.sort() # in-place sort, time complexity = O(nlogn) bubble sort going over n times
a = []
l1 = [1, 4, 6, 9]
l2 = [1, 2, 5, 8, 12]
mergeSortedLists(l1, l2)

"""

l1 = [1, 4, 6, 9]
      ^
      l

l2 = [1, 2, 5, 8, 12]
      ^
      r

# edge cases = 0 list(s)
# go over entire length of sum of two lists
# while l+r <= len(l1+l2) -2
# if el(l) <= el(r): then append to new list, l+=1
# elif el(l) > el(r): then append to new list, r+=1
# elif l1 list is exhausted l==len(l1) - 1: append l2 to new list, r+=1
# elif l2 list is exhausted l==len(l2) - 1: append l1 to new list, l+=1
"""

def mergeSortedListsEfficient(l1, l2):
    # edge cases = 0 list(s) - if both 0 lengths then also true
    if len(l1) == 0: return l2
    if len(l2) == 0: return l1

    l = 0
    r = 0
    mylist = []

    for _ in range(len(l1) + len(l2)):
        if l >= len(l1):
            # elif l1 list is exhausted l==len(l1): append l2 to new list, r+=1
            mylist.append(l2[r])
            r += 1
        elif r >= len(l2):
            # elif l2 list is exhausted l==len(l2): append l1 to new list, l+=1
            mylist.append(l1[l])
            l += 1
        elif l1[l] <= l2[r]:
            # if el(l) <= el(r): then append to new list, l+=1
            mylist.append(l1[l])
            l += 1
        elif l1[l] > l2[r]:
            # elif el(l) > el(r): then append to new list, r+=1
            mylist.append(l2[r])
            r += 1
        else:
            print("not sure why im here")

    return(mylist)

l1 = [1, 4, 6, 9]
l2 = [1, 2, 5, 8, 12]
print(mergeSortedListsEfficient(l1, l2))

def mergeKlists(listofL):
    lenL = len(listofL)
    print(lenL)
    a = []
    for i in range(lenL):
        print('list=', listofL[i])
        a = mergeSortedListsEfficient(a, listofL[i])
        print('a=', a)
    return a

print(mergeKlists([[1, 2], [3, 4], [6, 7], [1, 4, 5, 6]]))