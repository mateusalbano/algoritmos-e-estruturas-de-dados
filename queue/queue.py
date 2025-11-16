import sys
sys.path.append('linked_list')

from linked_list.linked_list import LinkedList

class Queue:
    
    def __init__(self):
        self.__items = LinkedList()

    def __iter__(self):
        return self.__items.__iter__()

    def __next__(self) -> any:
        return self.__items.__next__()
    
    def __len__(self) -> int:
        return len(self.__items)
    
    def __str__(self) -> str:
        return self.__items.__str__()

    def empty(self) -> bool:
        return self.__items.empty()

    def enqueue(self, item):
        self.__items.push_back(item)

    def dequeue(self):
        return self.__items.pop_front()

    def front(self):
        return self.__items.front()

    def back(self):
        return self.__items.back()

    def clear(self):
        self.__items.clear()