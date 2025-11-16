class ArrayList():
    def __init__(self, initialSize: int = 10):
        self.__data = [None] * initialSize
        self.__size = 0

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self) -> any:
        if self.__index < self.__size:
            item = self.get_at(self.__index)
            self.__index += 1
            return item
        else:
            raise StopIteration
    
    def __len__(self) -> int:
        return self.__size
    
    def __getitem__(self, pos: int):
         return self.get_at(pos)
    
    def __setitem__(self, pos: int, item: any):
        self.replace_at(pos, item)
    
    def __str__(self):
        if self.__size == 0:
            return "[]"
        to_string = "["
        i = 0
        while i < self.__size - 1:
            to_string += str(self.__data[i]) + ", "
            i += 1
        
        to_string += str(self.__data[self.__size - 1]) + "]"
        return to_string

    def __relocate(self, newSize = 10):
        temp = [None] * newSize
        i = 0
        while i < self.__size:
            temp[i] = self.__data[i]
            i += 1
        self.__data = temp

    def size(self) -> int:
        return self.__size

    def push_back(self, item):
        if self.__size == len(self.__data):
            self.__relocate(max(2, int(self.__size * 1.5)))

        self.__data[self.__size] = item
        self.__size += 1

    def pop_back(self):
        if self.__size == 0:
            raise IndexError("pop from empty list")
        self.__size -= 1
        item = self.__data[self.__size]
        self.__data[self.__size] = None
        return item
    
    def get_at(self, pos: int):
        if pos < 0 or pos > self.__size - 1:
            raise IndexError("list index out of range")
        
        return self.__data[pos]
    
    def search(self, item) -> int:
        i = 0
        while i < self.__size:
            if self.__data[i] == item:
                return i
            i += 1
        return -1
    
    def replace(self, item, new_item):
        pos = self.search(item)
        if pos != -1:
            self.__data[pos] = new_item
        else:
            raise ValueError("array_list.replace(item, new_item): item not in list")
        
    def replace_at(self, pos: int, new_item):
        if pos < 0 or pos > self.__size - 1:
            raise IndexError("list index out of range")
        self.__data[pos] = new_item

    def insert_at(self, pos: int, item):
        if pos < 0 or pos > self.__size:
            raise IndexError("list index out of range")
        
        if self.__size == len(self.__data):
            self.__relocate(max(2, int(self.__size * 1.5)))
        
        i = self.__size
        while i > pos:
            self.__data[i] = self.__data[i - 1]
            i -= 1
        self.__data[pos] = item
        self.__size += 1

    def remove(self, item):
        pos = self.search(item)
        if pos == -1:
            raise ValueError("array_list.remove(item): item not in list")
        
        return self.remove_at(pos)

    def remove_at(self, pos: int):
        if pos < 0 or pos > self.__size - 1:
            raise IndexError("list index out of range")
        
        if pos == self.__size - 1 or self.__size == 1:
           return self.pop_back()
        
        item = self.__data[pos]
        i = pos
        while i < self.__size - 1:
            self.__data[i] = self.__data[i + 1]
            i += 1

        self.__data[self.__size - 1] = None
        self.__size -= 1
        return item
    
    def swap(self, pos1: int, pos2: int):
        if pos1 < 0 or pos1 > self.size() - 1:
            raise IndexError("list index out of range")

        if pos2 < 0 or pos2 > self.size() - 1:
            raise IndexError("list index out of range")

        self.__data[pos1], self.__data[pos2] = self.__data[pos2], self.__data[pos1]

    def clear(self, initialSize: int = 10):
        self.__data = [None] * initialSize
        self.__size = 0

    def sort(self):
        self.quicksort()

    def bubblesort(self):
        i = 0
        j = 0
        while i < self.__size:
            is_sorted = True
            while j < self.__size - i - 1:
                if self.__data[j] > self.__data[j + 1]:
                    self.__data[j], self.__data[j + 1] = self.__data[j + 1], self.__data[j]
                    is_sorted = False
                j += 1
            if is_sorted:
                break
            j = 0
            i += 1

    def mergesort(self):
        def merge(l, middle, r):
            left = self.__data[l : middle + 1]
            right  = self.__data[middle + 1 : r + 1]
            i, j= 0, 0
            k = l
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.__data[k] = left[i]
                    k += 1
                    i += 1
                else:
                    self.__data[k] = right[j]
                    k += 1
                    j += 1

            while i < len(left):
                self.__data[k] = left[i]
                k += 1
                i += 1

            while j < len(right):
                self.__data[k] = right[j]
                k += 1
                j += 1
            

        def recursion(l, r):
            if l >= r:
                return
            middle = int((l + r) / 2)
            recursion(l, middle)
            recursion(middle + 1, r)
            merge(l, middle, r)

        recursion(0, self.__size - 1)


    def quicksort(self):
        def partition(l, r):
            pos = r
            pivot = self.__data[r]
            i = l
            j = l
            while j <= r:
                if j == pos:
                    j += 1
                    continue
                if self.__data[j] <= pivot:
                    self.__data[i], self.__data[j] = self.__data[j], self.__data[i]
                    i += 1
                j += 1
            self.__data[i], self.__data[pos] = self.__data[pos], self.__data[i]
            return i
        
        def recursion(l, r):
            if l >= r:
                return
            pivot = partition(l, r)
            recursion(l, pivot - 1)
            recursion(pivot + 1, r)

        recursion(0, self.__size - 1)

    def empty(self) -> bool:
        return self.__size == 0
    
    def contains(self, item) -> bool:
        return self.search(item) != -1