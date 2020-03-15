class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def printTreeView(root):
    buf = []
    output = []
    if not root:
        print('$')
    else:
        buf.append(root)
        count = 1
        nextCount = 0
        while count > 0:
            node = buf.pop(0)
            if node:
                output.append(node.value)
                count -= 1
                if node.left:
                    buf.append(node.left)
                    nextCount += 1
                else: buf.append(None)

                if node.right:
                    buf.append(node.right)
                    nextCount += 1
                else: buf.append(None)
            else:
                output.append('$n')

            if count == 0:
                print(output)
                output = []
                count = nextCount
                nextCount = 0


'''
    1 
   / \
  2   3
 /   / \
4   5   6
'''

mytree = Node(1)
mytree.left = Node(2)
mytree.right = Node(3)
mytree.left.left = Node(4)
mytree.right = Node(3)
mytree.right.left = Node(5)
mytree.right.right = Node(6)

printTreeView(mytree)

'''
    6
   / \
   1  0
       \
        7
         \
          8
'''
mytree = Node(6)
mytree.left = Node(1)
mytree.right = Node(0)
mytree.right.right = Node(7)
mytree.right.right.right = Node(8)
printTreeView(mytree)
