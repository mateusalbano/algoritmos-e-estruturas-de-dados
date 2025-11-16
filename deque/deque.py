import sys
sys.path.append('linked_list')

from linked_list.doubly_linked_list import DoublyLinkedList

class Deque:

    def __init__(self):
        self.__items = DoublyLinkedList()

    def __iter__(self):
        return self.__items.__iter__()
    
    def __next__(self) -> any:
        return self.__items.__next__()

    def __len__(self) -> int:
        return len(self.__items)
    
    def __str__(self) -> str:
        return str(self.__items)
    
    def push_front(self, item):
        self.__items.push_front(item)

    def push_back(self, item):
        self.__items.push_back(item)

    def pop_front(self):
        if self.empty():
            raise IndexError("pop from empty deque")
        
        return self.__items.pop_front()
    
    def pop_back(self):
        if self.empty():
            raise IndexError("pop from empty deque")
        
        return self.__items.pop_back()
    
    def front(self) -> any:
        if self.empty():
            raise IndexError("front from empty deque")
        
        return self.__items.front()
    
    def back(self) -> any:
        if self.empty():
            raise IndexError("back from empty deque")
        
        return self.__items.back()
    
    def empty(self) -> bool:
        return len(self.__items) == 0
    
    def clear(self):
        self.__items.clear()

    