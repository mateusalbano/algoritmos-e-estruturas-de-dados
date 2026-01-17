class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class HashSet:

    def __init__(self, initalSize=16):
        self.__data = [None] * initalSize
        self.__size = 0

    def __iter__(self):
        self.__index = 0
        return self
    
    def __next__(self):
        for i in range(self.__index, len(self.__data)):
            node = self.__data[i]
            if node:
                self.__index = i
                return node.value
            
        raise StopIteration
    
    def __len__(self) -> int:
        return self.__size

    def __str__(self) -> str:
        to_string = "{"
        i = 0
        for node in self.__data:
            if node:
                cur = node
                while cur:
                    if i > 0:
                        to_string += ", "
                    to_string += str(cur.value)
                    i += 1
                    cur = cur.next
                    
        to_string += "}"

        return to_string

    def __hash(self, value):
        return hash(value) % len(self.__data)
    
    def __change_capacity(self):
        temp = self.__data
        self.__data = [None] * len(self.__data) * 2

        for node in temp:
            if node:
                cur = node
                while cur:
                    next = cur.next
                    index = self.__hash(cur.value)
                    cur.next = self.__data[index]
                    self.__data[index] = cur
                    cur = next

    
    def put(self, value):
        index = self.__hash(value)
        node = self.__data[index]

        while node:
            if node.value == value:
                return
            node = node.next
        
        newNode = Node(value, self.__data[index])

        self.__data[index] = newNode
        self.__size += 1

        if self.__size / len(self.__data) > 0.75:
            self.__change_capacity()

    def remove(self, value):
        index = self.__hash(value)
        cur = self.__data[index]
        dummy = Node(next=cur)
        previous = dummy
        found = False

        while cur:
            if cur.value == value:
                previous.next = cur.next
                self.__size -= 1
                found = True
                break

            previous = cur
            cur = cur.next

        self.__data[index] = dummy.next
        
        if not found:
            raise KeyError(f"HashSet.remove(value): Value '{value}' not in set")

    def size(self) -> int:
        return self.__size

    def empty(self) -> bool:
        return self.__size == 0
    
    def contains(self, value):
        index = self.__hash(value)
        cur = self.__data[index]

        while cur:
            if cur.value == value:
                return True
            cur = cur.next

        return False
    
    def clear(self, initalSize=16):
        self.__data = [None] * initalSize
        self.__size = 0