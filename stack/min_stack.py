from stack import Stack

class MinStack:

    def __init__(self):
        self.__stack = Stack()
        self.__min_stack = Stack()

    def __iter__(self):
        return self.__stack.__iter__()

    def __next__(self) -> any:
        return self.__stack.__next__()
    
    def __len__(self) -> int:
        return len(self.__stack)
    
    def __str__(self) -> str:
        return self.__stack.__str__()

    def push(self, item):
        if self.empty() or not item > self.__min_stack.peek():
            self.__min_stack.push(item)
        self.__stack.push(item)

    def size(self) -> int:
        return self.__stack.size()
    
    def empty(self) -> bool:
        return self.__stack.empty()

    def peek(self):
        if self.empty():
            raise IndexError("empty MinStack")
        return self.__stack.peek()
    
    def min(self):
        if self.__min_stack.empty():
            raise IndexError("empty MinStack")
        return self.__min_stack.peek()

    def pop(self):
        if self.empty():
            raise IndexError("empty MinStack")
        
        if not self.__min_stack.peek() < self.__stack.peek():
            self.__min_stack.pop()

        return self.__stack.pop()


