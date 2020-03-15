'''
https://www.youtube.com/watch?v=o-_Gk0rBeIo

'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinTree(object):
    def __init__(self, value):
        self.root = Node(value)

    def printlevelbylevel(self, root):
        if not root:
            print('*')
            return -1
        else:
            buf = []
            delim = None

            buf.insert(0, root)
            buf.insert(0, delim)

            while True:
                currentnode = buf.pop()
                if currentnode:
                    print(str(currentnode.value) + ' ', end="")
                    if currentnode.left:
                        buf.insert(0, currentnode.left)
                    else:
                        #print('n-l', end="")
                        pass
                    if currentnode.right:
                        buf.insert(0, currentnode.right)
                    else:
                        #print('n-r', end="")
                        pass
                else:
                    print('\n')
                    if len(buf) == 0: break
                    buf.insert(0, delim)


    def pLbyL(self, root):
        if not root: return

        buf = []
        delim = None

        buf.insert(0, root)
        buf.insert(0, delim)

        while True:
            node = buf.pop()
            if node:
                print(str(node.value) + ' ', end="")
                if node.left:
                    buf.insert(0, node.left)
                else:
                    print('*/ ', end="")
                if node.right:
                    buf.insert(0, node.right)
                else:
                    print('\\* ', end="")
            else:
                print('\n')
                if len(buf) == 0: break
                buf.insert(0, delim)

mytree = BinTree(1)
mytree.root.left = Node(2)
mytree.root.right = Node(5)
mytree.root.left.left = Node(3)
mytree.root.left.right = Node(4)
mytree.root.right.left = Node(6)
mytree.root.right.right = Node(7)
mytree.root.right.right.right = Node(9)

#mytree.printlevelbylevel(mytree.root)
#mytree.printlevelbylevel(None)

mytree.pLbyL(mytree.root)
