class Node:
    def __init__(self, value = None, previous = None, next = None):
        self.value = value
        self.previous = previous
        self.next = next

class DoublyLinkedList():
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __iter__(self):
        self.__node = self.__head
        return self

    def __next__(self):
        if self.__node != None:
            item = self.__node.value
            self.__node = self.__node.next
            return item
        else:
            raise StopIteration
    
    def __getitem__(self, pos: int):
         return self.get_at(pos)
    
    def __setitem__(self, pos: int, item):
        self.replace_at(pos, item)
    
    def __len__(self) -> int:
        return self.__size
    
    def __str__(self) -> str:
        if self.__size == 0:
            return "[]"
        to_string = "["
        node = self.__head
        while node is not self.__tail:
            to_string += str(node.value) + ", "
            node = node.next

        to_string += str(node.value) + "]"
        return to_string
    
    def __get_node(self, item) -> Node:
        node = self.__head
        while node:
            if node.value == item:
                break
            node = node.next
        return node
    
    def __get_node_at(self, pos: int) -> Node:
        if pos < 0 or pos > self.__size - 1:
            raise IndexError("DoublyLinkedList.__get_node_at(pos): list index out of range")
        node = self.__head
        i = 0
        while node:
            if i == pos:
                break
            node = node.next
            i += 1
        return node
    
    def push_front(self, item):
        if self.__size == 0:
            self.__head = Node(item)
            self.__tail = self.__head
        else:
            new_node = Node(item)
            new_node.next = self.__head
            self.__head.previous = new_node
            self.__head = new_node
        self.__size += 1

    def push_back(self, item):
        if self.__size == 0:
            self.__head = Node(item)
            self.__tail = self.__head
        else:
            new_node = Node(item)
            new_node.previous = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def pop_front(self):
        if self.__size == 0:
            raise IndexError("DoublyLinkedList.pop_front(): pop from empty list")
        
        last_item = self.__head.value
        if self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.previous = None
        
        self.__size -= 1
        return last_item
    
    def pop_back(self):
        if self.__size == 0:
            raise IndexError("DoublyLinkedList.pop_back(): pop from empty list")
        
        last_item = self.__tail.value
        if self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.previous
            self.__tail.next = None
        
        self.__size -= 1
        return last_item
    
    def front(self):
        if self.__head:
            return self.__head.value
        else:
            return None
        
    def back(self):
        if self.__tail:
            return self.__tail.value
        else:
            return None

    def insert_at(self, pos: int, item):
        if pos == 0:
            self.push_front(item)
            return
        if pos == self.__size:
            self.push_back(item)
            return

        this_node = self.__get_node_at(pos)
        new_node = Node(item)
        this_node.previous.next = new_node
        new_node.previous = this_node.previous
        new_node.next = this_node
        this_node.previous = new_node
        self.__size += 1

    def remove_at(self, pos: int):
        if pos == 0:
            return self.pop_front()
        if pos == self.__size - 1:
            return self.pop_back()

        node = self.__get_node_at(pos)
        node.previous.next = node.next
        node.next.previous = node.previous
        self.__size -= 1
        return node.value
    
    def get_at(self, pos: int):
        return self.__get_node_at(pos).value

    def replace_at(self, pos: int, item):
        self.__get_node_at(pos).value = item

    def replace(self, item, new_item):
        node = self.__get_node(item)
        if node:
            node.value = new_item
        else:
            raise ValueError("DoublyLinkedList.replace(item, new_item): item not in list")
        
    def remove(self, item):
        node = self.__get_node(item)
        if not node:
            raise ValueError("DoublyLinkedList.remove(item): item not in list")
        if node is self.__head:
            return self.pop_front()
        if node is self.__tail:
            return self.pop_back()
        
        node.previous.next = node.next
        node.next.previous = node.previous
        self.__size -= 1
        return node.value
        
    def sort(self):
        self.mergesort()

    def bubblesort(self):
        if self.__size < 2:
            return
        
        i = 0
        dummy = Node(next=self.__head)
        self.__head.previous = dummy
        while i < self.__size:
            j = 0
            cur = dummy.next
            while j < self.__size - i - 1:
                next = cur.next
                next_next = next.next
                previous = cur.previous
                swap = False
                if cur.value > next.value:
                    swap = True
                    previous.next = next
                    next.previous = previous
                    next.next = cur
                    cur.previous = next
                    cur.next = next_next
                    if next_next:
                        next_next.previous = cur

                if not swap:
                    cur = cur.next
                j += 1
            
            i += 1
        self.__head = dummy.next
        self.__head.previous = None
        cur = self.__head
        while cur.next:
            cur = cur.next

        self.__tail = cur

    def mergesort(self):
        if self.__size < 2:
            return
        
        def find_middle(node):
            fast = node
            slow = node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            return slow.previous

        def merge(l, r):
            dummy = Node()
            cur = dummy
            while l and r:
                if l.value < r.value:
                    cur.next = l
                    l.previous = cur
                    cur = l
                    l = l.next
                else:
                    cur.next = r
                    r.previous = cur
                    cur = r
                    r = r.next 

            while l:
                cur.next = l
                l.previous = cur
                cur = l
                l = l.next

            while r:
                cur.next = r
                r.previous = cur
                cur = r
                r = r.next

            self.__tail = cur
            dummy.next.previous = None
            return dummy.next

        def recursion(head):
            if not head or not head.next:
                return head
            middle = find_middle(head)
            next_middle = middle.next
            next_middle.previous = None
            middle.next = None
            l = recursion(head)
            r = recursion(next_middle)
            return merge(l, r)
        
        self.__head = recursion(self.__head)


    def quicksort(self):
        if self.__size < 2:
            return
        
        def partition(head):
            pivot = head
            l1 = Node()
            l2 = Node()
            dummy1 = l1
            dummy2 = l2
            while head:
                next = head.next
                head.next = None
                if head.value < pivot.value:
                    l1.next = head
                    head.previous = l1
                    l1 = l1.next
                else:
                    l2.next = head
                    head.previous = l2
                    l2 = l2.next
                head = next

            l1.next = dummy2.next
            dummy2.next.previous = l1
            dummy1.next.previous = None
            return dummy1.next, pivot

        def recursion(head):
            if not head or not head.next:
                return head
            head, pivot = partition(head)
            next = pivot.next
            pivot.next = None
            if next:
                next.previous = None
            l = recursion(head)
            head = l
            r = recursion(next)
            while l.next:
                l = l.next

            l.next = r
            if r:
                r.previous = l
            return head
        
        self.__head = recursion(self.__head)
        new_tail = self.__head
        while new_tail.next:
            new_tail = new_tail.next

        self.__tail = new_tail

    def size(self) -> int:
        return self.__size
    
    def empty(self) -> bool:
        return self.__size == 0

    def contains(self, item) -> bool:
        return self.__get_node(item) is not None
    
    def clear(self):
        self.__tail = None
        self.__head = None
        self.__size = 0