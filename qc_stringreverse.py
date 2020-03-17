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

print('===============')

# OPTION B
# O(1) Space optimised, since string is manipulated in place

def swapString(mystr, l, r):

    while l < r:
        mystr[l], mystr[r] = mystr[r], mystr[l]
        l += 1
        r -= 1

myList = ['T', 'h', 'i', 's', ' ', 'i', 's', ' ', 'a', ' ', 'b', 'o', 'y']
#swapString(mystr, 0, len(mystr) - 1)
print("mystr = ", myList)
print('===============')


def reverseList(mystr):
    strlen = len(mystr)

    if strlen <= 1: return mystr

    # swap the original string
    swapString(mystr, 0, strlen - 1)
    print(myList)

    # now step through and reverse those that are within spaces or end of list
    l = 0
    r = 0
    for i in range(len(mystr) + 1):
        if (i == len(mystr)):
            #print('final l = ', l, ' r = ', i - 1)
            swapString(mystr, l, i - 1)
            break
        elif (mystr[i] == ' '):
            #print('l = ', l, ' r = ', i - 1)
            swapString(mystr, l, i - 1)
            l = i + 1
        else:
            pass



reverseList(myList)
print(myList)
print('..........')

