def highestProduct(list_of_ints):
    # a1 a2 a3 - variables first 3 in the list
    a1 = list_of_ints[0]
    a2 = list_of_ints[1]
    a3 = list_of_ints[2]


    # assign them from lowest to highest value
    for i in range(3):
        if a1 > a2:
            temp = a1
            a1 = a2
            a2 = temp
        elif a2 > a3:
            temp = a2
            a2 = a3
            a3 = temp

    print(str(a1))
    print(str(a2))
    print(str(a3))


    # walk through list from 4
    for x in list_of_ints[3:]:
        if x > a3:
            a1 = a2
            a2 = a3
            a3 = x
            print("a3 = " + str(a3))
        elif x > a2:
            a1 = a2
            a2 = x
            print("a2 = " + str(a2))
        elif x > a1:
            a1 = x
            print("a1 = " + str(a1))
    return a1*a2*a3

def highestProduct_novice(list_of_ints):
    # optimised for space sort() sorts the same list, sorted(listname) creates a copy
    list_of_ints.sort()
    print(list_of_ints)
    last_idx = len(list_of_ints) - 1
    return list_of_ints[last_idx] * list_of_ints[last_idx - 1] * list_of_ints[last_idx - 2]

def highestProduct_bubblesort(list_of_ints):
    list_len = len(list_of_ints) - 1
    for i in range(list_len):
        for j in range(list_len):
            if list_of_ints[j] < list_of_ints[j+1]:
                temp = list_of_ints[j]
                list_of_ints[j] = list_of_ints[j+1]
                list_of_ints[j+1] = temp
    print(list_of_ints)
    return list_of_ints[0] * list_of_ints[1] * list_of_ints[2]


#list_of_ints = [2, -1, -2, 5, 1, 9, 4]
list_of_ints = [-10, 1, 3, 2, -10]
print(highestProduct(list_of_ints))
##print(highestProduct_novice(list_of_ints))
#print(highestProduct_bubblesort(list_of_ints))

# minimum list of 3 = Yes
# negatives = yes
# optimising for space or time? = time

# solutions - bubble sort then take last 3
# O(nlogn) - runtime
# O(1) - space

# a1 a2 a3 - variables first 3 in the list
# walk through list from 4
# if x > a3, then a3 = elementx : elif x > a2 then a2 = x: elif x > a1 then a1 = x: else: continue
# return a1*a2*a3
# O(n) - runtime
# O(1) - space
