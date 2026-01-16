class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class LinkedList():
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
        previous = None
        while node:
            previous = node
            if node.value == item:
                break
            node = node.next
        return previous, node
    
    def __get_node_at(self, pos: int) -> Node:
        if pos < 0 or pos > self.__size - 1:
            raise IndexError("LinkedList.__get_node_at(pos): list index out of range")
        node = self.__head
        previous = None
        i = 0
        while i < pos:
            previous = node
            node = node.next
            i += 1
        return previous, node

    def push_front(self, item):
        if self.__size == 0:
            self.__head = Node(item)
            self.__tail = self.__head
        else:
            new_node = Node(item)
            new_node.next = self.__head
            self.__head = new_node
        self.__size += 1

    def push_back(self, item):
        if self.__size == 0:
            self.__head = Node(item)
            self.__tail = self.__head
        else:
            new_node = Node(item)
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1

    def pop_front(self):
        if self.__size == 0:
            raise IndexError("LinkedList.pop_front(): pop from empty list")

        last_item = self.__head.value
        if self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next

        self.__size -= 1
        return last_item
    
    def pop_back(self):
        node = None
        if self.__size == 0:
            raise IndexError("LinkedList.pop_back(): pop from empty list")
        if self.__size == 1:
            node = self.__head
            self.__head = None
            self.__tail = None
        else:
            previous, node = self.__get_node_at(self.__size - 1)
            previous.next = None
            self.__tail = previous

        self.__size -= 1
        return node.value
    
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

        previous, node = self.__get_node_at(pos)
        
        new_node = Node(item)
        if previous:
            previous.next = new_node

        new_node.next = node
        self.__size += 1

    def remove_at(self, pos: int):
        if pos == 0:
            return self.pop_front()
        if pos == self.__size - 1:
            return self.pop_back()
        
        previous, node = self.__get_node_at(pos)
        if previous:
            previous.next = node.next

        node.next = None
        self.__size -= 1
        return node.value
    
    def get_at(self, pos: int):
        _, node = self.__get_node_at(pos)
        return node.value

    def replace_at(self, pos: int, item):
        _, node = self.__get_node_at(pos)
        node.value = item

    def replace(self, item, new_item):
        _, node = self.__get_node(item)
        if node:
            node.value = new_item
        else:
            raise ValueError("LinkedList.replace(item, new_item): item not in list")
        
    def remove(self, item):
        previous, node = self.__get_node(item)
        if not node:
            raise ValueError("LinkedList.remove(item): item not in list")
        if node is self.__head:
            return self.pop_front()
        if node is self.__tail:
            return self.pop_back()
    
        previous.next = node.next
        self.__size -= 1
        return node.value
  
    def sort(self):
        self.mergesort()

    def bubblesort(self):
        if self.__size < 2:
            return
        
        i = 0
        dummy = Node(next=self.__head)
        while i < self.__size:
            j = 0
            cur = dummy.next
            previous = dummy
            while j < self.__size - i - 1:
                next = cur.next
                next_next = next.next
                swap = False
                if cur.value > next.value:
                    swap = True
                    previous.next = next
                    cur.next = next_next
                    next.next = cur
                    previous = next

                if not swap:
                    previous = cur
                    cur = cur.next
                j += 1
            
            i += 1
        self.__head = dummy.next
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
            previous = None
            while fast and fast.next:
                previous = slow
                fast = fast.next.next
                slow = slow.next

            return previous

        def merge(l, r):
            dummy = Node()
            cur = dummy
            while l and r:
                if l.value < r.value:
                    cur.next = l
                    cur = l
                    l = l.next
                else:
                    cur.next = r
                    cur = r
                    r = r.next 

            while l:
                cur.next = l
                cur = l
                l = l.next

            while r:
                cur.next = r
                cur = r
                r = r.next

            self.__tail = cur
            return dummy.next

        def recursion(head):
            if not head or not head.next:
                return head
            middle = find_middle(head)
            next_middle = middle.next
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
                    l1 = l1.next
                else:
                    l2.next = head
                    l2 = l2.next
                head = next

            l1.next = dummy2.next
            return dummy1.next, pivot

        def recursion(head):
            if not head or not head.next:
                return head
            head, pivot = partition(head)
            next = pivot.next
            pivot.next = None
            l = recursion(head)
            head = l
            r = recursion(next)
            while l.next:
                l = l.next

            l.next = r
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