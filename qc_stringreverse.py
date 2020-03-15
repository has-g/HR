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
'''
def reverseString1(mystr):
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

def reverseString(mystr):
    strlen = len(mystr)

    # check for zero string
    if strlen == 0: return -1

    # check for single char
    if strlen == 1: return mystr

    tempword = ''
    tempstr = ''

    for i in range(strlen - 1, -1, -1):
        if ((mystr[i] == ' ') or (i == -1)):
            print('tempword = ', tempword)
            for j in range(len(tempword) - 1, -1, -1):
                #print(tempword[j])
                tempstr += tempword[j]
            tempstr += ' '
            tempword = ''
        else:
            tempword += mystr[i]

    # handle for the final non-null value
    print(tempword)
    return tempstr

print(reverseString('This is a length'))