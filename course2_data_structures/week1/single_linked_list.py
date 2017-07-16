"""Singly Linked list"""

class SinglyLinkedList(object):

    def __init__(self):
        self.head = Node()
        self.size = 0
        self.tail = self.head

    def push_front(self, key):
        """Add in the front"""
        new_node = Node(key)
        self.head.next, new_node.next = new_node, self.head.next
        if self.size == 1:
            self.tail = new_node
        self.size += 1

    def top_front(self):
        """Return front item"""
        return self.head.next

    def pop_front(self):
        """Remove front item"""
        if self.empty():
            raise IndexError('List empty')
        node = self.head.next
        self.head.next = self.head.next.next
        if self.size == 1:
            self.tail = self.head
        self.size -= 1
        return node

    def push_back(self, key):
        """Add to back"""
        new_node = Node(key=key)
        # node = self.head
        # while node:
        #     node = node.next
        # node.next = new_node

        self.tail.next= new_node
        self.tail = new_node
        self.size += 1

    def top_back(self):
        """Return back item"""
        # node = self.head
        # while node:
        #     node = node.next
        return self.tail

    def pop_back(self):
        """Remove back item"""
        if self.empty():
            raise IndexError('List empty')
        node = self.head
        prev = self.head
        while node:
            prev = node
            node = node.next
        prev.next = None
        self.tail = prev
        return node


    def find(self, key):
        """Is key in the list"""
        node = self.head
        while node:
            if node.key == key:
                return node
            node = node.next
        return

    def erase(self, key):
        """Remove key from the list"""
        node = self.head
        prev = self.head
        while node:
            prev = node
            if node.key == key:
                break
            node = node.next
        prev.next = prev.next.next
        if self.tail == node:
            self.tail = prev
        self.size -= 1
        return node

    def empty(self):
        """Is list empty"""
        return self.size == 0

    def add_before(self, node, key):
        """Adds key before a given node."""
        node = self.head
        prev = self.head
        while node:
            prev = node
            if node.key == node.key:
                break
            node = node.next

    def add_after(self, node, key):
        """Adds a key after a given node."""
        new_node = Node(key)
        new_node.next, node.next = node.next, new_node
        if self.tail == node:
            self.tail = new_node
        self.size += 1

    def print_list(self):
        node = self.head
        while node:
            print(node.key, '->')
            node = node.next


class Node(object):

    def __init__(self, key=None, next_node=None):
        self.key = key
        self.next = next_node


singly_linked_list = SinglyLinkedList()
singly_linked_list.push_front('a')
singly_linked_list.push_front('b')
singly_linked_list.push_front('c')
singly_linked_list.print_list()