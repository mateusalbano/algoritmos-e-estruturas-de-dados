class node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self) -> int:
        return self.size

    def push_back(self, item):
        if self.size == 0:
            self.head = node(item)
            self.tail = self.head
        else:
            new_node = node(item)
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def push_front(self, item):
        if self.size == 0:
            self.head = node(item)
            self.tail = self.head
        else:
            new_node = node(item)
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError("pop from empty list")
        
        last_item = self.tail.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None
        
        self.size -= 1
        return last_item
    
    def pop_front(self):
        if self.size == 0:
            raise IndexError("pop from empty list")
        
        last_item = self.head.value
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None
        
        self.size -= 1
        return last_item
    
    def __get_node(self, item) -> node:
        node = self.head
        while node:
            if node.value == item:
                break
            node = node.next
        return node
    
    def __get_node_at(self, pos: int) -> node:
        if pos < 0 or pos > self.size - 1:
            raise IndexError("list index out of range")
        node = self.head
        i = 0
        while node:
            if i == pos:
                break
            node = node.next
            i += 1
        return node
    
    def insert_at(self, pos: int, item):
        if pos == 0:
            self.push_front(item)
            return
        if pos == self.size:
            self.push_back(item)
            return

        this_node = self.__get_node_at(pos)
        new_node = node(item)
        this_node.previous.next = new_node
        new_node.previous = this_node.previous
        new_node.next = this_node
        this_node.previous = new_node
        self.size += 1

    def replace_at(self, pos: int, item):
        self.__get_node_at(pos).value = item

    def replace(self, item, new_item):
        node = self.__get_node(item)
        if node:
            node.value = new_item
        else:
            raise ValueError("linked_list.replace(item, new_item): item not in list")
        
    def remove_at(self, pos: int):
        if pos == 0:
            self.pop_front()
            return
        if pos == self.size - 1:
            self.pop_back()
            return

        node = self.__get_node_at(pos)
        node.previous.next = node.next
        node.next.previous = node.previous
        self.size -= 1
        return node.value

    def remove(self, item):
        node = self.__get_node(item)
        if not node:
            raise ValueError("linked_list.remove(item): item not in list")
        if node is self.head:
            return self.pop_front()
        if node is self.tail:
            return self.pop_back()
        
        node.previous.next = node.next
        node.next.previous = node.previous
        self.size -= 1
        return node.value

    def get_at(self, pos: int):
        return self.__get_node_at(pos).value

    def back(self):
        if self.head:
            return self.head.value
        else:
            return None

    def front(self):
        if self.tail:
            return self.tail.value
        else:
            return None
        
    def empty(self) -> bool:
        return self.size == 0
    
    def contains(self, item) -> bool:
        return self.__get_node(item) is not None
    
    def clear(self):
        self.tail = None
        self.head = None
        self.size = 0

    def to_string(self) -> str:
        if self.size == 0:
            return "[]"
        to_string = "["
        node = self.head
        while node is not self.tail:
            to_string += str(node.value) + ", "
            node = node.next

        to_string += str(node.value) + "]"
        return to_string