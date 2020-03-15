'''

https://www.youtube.com/watch?v=6oL-0TdVy28
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def printTree(self, orderType):
        if orderType == 'preOrder':
            return self.preOrderPrint(self.root, "")
        elif orderType == 'inOrder':
            return self.inOrderPrint(self.root, "")
        elif orderType == 'postOrder':
            return self.postOrderPrint(self.root, "")
        else:
            print("type " + str(orderType) + str(" does not exist"))

    def preOrderPrint(self, start, traversal):
        '''Root -> left node -> right node'''
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preOrderPrint(start.left, traversal)
            traversal = self.preOrderPrint(start.right, traversal)
        return traversal

    def inOrderPrint(self, start, traversal):
        '''left node -> Root -> right node'''
        if start:
            traversal = self.inOrderPrint(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.inOrderPrint(start.right, traversal)
        return traversal

    def postOrderPrint(self, start, traversal):
        ''' left node -> right node -> root'''
        if start:
            traversal = self.postOrderPrint(start.left, traversal)
            traversal = self.postOrderPrint(start.right, traversal)
            traversal += str(start.value) + str('-')
        return traversal
'''
preorder = 1-2-4-5-3-6-7
inorder = 4-2-5-1-6-3-7
postorder = 4-2-5-6-3-7-1
      1
     /  \
    2    3
   / \   / \
  4   5 6   7   
'''

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.printTree("preOrder"))
print(tree.printTree("inOrder"))
print(tree.printTree("postOrder"))