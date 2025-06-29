class ordered_array_list():
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
        l = 0
        r = self.size - 1
        while (l < r):
            mid =  int(l + (r - l) / 2)
            if self.data[mid] >= item:
                r = mid
            else:
                l = mid + 1

        if self.data[l] == item:
            return l
        
        return -1
    
    def replace(self, item, new_item):
        pos = self.search(item)
        if pos != -1:
            self.remove_at(pos)
            self.insert(new_item)
        else:
            raise ValueError("array_list.replace(item, new_item): item not in list")
    
    def insert(self, item):
        l = 0
        r = self.size
        while (l < r):
            mid =  int(l + (r - l) / 2)
            if self.data[mid] == item:
                self.insert_at(mid, item)
                return
            if self.data[mid] > item:
                r = mid - 1
            else:
                l = mid + 1

        if l < self.size and item > self.data[l]:
            self.insert_at(l + 1, item)
        else:
            self.insert_at(l, item)
    

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