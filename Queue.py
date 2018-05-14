import queue

class Queue:

    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def remove(self, item):
        return self._items.pop(self._items.index(item))

    def __contains__(self, object):
        return object in self._items

    def toList(self):
        return self._items
