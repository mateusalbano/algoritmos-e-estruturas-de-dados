import sys
sys.path.append('linked_list')

from linked_list.linked_list import LinkedList

class Queue:
    
    def __init__(self):
        self.__items = LinkedList()

    def __iter__(self):
        return self.__items.__iter__()

    def __next__(self):
        return self.__items.__next__()
    
    def __len__(self) -> int:
        return len(self.__items)
    
    def __str__(self) -> str:
        return self.__items.__str__()

    def enqueue(self, item):
        self.__items.push_back(item)

    def dequeue(self):
        if self.empty():
            raise IndexError("Queue.dequeue(): dequeue from empty queue")
        return self.__items.pop_front()

    def front(self):
        if self.empty():
            raise IndexError("Queue.front(): front from empty queue")
        return self.__items.front()

    def back(self):
        if self.empty():
            raise IndexError("Queue.back(): back from empty queue")
        return self.__items.back()
    
    def size(self) -> int:
        return len(self.__items)
    
    def empty(self) -> bool:
        return self.__items.empty()

    def clear(self):
        self.__items.clear()