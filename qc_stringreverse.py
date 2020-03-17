'''
1. Reverse words in a  string. "This is a girl" becomes "girl a is This".
Reverse the string completely. Then reverse every word.

2. Calculate nth Fibonacci number. Optimize it.
Did it with recursion. Optimized using DP
see tutorials

see ic_6_Fibonnaci.py
'''

'''
1. what are we optimising for? Time or space?
2. assumptions: non empty string or list
3. Do you expect inplace or out of place manipulation
4. assumption: delimiter = ' ' 
5. assumption: no leading or trailing spaces?
'''

#(A)
#BRUTE FORCE APPROACH
# Overall = O(n) runtime, space = O(1)


def bf_reversewords(mystr):
    if len(mystr) <= 1: return mystr
    # e.g. "This is a girl" o/p => "girl a is This"

    # edge case of space at beginning or end of string, retain the space for later

    # split the list into constituent words ['This' 'is' 'a' 'girl']
    mywords = mystr.split()

    temp = ''
    mywords = []

    # O(n) runtime
    # space = O(1)
    for j in range(len(mystr)):
        if mystr[j] != ' ':
            temp += mystr[j]
        elif (mystr[j] == ' '):
            mywords.append(temp)
            mywords.append(' ')
            temp = ''
        else:
            print('whoa!')
    mywords.append(temp)

    print('mywords = ', mywords)

    # create new string
    mynewstr = ''

    # O(n) runtime
    # space = O(n)
    # step back from end to beginning
    for i in range(len(mywords) - 1, -1, -1):
        # make up the new string sentence
        mynewstr += mywords[i]
        #mynewstr += ' '

    return mynewstr

print(bf_reversewords("This is a girl"))

print(===============)

def reverseString(mystr):
    strlen = len(mystr)

    # check for zero string
    if strlen == 0: return -1

    # check for single char
    if strlen == 1: return mystr

    tempword = ''
    tempstr = ''

    for i in range(strlen - 1, -1, -1):
        if mystr[i] != ' ':
            tempword += mystr[i]
        else:
            print('tempword = ', tempword)
            for j in range(len(tempword) - 1, -1, -1):
                #print(tempword[j])
                tempstr += tempword[j]

            tempstr += ' '
            tempword = ''

    # handle for the final non-null value
    print(tempword)
    for k in range(len(tempword) - 1, -1, -1):
        tempstr += tempword[k]

    return tempstr

def swapStringInPlace(mylist, lidx, ridx):
    '''
    # 0 and single value
    if len(myL) == 0: return myL
    if len(myL) == 1: return myL

    # very important - this is in-place list manipulation
    if ((lidx < 0) or (ridx > len(myL) - 1)): return
    '''

    print('received l = ', lidx, ' r = ', ridx)
    while lidx < ridx:
        mylist[lidx], mylist[ridx] = mylist[ridx], mylist[lidx]
        lidx += 1
        ridx -= 1

def stringreverse(mylist):
    # 0 and single value
    if len(mylist) == 0: return
    if len(mylist) == 1: return

    mylistlen = len(mylist) - 1
    swapStringInPlace(mylist, 0, mylistlen)
    print(mylist)

    # Complexity
    # O(n) time and O(1) space!

    lidx = 0

    for i in range(len(mylist) + 1):
        if (i == len(mylist) or (mylist[i] == ' ')):
            swapStringInPlace(mylist, lidx, i - 1)
            print(mylist)
            lidx = i + 1

#print(reverseString('This is a length'))
mylist = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 's', 't', 'r', 'i', 'n', 'g']
stringreverse(mylist)
print(mylist)
'''
swapStringInPlace(mylist, 6, 6)
print(mylist)

swapStringInPlace(mylist, 9, 10)
print(mylist)
'''