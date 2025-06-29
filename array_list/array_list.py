class array_list():
    def __init__(self, initialSize: int = 10):
        self.data = [None] * initialSize
        self.size = 0

    def __relocate(self, newSize: int):
        temp = [None] * newSize
        i = 0
        while i < self.size:
            temp[i] = self.data[i]
            i += 1
        self.data = temp

    def get_size(self) -> int:
        return self.size

    def push_back(self, item):
        if self.size == len(self.data):
            self.__relocate(max(2, int(self.size * 1.5)))

        self.data[self.size] = item
        self.size += 1

    def pop_back(self):
        if self.size == 0:
            raise IndexError("pop from empty list")
        
        item = self.data[self.size]
        self.data[self.size] = None
        self.size -= 1
        return item
    
    def get_at(self, pos: int):
        if pos < 0 or pos > self.size - 1:
            raise IndexError("list index out of range")
        
        return self.data[pos]
    
    def search(self, item) -> int:
        i = 0
        while i < self.size:
            if self.data[i] == item:
                return i
            i += 1
        return -1
    
    def replace(self, item, new_item):
        pos = self.search(item)
        if pos != -1:
            self.data[pos] = new_item
        else:
            raise ValueError("array_list.replace(item, new_item): item not in list")
        
    def replace_at(self, pos: int, new_item):
        if pos < 0 or pos > self.size - 1:
            raise IndexError("list index out of range")
        self.data[pos] = new_item

    def insert_at(self, pos: int, item):
        if pos < 0 or pos > self.size:
            raise IndexError("list index out of range")
        
        if self.size == len(self.data):
            self.__relocate(max(2, self.newSize * 1.5))
        
        i = self.size
        while i > pos:
            self.data[i] = self.data[i - 1]
            i -= 1
        self.data[pos] = item
        self.size += 1

    def remove(self, item):
        pos = self.search(item)
        if pos == -1:
            raise ValueError("array_list.remove(item): item not in list")
        
        return self.remove_at(pos)

    def remove_at(self, pos: int):
        if pos < 0 or pos > self.size - 1:
            raise IndexError("list index out of range")
        
        if pos == self.size - 1 or self.size == 1:
           return self.pop_back()
        
        item = self.data[pos]
        i = pos
        while i < self.size - 1:
            self.data[i] = self.data[i + 1]
            i += 1

        self.data[self.size - 1] = None
        self.size -= 1
        return item


    def clear(self, initialSize: int = 10):
        self.data = [None] * initialSize
        self.size = 0

    def sort(self):
        self.quicksort()

    def bubblesort(self):
        i = 0
        j = 0
        while i < self.size:
            is_sorted = True
            while j < self.size - i - 1:
                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    is_sorted = False
                j += 1
            if is_sorted:
                break
            j = 0
            i += 1

    def mergesort(self):
        def merge(l, middle, r):
            left = self.data[l : middle + 1]
            right  = self.data[middle + 1 : r + 1]
            i, j= 0, 0
            k = l
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.data[k] = left[i]
                    k += 1
                    i += 1
                else:
                    self.data[k] = right[j]
                    k += 1
                    j += 1

            while i < len(left):
                self.data[k] = left[i]
                k += 1
                i += 1

            while j < len(right):
                self.data[k] = right[j]
                k += 1
                j += 1
            

        def recursion(l, r):
            if l >= r:
                return
            middle = int((l + r) / 2)
            recursion(l, middle)
            recursion(middle + 1, r)
            merge(l, middle, r)

        recursion(0, self.size - 1)


    def quicksort(self):
        def partition(l, r):
            pos = r
            pivot = self.data[r]
            i = l
            j = l
            while j <= r:
                if j == pos:
                    j += 1
                    continue
                if self.data[j] <= pivot:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
                    i += 1
                j += 1
            self.data[i], self.data[pos] = self.data[pos], self.data[i]
            return i
        
        def recursion(l, r):
            if l >= r:
                return
            pivot = partition(l, r)
            recursion(l, pivot - 1)
            recursion(pivot + 1, r)

        recursion(0, self.size - 1)

    def empty(self) -> bool:
        return self.size == 0
    
    def contains(self, item) -> bool:
        return self.search(item) != -1

    def to_string(self) -> str:
        if self.size == 0:
            return "[]"
        to_string = "["
        i = 0
        while i < self.size - 1:
            to_string += str(self.data[i]) + ", "
            i += 1
        
        to_string += str(self.data[self.size - 1]) + "]"
        return to_string