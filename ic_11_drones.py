def findsingledrone(lst):
    lstlen = len(lst)

    for i in range(lstlen):
        for j in range(lstlen - 1):
            if lst[j] > lst[j+1]:
                temp = lst[j]
                lst[j] = lst[j+1]
                lst[j+1] = temp
        print(lst)

    for x in range(lstlen):
        if lst[x] != lst[x+1]:
            return lst[x+1]
        x += 1
        print('>> ' + str(x))

def findsingledrone2(lst):
    lst.sort()
    for i in range(len(lst)):
        if lst[i] != lst[i+1]:
            return lst[i+1]
        i += 1

def findsingledrone3(lst):
    mydict = {}
    for i in range(len(lst)):
        if lst[i] in mydict:
            value = mydict[lst[i]]
            mydict[lst[i]] = value + 1
        else:
            mydict[lst[i]] = 1

    for x, y in mydict.items():
        if y == 1: return x

#print(findsingledrone([2, 4, 9, 3, 2, 16, 4, 13, 9, 13, 16]))
#print(findsingledrone2([2, 4, 9, 3, 2, 16, 4, 13, 9, 13, 16]))

print(findsingledrone3([2, 4, 9, 3, 2, 16, 4, 13, 9, 13, 16]))