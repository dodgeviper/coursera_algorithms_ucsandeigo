# Uses python3.
"""Compute Tree height.
Task:
You are given a description of a rooted tree. Your task is to compute and output its
height. You are given an arbitrary tree and not necessarily a binary tree.

Input format:
the first line contains the number of numbers n. The second line contains n integer
numbers from -1 to n-1 parents of nodes. If the i-th one of the them (0<= i <= n-1) is -1
node i is the root otherise its 0-based index of the parent of the i-th node. It is
guaranteed that there is exactly one root. It is guaranteed that input represents
a tree.

Constraints: 1<= n <= 10^5.

Output format: Output the height of the tree.
"""

import sys
sys.setrecursionlimit(10**7)

class Node(object):

    def __init__(self, data, children=None):
        self.data = data
        self.children = children or []
        self.parent = None

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent

    def __str__(self):
        return self.data + "->" + nodes.children

def compute_height_recur(tree, root):

    def compute(node):
        if not node.children:
            return 1
        return 1 + max(list(map(compute, node.children)))

    return compute(tree[root])


def compute_height(tree, root):
    queue = [tree[root]]
    height = 1
    parents_visited = set()
    while queue:
        node = queue.pop(0)
        if node.parent not in parents_visited:
            # Count only when the parent has been visited once.
            parents_visited.add(node.parent)

            if node.parent is not None:
                # Add all siblings at this level
                for child in node.parent.children:
                    parents_visited.add(child)
            height += 1
        queue.extend(node.children)
    return height


num_nodes = int(input())
nodes = [Node(x) for x in range(num_nodes)]
root_index = -1
parents = list(map(int, input().split()))
for child_index in range(num_nodes):
    parent_index = parents.pop(0)
    if parent_index == -1:
        root_index = child_index
    else:
        nodes[child_index].parent = nodes[parent_index]
        nodes[parent_index].add_child(nodes[child_index])


# print(nodes)
print(compute_height_recur(nodes, root_index))
# print(compute_height(nodes, root_index))
