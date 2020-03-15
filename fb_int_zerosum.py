'''
print numbers in a list that add up to zero

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

    #print('exhausted list and not found')


'''
            if c in myset:
                print('found ', str(a), ' ', str(b), ' ', str(c))
            else:
                myset.add(c)

'''
print(sumZero([-3, -4, -5, 7, 8]))
