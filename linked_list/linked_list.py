class node:
    def __init__(self, value = None, previous = None, next = None):
        self.value = value
        self.previous = previous
        self.next = next

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
            return self.pop_front()
        if pos == self.size - 1:
            return self.pop_back()

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
        
    def sort(self):
        self.mergesort()

    def bubblesort(self):
        i = 0
        dummy = node(next=self.head)
        self.head.previous = dummy
        while i < self.size:
            j = 0
            cur = dummy.next
            while j < self.size - i - 1:
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
        self.head = dummy.next
        self.head.previous = None
        cur = self.head
        while cur.next:
            cur = cur.next

        self.tail = cur

    def mergesort(self):

        def find_middle(node) -> node:
            fast = node
            slow = node
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next

            return slow.previous

        def merge(l, r) -> node:
            dummy = node()
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

            self.tail = cur
            dummy.next.previous = None
            return dummy.next

        def recursion(head) -> node:
            if not head or not head.next:
                return head
            middle = find_middle(head)
            next_middle = middle.next
            next_middle.previous = None
            middle.next = None
            l = recursion(head)
            r = recursion(next_middle)
            return merge(l, r)
        
        self.head = recursion(self.head)


    def quicksort(self):

        def partition(head) -> node:
            pivot = head
            l1 = node()
            l2 = node()
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
            
        def recursion(head) -> node:
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
        
        self.head = recursion(self.head)
        new_tail = self.head
        while new_tail.next:
            new_tail = new_tail.next

        self.tail = new_tail

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