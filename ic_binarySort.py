import math

def binarySort(targetnum, sortedlist):
    indexFloor = 0
    indexCeiling = len(sortedlist) - 1

    count = 0

    print('mylist(' + str(len(sortedlist)) + ') = ' + str(myList))

    if targetnum == int(sortedlist[indexCeiling]):
        print("Found number in last index")
        return True

    while True:
        midIndex = indexFloor + (indexCeiling-indexFloor)//2
        print("floor= " + str(indexFloor) + " ceiling= " + str(indexCeiling) + " mid= " + str(midIndex))

        # bang on
        if targetnum == int(sortedlist[midIndex]):
            print("Found number")
            return True

        # num belongs to left half
        if targetnum < int(sortedlist[midIndex]):
            #indexFloor = unchanged
            indexCeiling = midIndex

        # num belongs to right half
        if targetnum > int(sortedlist[midIndex]):
            indexFloor = midIndex + 1
            #indexCeiling = unchanged

        # trawled through all
        if (indexCeiling - indexFloor) <= 0:
            return False

        count += count + 1
        if count > 20:
            break



#myList = ['0', '4', '5', '7', '9', '11', '15', '16', '20', '21', '23', '100', '104', '105', '107', '109', '111', '115', '116', '120', '121', '123']
myList = ['0', '4', '5', '7', '9', '11', '15', '16', '20', '21', '23', '100', '104', '105']

'''
for i in myList:
    print('------------' + i + '-----------------')
    print(str(binarySort(int(i), myList)))
'''

print(str(binarySort(101, myList)))
