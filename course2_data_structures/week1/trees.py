"""Trees.
Examples: Syntax structures, Heirarchies, Abstract Syntax Tree for code.

Definition:
: is empty or
a node with key or child tree.

Leaf - a node which has no children.

Forest - collection of trees.
"""

class BinarySearchTree(object):

    def __init__(self, data):
        self.root = Node(data=data)

    def height(self):
        def compute(node):
            if node is None:
                return 0
            return 1 + max(compute(node.left), compute(node.right))

        return compute(self.root)

    def size(self):

        def compute(node):
            if node is None:
                return 0
            return 1 + compute(node.left) + compute(node.right)

        return compute(self.root)


    def in_order_traversal(self):
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            print(node.key)
            traverse(node.right)

    def pre_order_traversal(self):

        def traverse(node):
            if node is None:
                return
            print(node.data)
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)


    def post_order_traversal(self):
        def traverse(node):
            if node is None:
                return
            traverse(node.left)
            traverse(node.right)
            print(node.data)

        traverse(self.root)


    def level_traversal(self):
        """Is also called Breadth first search traversal"""
        queue = []
        queue.push(self.root)
        while queue:
            node = queue.pop(0)
            if node:
                print(node.data)
                queue.push(node.left)
                queue.push(node.right)





class Node(object):

    def __init__(self, left=None, right=None, data=None, parent=None):
        self.left = left
        self.right = right
        self.data = data
        self.parent = parent
