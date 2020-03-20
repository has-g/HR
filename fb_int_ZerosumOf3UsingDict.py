'''
print numbers in a list that add up to zero

BEST option = https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/
has all 3 options of solving this - MUST SEE
'''

def sumZero(mylist):
    listlen = len(mylist)
    if listlen < 3:
        print('none')
    elif listlen == 3:
        if (mylist[0] + mylist[1] + mylist[2] == 0):
            print('found in listlen of 3: ' + str(mylist[0]) + ' ' + str(mylist[1]) + ' ' + str(mylist[2]))
            return True
        else:
            return ('none')

    myset = set()

    for i in range(listlen):
        a = mylist[i]
        for j in range(i, listlen):
            b = mylist[j]
            c = 0 - (a + b)
            for k in range(j, listlen):
                if c == mylist[k]:
                    print('found ', str(a), ' ', str(b), ' ', str(c))


print(sumZero([-3, -4, -5, 7, 8]))

# sort the list first and then iterate L and R from both ends
# Complexity O(n**2) time and O(1) space
'''
1. Sort all element of array
2. Run loop from i=0 to n-2.
     Initialize two index variables l=i+1 and r=n-1
4. while (l < r) 
     Check sum of arr[i], arr[l], arr[r] is
     zero or not if sum is zero then print the
     triplet and do l++ and r--.
5. If sum is less than zero then l++
6. If sum is greater than zero then r--
7. If not exist in array then print not found.
'''

def FindSumZero(mylist):
    # checks for lists < 3
    if len(mylist) < 3: return []

    # create list of list empty to return
    returnlist = []

    # checks for list == 3
    if len(mylist) == 3:
        if mylist[0] + mylist[1] + mylist[2] == 0:
            returnlist.append(mylist)
            return returnlist
        else:
            return []

    n = len(mylist)

    # sort the list in-place
    mylist.sort()

    # for loop 0 to n-2 of given list
    for i in range(n-2):
        # create two pointers l=i+1 and r=n-1
        # note: the two pointers are just outside the range i would traverse
        l = i + 1
        r = n - 1

        while l < r:
            total = mylist[i] + mylist[l] + mylist[r]
            #print('total = ', total)
            if total == 0:
                # if i+l+r = 0, populate return list, l += 1, r -= 1
                returnlist.append([mylist[i], mylist[l], mylist[r]])
                l += 1
                r -= 1
            elif total < 0:
                # if i+l+r < 0, l +=1
                l += 1
            elif total > 0:
                # if i+l+r > 0, r -=1
                r -= 1
            else:
                print('not sure why Im here')

    return returnlist


print(FindSumZero([-3, -4, -5]))
print(FindSumZero([-3, -4]))
print(FindSumZero([-3, -4, 7]))
print(FindSumZero([0, -1, 2, -3, 1]))
print(FindSumZero([-3, -4, -5, 7, 8, 9]))
print('-----------end of FindSumZero--------------')
# Run a loop from i=0 to n-2
#   Create an empty hash table
#   Run inner loop from j=i+1 to n-1
#       If -(arr[i] + arr[j]) is present in hash table
#          print arr[i], arr[j] and -(arr[i]+arr[j])
#       Else
#          Insert arr[j] in hash table.
# O(n**2) runtime, O(n) space

def FindSumZeroUsingDictionary(mylist):
    n = len(mylist)
    # checks for lists < 3
    if n < 3: return []

    # create list of list empty to return
    returnlist = []

    # checks for list == 3
    if n == 3:
        if mylist[0] + mylist[1] + mylist[2] == 0:
            returnlist.append(mylist)
            return returnlist
        else:
            return []

    for i in range(n-1):
        # for i from 0 to n-1
        myset = set()
        for j in range(i+1, n):
            x = 0 - (mylist[i] + mylist[j])
            # search in dict
            if x in myset:
                returnlist.append([mylist[i], mylist[j], x])
            else:
                # else create a key with x and element does not matter
                myset.add(mylist[j])

    return returnlist

print(FindSumZeroUsingDictionary([-3, -4, -5]))
print(FindSumZeroUsingDictionary([-3, -4]))
print(FindSumZeroUsingDictionary([0, -1, 2, -3, 1]))
print(FindSumZeroUsingDictionary([-3, -4, 7]))
print(FindSumZeroUsingDictionary([-3, -4, -5, 7, 8, 9]))