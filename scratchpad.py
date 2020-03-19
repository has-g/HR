class Trie(object):
    def __init__(self):
        self.head = {}

    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        # * denotes the Trie has this word as item
        # if * doesn't exist, Trie doesn't have this word but as a path to longer word
        cur['*'] = True
        print(self.head)

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]

        if '*' in cur:
            return True
        else:
            return False


dictionary = Trie()

dictionary.add("hi")
dictionary.add("hello")
dictionary.add("sell")
dictionary.add("seller")
print(dictionary.search("hi"))
print(dictionary.search("hello"))
print(dictionary.search("hel"))
print(dictionary.search("hey"))
print(dictionary.search("seller"))


def SearchForElinSortedList(lst, el):
    if len(lst) == 0: return -1

    if len(lst) == 1:
        if el == lst[0]:
            return 0
        else:
            return -1

    listlen = len(lst)

    l = 0
    r = listlen - 1

    while l < r:
        mid = l + (r - l)//2

        if el < lst[mid]:
            r = mid - 1
        elif el > lst[mid]:
            l = mid + 1
        elif el == lst[mid]:
            return mid
        else:
            return -1

    return -1
print('----------')
print(SearchForElinSortedList([0, 2, 4, 5, 7, 8, 9], -7))
print(SearchForElinSortedList([-7], -7))

def mergeSortedLists(left, right):
    lenleft = len(left)
    lenright = len(right)

    lidx = 0
    ridx = 0

    mylist = []

    # empty lists
    if lenleft == 0: return right
    if lenright == 0: return left

    # single length lists

    for _ in range(lenleft + lenright):
        if lidx < lenleft and ridx < lenright:
            # if value in left list is smaller
            if left[lidx] <= right[ridx]:
                mylist.append(left[lidx])
                lidx += 1
            else:
                mylist.append(right[ridx])
                ridx += 1
        elif lidx == lenleft:
            # copy remaining items from right list
            mylist.append(right[ridx])
            ridx += 1
        elif ridx == lenright:
            # copy remaining items from right list
            mylist.append(left[lidx])
            lidx += 1

    return mylist


print(mergeSortedLists([0, 3, 7, 8, 9], [1, 4]))

def mergesort(lst):
    if len(lst) <= 1: return lst

    mid = len(lst)//2

    left = mergesort(lst[:mid])
    right = mergesort(lst[mid:])

    return mergeSortedLists(left, right)

print(mergesort([7, 1, -3, 100, 34, -8, 4, 2]))


def listmodifier(int_list):
    for i, j in enumerate(int_list):
        int_list[i] *= 2

# notice the original list although passed as an argument got changed by the procedure
int_list_original = [0, 2, 3, 4]
listmodifier(int_list_original)
print(int_list_original)


def reverse(list_of_chars):

    left_index  = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]
        # Move towards middle
        left_index  += 1
        right_index -= 1


listofchars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
reverse(listofchars)
print(listofchars)


def SortSoredLists(l1, l2):
    if len(l1) == 0: return l2
    if len(l2) == 0: return l1

    totallen = len(l1) + len(l2)

    l = 0
    r = 0
    mylist = []

    for i in range(totallen):
        print(">> l = ", l, ", r = ", r)

        if l >= len(l1):
            mylist.append(l2[r])
            r += 1
        elif r >= len(l2):
            mylist.append(l1[l])
            l += 1
        elif l1[l] <= l2[r]:
            mylist.append(l1[l])
            l += 1
        elif l1[l] > l2[r]:
            mylist.append(l2[r])
            r += 1
        else:
            print("shouldn't be here: l = ", l, ", r = ", r)

    return mylist

print(SortSoredLists([2, 5], [1, 3, 4, 7, 10]))
# Complexity
# O(n)O(n) time and O(n)O(n) additional space, where nn is the number of items in the merged list.

def findSum(target, L, sofar=None):
    if sofar is None:
        sofar = []
    if not target:
        print(sofar)
        return
    if target < 0:
        return
    for i,num in enumerate(L):
        print("i = ", i, ", num = ", num, ", L = ", L)
        return findSum(target-num, L[:i]+L[i+1:], sofar+[num])

print(findSum(10, [1,3,11,123,5,7]))


def sort_scores(unsorted_scores, highest_possible_score):
    # create a list of actual index 1 to 100, each element is 0
    score = [0] * (highest_possible_score + 1)

    # nothing to do
    if len(unsorted_scores) <= 1: return unsorted_scores

    # create a count at the index of the score found
    for i, j in enumerate(unsorted_scores):
        print(i, ' ', j)
        if score[j] == 0:
            score[j] = 1
        else:
            score[j] += 1

    #print(score)

    # with highest value first
    returnscore = []
    for x in range(len(score) - 1, -1, -1):
        if score[x] != 0:
            for y in range(score[x]):
                returnscore.append(x)

    return returnscore



print(sort_scores([20, 10, 30, 30, 10, 20], 100))




print("======")
# 0, 1, 1, 2, 3, 5, 8, 13, ....
# f(n) = f(n-2) + f(n-1)
#

def fib(n):
    global fib_counter
    fib_counter += 1
    # edge case -ve
    if n < 0: raise IndexError('number cannot be negative')
    # edge cases 0
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)

fib_counter = 0
print(fib(7))
print("fib_counter = ", fib_counter)

# total runtime is a binary tree due to recursion O(2**n)
# it is a binary tree of depth 5 for f(5)
# with memoization we can get to O(n) runtime and O(n) space

# two ways to do it - we can have a global variable declared and that accessed inside our function
# or define it as a class and use a class variable

def fib_m(n):
    global fib_counter
    fib_counter += 1
    # edge case -ve
    if n < 0: raise IndexError('number cannot be negative')
    # edge cases 0
    if n <= 1:
        return n

    global dDict
    a = 0

    if n in gDict:
        return gDict[n]
    else:
        a = fib_m(n-1) + fib_m(n-2)
        gDict[n] = a

    return a

gDict = {}
fib_counter = 0
print(fib_m(7))
print("fib_counter = ", fib_counter)


class fib_class:
    def __init__(self):
        self.dict = {}
        self.counter = 0

    def fib_class_fib(self, n):
        self.counter += 1
        #print("self.counter = ", self.counter)
        if n < 0: raise IndexError('number cannot be negative')
        if n <= 1:
            return n

        if n in self.dict:
            return self.dict[n]
        else:
            self.dict[n] = self.fib_class_fib(n-1) + self.fib_class_fib(n-2)

        return self.dict[n]

a = fib_class()
print(a.fib_class_fib(2))


def canjump(nums):
    maximum_reachable_index = 0

    for index, max_jump in enumerate(nums):
        #print(f"{index}", end=' ')
        if index > maximum_reachable_index:
            print(f"> {maximum_reachable_index} and is unreachable.")
            return False

        #print(f"+ {max_jump} => {index + max_jump} : {maximum_reachable_index} ")
        print(index, " + ", max_jump, " => ", index + max_jump, " : ", maximum_reachable_index)
        if index + max_jump > maximum_reachable_index:
            maximum_reachable_index = index + max_jump
        #maximum_reachable_index = max(index + max_jump, maximum_reachable_index)

    return True


nums = [3,2,1,0,4]
#nums = [2,3,1,1,5]
print(canjump(nums))