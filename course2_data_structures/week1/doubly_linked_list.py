"""Doubly linked list"""

class DoublyLinkedList(object):
    pass

class Node(object):

    def __init__(self, key=None, next_node=None, prev_node=None):
        self.key = key
        self.next = next_node
        self.prev = prev_node