class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def printTree(root):

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
            # record node first
            if node:
                output.append(node.value)
                count -= 1
            else:
                # node with no children
                output.append('$')

            # if node does have a left or right child
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
            if count == 0:
                print(output)
                output = []
                count = nextCount
                nextCount = 0
        # print the remaining all empty leaf node part
        for i in range(len(buf)):
            output.append('$')
        print(output)

def printTreeView(root):
    buf = []
    output = []
    if not root:
        print('$')
    else:
        buf.append(root)
        count = 1
        nextcount = 0
        while count > 0:
            node = buf.pop(0)
            if node:
                # append value of node to print list
                output.append(node.value)
                # decrement count
                count -= 1
                # if next level exist increment next count by the same amount
                if node.left:
                    buf.append(node.left)
                    nextcount += 1
                else: output.append('$l')

                if node.right:
                    buf.append(node.right)
                    nextcount += 1
                else: output.append('$r')
            else:
                output.append('$n')

            if count == 0:
                print(buf)
                buf = []
                count = nextcount
                nextcount = 0


'''
def PrintTreeByLevel(root):
    buf = []
    output = []
    current = 0
    if not root: print('$')
    else:
        buf.append(root)
        node = buf.pop(0)
        print(node.value)
        output.append(node.value)
        output.append('null')

        for i in range(4):
            current = output.pop(0)
            if node.left:
                output.append(node.left.value)
                buf.append(node.left)
            if node.right:
                output.append(node.right.value)
                buf.append(node.right)

            current = output.pop(0)
            print(output)

            if current == 'null':
                print('\n')
                output.append('null')
                print(output)

'''


'''
    1 
   / \
  2   3
 /   / \
4   5   6
         \
          7
'''

mytree = Node(1)
mytree.left = Node(2)
mytree.right = Node(3)
mytree.left.left = Node(4)
mytree.right = Node(3)
mytree.right.left = Node(5)
mytree.right.right = Node(6)
mytree.right.right.right = Node(7)

printTree(mytree)
#PrintTreeByLevel(mytree)
#printTreeView(mytree)