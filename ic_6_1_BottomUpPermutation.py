def perm(argstr, mylist = []):
    if len(argstr) == 1:
        x = mylist.append(argstr)
        print(x)
        return x
    al = argstr[0]
    str1 = argstr[1:]
    count = 0
    for i in range(len(str1) + 1):
        mystr = ""
        for j in range(len(str1)):
            if count == j: mystr += al
            mystr += str1[j]
        if count == len(str1): mystr += al
        mylist.append(mystr)
        count += 1

    newargstr = argstr[:-1]
    print('str len = ' + str(len(newargstr)) + ', list = ' + str(mylist))
    return perm(newargstr, mylist)

print(perm('tcb'))

def generateperm(str):
    return perm(str[0], mylist[1:])

#print(generateperm('abcd'))