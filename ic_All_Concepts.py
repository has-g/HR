
'''
1) Binary Search in sorted list
2) Bubble Sort
3) Palindrome
4) Binary depth first traversal
5) Print a binary tree
'''

def BinarySearchInSortedList_naive(list, x):
    listlen = len(list)
    for i in range(listlen):
        if list[i] == x:
            return i
    return -1
#print(BinarySearchInSortedList_naive([-1, 0, 2, 4, 6, 7, 9, 12], 2))

def BinarySearchInSortedList(list, x):
    if len(list) == 0: return -1
    if len(list) == 1:
        if list[0] == x: return 0
        else: return -1
    l = 0
    r = len(list) - 1
    m = l + (r-l)//2

    # check that l less than and equal to right, else you will miss the last idx
    while l <= r:
        m = l + (r - l)// 2
        if list[m] == x: return m
        elif list[m] > x: r = m - 1
        elif list[m] < x: l = m + 1
        else: print('invalid')
    return -1
#print(BinarySearchInSortedList([-1, 0, 2, 4, 6, 7, 9, 12], 4))

''' ========== 2. Bubble sort ==========='''
def BubbleSort_naive(mylist):
    list = sorted(mylist) # makes a copy
    #print(mylist.sort(reverse=True)) # sorts the same list
    return mylist
#print(BubbleSort_naive([5, -1, 11, 3, 2, 99, 2, 1, -1]))

def BubbleSort(mylist):
    listlen = len(mylist)
    if listlen <= 1: return mylist
    for i in range(listlen):
        for j in range(listlen - 1):
            if mylist[j] > mylist[j + 1]:
                temp = mylist[j]
                mylist[j] = mylist[j + 1]
                mylist[j + 1] = temp
        #print(mylist)
    return(mylist)
#print(BubbleSort([5, -1, 11, 3, 2, 99, 2, 1, -1]))

''' ========== 3) Palindrome ========== '''
def Palindrom_stringmanipulator(str):
    stringlen = len(str)
    if stringlen == 0: return -1
    if stringlen == 1: return True

    m = stringlen // 2
    if stringlen%2:
        # odd
        # note: string index also goes to m-1
        leftstr = str[0:m]
        rightstr = str[m + 1: stringlen]
    else:
        # even
        leftstr = str[0:m]
        rightstr = str[m:stringlen]
    rightstr_reversed = rightstr[::-1]
    print(leftstr + ' - ' + rightstr_reversed)
    if leftstr == rightstr_reversed: return True
    return False
#print(Palindrom_stringmanipulator("deliledx"))


def Palindrom(str):
    stringlen = len(str)
    if stringlen == 0: return -1
    if stringlen == 1: return True

    mid = stringlen//2

    for i in range(mid):
        if str[i] != str[stringlen - 1 - i]: return False
    return True
#print(Palindrom("delxled"))

''' ========== 4) PrintBinaryTree ========== '''
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, value):
        self.root = Node(value)

    def print_tree(self, printtype):
        if printtype == 'preorder':
            return self.preorder_traversal(self.root, "")
        elif printtype == 'inorder':
            return self.inorder_traversal(self.root, "")
        elif printtype == 'levelorder':
            return self.levelorder_print(self.root)
        else:
            print("wrong printtype = " + printtype)

    def preorder_traversal(self, start, traversal):
        # root -> left -> right
        if start:
            #traversal += 'again'
            traversal += str(start.value) + "-"
            traversal = self.preorder_traversal(start.left, traversal)
            traversal = self.preorder_traversal(start.right, traversal)
        return traversal

    def inorder_traversal(self, start, traversal):
        # left -> root -> right
        if start:
            traversal = self.inorder_traversal(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.inorder_traversal(start.right, traversal)
        return traversal

    def levelorder_print(self, start):
        # level by level traversal
        if not start: return
        else:
            items = []
            items.insert(0, start)
            traversal = ""

            while len(items) > 0:
                # print value of first item
                traversal += str(items[-1].value) + "-"
                print(traversal)
                # pop the value into a node
                node = items.pop()
                # check left and right of node
                if node.left:
                    items.insert(0, node.left)
                if node.right:
                    items.insert(0, node.right)
            return traversal



'''
      1
     /  \
    2    3
   / \   / \
  4   5 $   7
             \
              8
'''
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right = Node(3)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

print(tree.print_tree('preorder'))
print(tree.print_tree('inorder'))
#print(tree.print_tree('postorder'))
print(tree.print_tree('levelorder'))

