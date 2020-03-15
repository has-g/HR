'''
def merge_listsOld(myList, aliceList):
    # worst case O(n)
    fulllist = myList + aliceList
    # worst case O(nlogn) complexity
    return sorted(fulllist)
'''



    # create empty list newList

    # determine shorter list and determine length of this list

    # for each index

        # append newList with list of values in asc order

def merge_lists(myList, aliceList):


def enterIntoList(aList, number):
    # create empty list
    newList = []
    flag = 0

    if number >= aList[-1]:
        newList = aList
        newList.append(number)
    else:
        # loop through all elements in alist
        for x in aList:
            # if number < the nth indexed number, add to aList
            if (number < x) & (flag == 0):
                newList.append(number)
                flag = 1
            newList.append(x)

    return newList






my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
#print(merge_lists(my_list, alices_list))

print(enterIntoList(my_list, 6))
