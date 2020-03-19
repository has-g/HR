'''
8. Given an array of non-negative integers, you are initially positioned at the
first index of the array. Each element in the array represents your maximum jump length
at that position.Determine if you are able to reach the last index.
Example 1:
Input: [2,3,1,1,4] = True
Input: [3,2,1,0,4] = False
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.


i    j   value  newidx    notes
0         2      0+2=2     if (newidx > len(L)-1): return False

     2:4  1      2+1=3     if newidx > len(L)-1: return False
                          exhaust j
     3    1      3+1=4
1         3      4
     4:4
2         1      2+1=3
     3:4  1      4
Runtime complexity O(n**2)
Space complexity O(1)

edge cases - list 0 length
edge cases - list 1 length
'''

def jumptolastindex(mylist):
    lenmylist = len(mylist) - 1

    if (lenmylist <= 0): return None

    for i in range(0, len(mylist) - 1):
        newidx = i + mylist[i]
        print("i=", i, " newidx=", newidx)
        # if newidx goes over last element, return false
        if newidx > (len(mylist) - 1): return False
        # if current index goes to second last element and it still does not add up to last len-1, return false
        if (i == len(mylist) - 2) and (newidx != len(mylist) - 1): return False

        for j in range(newidx, len(mylist) - 1):
            newidx = j + mylist[j]
            print("     j=", j, " newidx=", newidx)
            if newidx > (len(mylist) - 1): return False
            if (j == len(mylist) - 2) and (newidx != len(mylist) - 1): return False

    return True

#print(jumptolastindex([2,3,1,1,4])) # true
print(jumptolastindex([3,2,1,0,4])) # false
print(jumptolastindex([2,0,1,1,2])) # true


def jumptest(mylist):
    if len(mylist) <= 0: return None

    maximum_reachable_index = 0

    for i, jump in enumerate(mylist):
        if i > maximum_reachable_index: return False

        # maximum reachable index should always be within the last index
        print("index=", i, " j=", jump, " max reachable index = ", maximum_reachable_index)
        maximum_reachable_index = max((i + jump), maximum_reachable_index)

    return True

print("------")
print(jumptest([2,3,1,1,4])) # true
print(jumptest([3,2,1,0,4])) # false
print(jumptest([2,0,1,1,2])) # true