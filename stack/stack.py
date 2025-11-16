import sys
sys.path.append('linked_list')

from linked_list.linked_list import LinkedList

class Stack:
    def __init__(self):
        self.__items = LinkedList()
        self.__items.__iter__()

    def __iter__(self):
        return self

    def __next__(self) -> any:
        return self.__items.__next__()
    
    def __len__(self) -> int:
        return len(self.__items)
    
    def __str__(self) -> str:
        return self.__items.__str__()

    def push(self, item):
        self.__items.push_front(item)

    def pop(self):
        if self.empty():
            raise IndexError("pop from empty stack")
        
        return self.__items.pop_front()

    def peek(self):
        if self.empty():
            raise IndexError("peek from empty stack")
        
        return self.__items.front()

    def empty(self):
        return self.__items.empty()

    def size(self):
        return self.__items.size()
    
    def clear(self):
        self.__items.clear()

    def to_string(self) -> str:
        return self.__items.to_string()