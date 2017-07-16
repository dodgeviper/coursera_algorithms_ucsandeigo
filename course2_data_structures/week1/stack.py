"""Stacks: LIFO

Stacks can be used to solve problems like balanced string.
"""

class Stack(object):

    def push(self, key):
        """Adds key to the collection at the top."""
        pass

    def top(self):
        """Returns the most recently added key."""
        return

    def pop(self):
        """Removes and returns the most recently added key."""
        return

    def empty(self):
        """Is the list empty"""
        return False


class StackAsArray(object):
    """Following operations are O(1) but memory used is O(# Insertions)"""
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, key):
        self.stack[self.top + 1] = key
        self.top += 1

    def top(self):
        return self.stack[self.top]

    def pop(self):
        key = self.stack[self.top]
        self.top -= 1
        return key

    def empty(self):
        return len(self.stack) == 0


class StackAsLinkedList(object):
    """All operations are O(1). Even with singly linked list will do."""
    pass
