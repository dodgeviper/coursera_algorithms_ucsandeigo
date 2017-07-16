"""Queue: Abstract data type"""


class Queue(object):

    def enqueue(self, key):
        """Adds keys to collections."""
        pass

    def dequeue(self):
        """Removes and returns the least recently added key."""
        pass


class QueueAsArray(object):
    """O(1) time complexity for operations but wasted space. again for the same reason as space."""

    def __init__(self):
        self.queue = []
        self.top = 0
        self.last = 0

    def enqueue(self, key):
        self.last += 1
        self.queue[self.last] = key

    def dequeue(self):
        if self.empty():
            raise IndexError('Empty queue')
        key = self.queue[self.top]
        self.top += 1

    def empty(self):
        return self.top == self.last

class QueueAsLinkedList(object):
    """All operations are O(1)."""
    pass
