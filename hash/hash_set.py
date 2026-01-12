class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class HashSet:

    def __init__(self, initalSize=16):
        self.data = [None] * initalSize
        self.size = 0

    def _hash(self, value):
        return hash(value) % len(self.data)
    
    def _change_capacity(self):
        temp = self.data
        self.data = [None] * len(self.data) * 2

        for node in temp:
            if node:
                cur = node
                while cur:
                    next = cur.next
                    index = self._hash(cur.value)
                    cur.next = self.data[index]
                    self.data[index] = cur
                    cur = next

    
    def put(self, value):
        index = self._hash(value)
        node = self.data[index]

        while node:
            if node.value == value:
                return
            node = node.next
        
        newNode = Node(value, self.data[index])

        self.data[index] = newNode
        self.size += 1

        if self.size / len(self.data) > 0.75:
            self._change_capacity()


    def contains(self, value) -> any:
        index = self._hash(value)
        cur = self.data[index]

        while cur:
            if cur.value == value:
                return True
            cur = cur.next

        return False

    def remove(self, value):
        index = self._hash(value)
        cur = self.data[index]
        dummy = Node(next=cur)
        previous = dummy

        while cur:
            if cur.value == value:
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
                    to_string += str(cur.value)
                    i += 1
                    cur = cur.next
                    
        to_string += "}"

        return to_string