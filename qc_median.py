def findMedian(lst):
    listlen = len(lst)
    if listlen == 0:
        return None

    lst.sort()
    #print("lst = ", lst)
    if listlen % 2 == 0:
        # even
        a = lst[listlen//2]
        b = lst[listlen//2 - 1]
        return (a+b)/2.0
    else:
        # odd
        return lst[listlen//2]


print(findMedian([-30, 1, 2, 4, 7, 8, 1]))
#print(findMedian([1, 2]))
#print(findMedian([-30, 7, 8, 1, 100]))


def linearmedian(lst):
    listlen = len(lst)
    if listlen == 0:
        return None
    elif listlen == 1:
        return lst[0]
    elif listlen == 2:
        return (lst[0] + lst[1])/2.0

    mylist = sorted(lst[0:3])
    print("median holder list = ", mylist)
    evenlist = True
    for i in lst[3:]:
        if evenlist:
            # list size is even numbers - so median = average of middle two
            print("even number ", i)
            if i < mylist[0]:
                # no change to median list
            elif i == mylist[0]:

            elif (i > mylist[0]) && (i < mylist[1]):

            elif i == mylist[i]:

            elif (i > mylist[1]) && (i < mylist[2]):

            elif i == mylist[2]:

            elif i > mylist[2]:


            evenlist = False

        else:
            # list size is odd numbers - so median = middle number

            print("odd number ", i)

            evenlist = True



linearmedian([-30, 1, 2, 4, 7, 8, 1])