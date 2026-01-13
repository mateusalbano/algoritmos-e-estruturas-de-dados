class Node:

    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class HashMap:

    def __init__(self, initalSize=16):
        self.data = [None] * initalSize
        self.size = 0

    def __getitem__(self, key: any):
         return self.get(key)
    
    def __setitem__(self, key: any, value: any):
        self.put(key, value)

    def _hash(self, key):
        return hash(key) % len(self.data)
    
    def _change_capacity(self):
        temp = self.data
        self.data = [None] * len(self.data) * 2

        for node in temp:
            if node:
                cur = node
                while cur:
                    next = cur.next
                    index = self._hash(cur.key)
                    cur.next = self.data[index]
                    self.data[index] = cur
                    cur = next

    
    def put(self, key, value):
        index = self._hash(key)
        node = self.data[index]

        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        
        newNode = Node(key, value, self.data[index])

        self.data[index] = newNode
        self.size += 1

        if self.size / len(self.data) > 0.75:
            self._change_capacity()


    def get(self, key) -> any:
        index = self._hash(key)
        cur = self.data[index]

        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next

        return None

    def remove(self, key):
        index = self._hash(key)
        cur = self.data[index]
        dummy = Node(next=cur)
        previous = dummy

        while cur:
            if cur.key == key:
                previous.next = cur.next
                self.size -= 1
                break

            previous = cur
            cur = cur.next

        self.data[index] = dummy.next


    def __str__(self):
        to_string = "{"
        i = 0
        for node in self.data:
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