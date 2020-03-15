
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def isbalanced(self, root):
        if not root: return True

        buf = []
        delim = None
        eachlevelcount = [1]

        buf.insert(0, root)
        buf.insert(0, delim)

        while True:
            node = buf.pop()
            if node:
                print(str(node.value) + " ", end="")
                if node.left:
                    buf.insert(0, node.left)
                if node.right:
                    buf.insert(0, node.right)
            else:
                print('\n')
                #print("buf length = " + str(len(buf)))
                nextlevelcount = len(buf)
                if len(buf) == 0: break
                eachlevelcount.append(len(buf))
                buf.insert(0, delim)

        print(eachlevelcount)



balancedtree = Tree(1)
balancedtree.root.left = Node(2)
balancedtree.root.right = Node(3)
balancedtree.root.left.left = Node(4)
balancedtree.root.right.left = Node(5)
balancedtree.root.right.right = Node(6)

'''
balanced
               1
              / \
            2    3
           /    / \
          4    5   6

imbalanced
               1
              / \
            2    3
                  \
                   4
                    \
                     5
'''
imbalancedtree = Tree(1)
imbalancedtree.root.left = Node(2)
imbalancedtree.root.right = Node(3)
imbalancedtree.root.right.right = Node(4)
imbalancedtree.root.right.right.right = Node(5)

#print(imbalancedtree.isbalanced(imbalancedtree.root))
print(balancedtree.isbalanced(balancedtree.root))
