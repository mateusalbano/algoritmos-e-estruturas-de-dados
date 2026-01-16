class Stack:
    def __init__(self):
        self.__items = []

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self) -> any:
        if self.__index < len(self.__items):
            item = self.__items[self.__index]
            self.__index += 1
            return item
        else:
            raise StopIteration
    
    def __len__(self) -> int:
        return len(self.__items)
    
    def __str__(self) -> str:
        return str(self.__items)

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.empty():
            raise IndexError("Stack.pop(): pop from empty stack")
        
        return self.__items.pop()

    def peek(self):
        if self.empty():
            raise IndexError("Stack.peek(): peek from empty stack")
        
        return self.__items[-1]
    
    def size(self) -> int:
        return len(self.__items)

    def empty(self):
        return len(self.__items) == 0

    def clear(self):
        self.__items = []
