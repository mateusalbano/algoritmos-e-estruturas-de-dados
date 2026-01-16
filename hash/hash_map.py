class Node:

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class HashMap:

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
                return node.key

        raise StopIteration

    def __getitem__(self, key):
         return self.get(key)
    
    def __setitem__(self, key, value):
        self.put(key, value)

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
                    to_string += str(cur.key) + ": " + str(cur.value)
                    i += 1
                    cur = cur.next
                    
        to_string += "}"

        return to_string

    def __hash(self, key):
        return hash(key) % len(self.__data)
    
    def __change_capacity(self):
        temp = self.__data
        self.__data = [None] * len(self.__data) * 2

        for node in temp:
            if node:
                cur = node
                while cur:
                    next = cur.next
                    index = self._hash(cur.key)
                    cur.next = self.__data[index]
                    self.__data[index] = cur
                    cur = next

    
    def put(self, key, value):
        index = self.__hash(key)
        node = self.__data[index]

        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        
        newNode = Node(key, value, self.__data[index])

        self.__data[index] = newNode
        self.__size += 1

        if self.__size / len(self.__data) > 0.75:
            self.__change_capacity()


    def get(self, key, *args):
        index = self.__hash(key)
        cur = self.__data[index]

        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next

        if len(args) == 0:
            return None
        else:
            return args[0]

    def pop(self, key, *args):
        popped_value = None
        found = False

        index = self.__hash(key)
        cur = self.__data[index]
        dummy = Node(next=cur)
        previous = dummy

        while cur:
            if cur.key == key:
                previous.next = cur.next
                popped_value = cur.value
                self.__size -= 1
                found = True
                break

            previous = cur
            cur = cur.next

        self.__data[index] = dummy.next
        
        if not found:
            if len(args) == 0:
                raise KeyError(f"HashMap.pop(key, *args): Key '{key}' not found")
            else:
                return args[0]
        
        return popped_value

    def keys(self) -> list:
        keys = []
        for node in self.__data:
            if node:
                cur = node
                while cur:
                    keys.append(cur.key)
                    cur = cur.next

        return keys
    
    def values(self) -> list:
        values = []
        for node in self.__data:
            if node:
                cur = node
                while cur:
                    values.append(cur.value)
                    cur = cur.next

        return values
    
    def items(self) -> list:
        items = []
        for node in self.__data:
            if node:
                cur = node
                while cur:
                    items.append((cur.key, cur.value))
                    cur = cur.next

        return items
    
    def size(self) -> int:
        return self.__size
    
    def empty(self) -> bool:
        return self.__size == 0
    
    def contains(self, key) -> bool:
        index = self.__hash(key)
        cur = self.__data[index]

        while cur:
            if cur.key == key:
                return True
            cur = cur.next

        return False

    def clear(self, initalSize=16):
        self.__data = [None] * initalSize
        self.__size = 0