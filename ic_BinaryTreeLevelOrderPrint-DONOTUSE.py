
'''

5) Print a binary tree
'''
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def printTraversal(self, start):
        items = []
        if not start:
            print('$')
        else:
            #items.insert(0, start)
            items.append(start)
            traversal = ''
            while len(items) > 0:
                it = items[-1]
                if it:
                    traversal += str(it.value) + '-'
                node = items.pop()

                if node.left:
                    items.insert(0, node.left)
                    #items.append(node.left)
                if node.right:
                    items.insert(0, node.right)
                    #items.append(node.right)
        print(traversal)

    def PrintBinaryTreeByLevel(self, root):
        buf = []
        output = []

        if not root:
            print('*')
        else:
            nextCount = 0
            buf.append(root)
            count = len(buf)
            #print('count = ' + str(count))
            while count > 0:
                node = buf.pop(0)
                if node:
                    output.append(node.value)
                    count -= 1
                else:
                    output.append('*')

                if node and node.left:
                    buf.append(node.left)
                    nextCount += 1
                else:
                    buf.append(None)

                if node and node.right:
                    buf.append(node.right)
                    nextCount += 1
                else:
                    buf.append(None)

                # if count goes down to 0, then print out list
                # reset list
                # set count to nextCount as that many times you will have to go over
                # reset nextCount
                if count == 0:
                    print(output)
                    count = nextCount
                    #print('nextCount = ' + str(nextCount))
                    nextCount = 0
                    output = []




binaryTree = Tree(1)
binaryTree.root.left = Node(2)
binaryTree.root.right = Node(3)
binaryTree.root.left.left = Node(4)
binaryTree.root.left.right = Node(5)
binaryTree.root.right.right = Node(7)
binaryTree.root.right.right.right = Node(8)

'''
      1
     /  \
    2    3
   / \   / \
  4   5 $   7
             \
              8
'''
binaryTree.printTraversal(binaryTree.root)
binaryTree.PrintBinaryTreeByLevel(binaryTree.root)
