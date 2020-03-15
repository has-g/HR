'''
https://www.youtube.com/watch?v=6oL-0TdVy28

preorder = 1-2-4-5-3-6-7
inorder = 4-2-5-1-6-3-7
postorder = 4-2-5-6-3-7-1
      1
     /  \
    2    3
   / \   / \
  4   5 6   7
'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def print(self, root, type):
        if type == 'preorder':
            print(self.print_preorder(self.root))
        elif type == 'inorder':
            print(self.print_inorder(self.root))
        elif type == 'postorder':
            print(self.print_postorder(self.root))
        else:
            print('unknown type')

    def print_preorder(self, root, traversal = ""):
        # preorder = root, left, right
        # inorder = left, root, right
        # postorder = left, right, root
        if root:
            traversal += (str(root.value) + "-")
            traversal = self.print_preorder(root.left, traversal)
            traversal = self.print_preorder(root.right, traversal)
        return traversal

    def print_inorder(self, root, traversal = ""):
        # preorder = root, left, right
        # inorder = left, root, right
        # postorder = left, right, root
        if root:
            traversal = self.print_inorder(root.left, traversal)
            traversal += (str(root.value) + "-")
            traversal = self.print_inorder(root.right, traversal)
        return traversal

    def print_postorder(self, root, traversal = ""):
        # preorder = root, left, right
        # inorder = left, root, right
        # postorder = left, right, root
        if root:
            traversal = self.print_postorder(root.left, traversal)
            traversal = self.print_postorder(root.right, traversal)
            traversal += (str(root.value) + "-")
        return traversal

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

tree.print(tree.root, 'preorder')
tree.print(tree.root, 'inorder')
tree.print(tree.root, 'postorder')


