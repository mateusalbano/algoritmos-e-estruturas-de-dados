class MinStack:

    def __init__(self):
        self.__stack = []
        self.__min_stack = []

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self) -> any:
        if self.__index < len(self.__items):
            item = self.__stack[self.__index]
            self.__index += 1
            return item
        else:
            raise StopIteration
    
    def __len__(self) -> int:
        return len(self.__stack)
    
    def __str__(self) -> str:
        return str(self.__stack)

    def push(self, item):
        if self.empty() or not item > self.__min_stack[-1]:
            self.__min_stack.append(item)
        self.__stack.append(item)

    def peek(self):
        if self.empty():
            raise IndexError("empty MinStack")
        return self.__stack[-1]
    
    def min(self):
        if self.empty():
            raise IndexError("empty MinStack")
        return self.__min_stack[-1]

    def pop(self):
        if self.empty():
            raise IndexError("empty MinStack")
        
        if not self.__min_stack[-1] < self.__stack[-1]:
            self.__min_stack.pop()

        return self.__stack.pop()
    
    def empty(self):
        return len(self.__stack) == 0
    
    def clear(self):
        self.__stack = []
        self.__min_stack = []