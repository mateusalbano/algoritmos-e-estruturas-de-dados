import sys
sys.path.insert(0, '..')

from array_list import ArrayList

class Heap:

    def __init__(self):
        self.__items = ArrayList()

    def __iter__(self):
        return self.__items.__iter__()

    def __next__(self):
        return self.__items.__next__()
    
    def __len__(self) -> int:
        return len(self.__items)
    
    def __getitem__(self, pos: int):
         return self.__items[pos]
    
    def __str__(self) -> str:
        return self.__items.__str__()

    def enqueue(self, item):
        self.__items.push_back(item)
        self.__heapify_up(self.__items.size() - 1)

    def __heapify_up(self, index):
        parent_idx = self.__parent(index)
        if parent_idx < 0:
            return
        
        cur = self.__items.get_at(index)
        parent = self.__items.get_at(parent_idx)
        cur_key = cur[0] if isinstance(cur, tuple) else cur
        parent_key = parent[0] if isinstance(parent, tuple) else parent
        if cur_key < parent_key:
            self.__items.swap(index, parent_idx)
            self.__heapify_up(parent_idx)


    def __parent(self, index):
        return (index - 1) // 2

    def __left_child(self, index):
        return 2 * index + 1

    def __right_child(self, index):
        return 2 * index + 2
    
    def peek(self) -> any:
        if self.size() == 0:
            raise IndexError("empty heap")
        return self.__items[0]

    def dequeue(self):
        if self.size() == 0:
            raise IndexError("empty heap")
        root = self.__items[0]
        last_idx = self.size() - 1
        if last_idx == 0:
            self.__items.pop_back()
            return root

        last = self.__items.get_at(last_idx)
        self.__items.replace_at(0, last)
        self.__items.pop_back()
        self.__heapify_down(0)
        return root

    def __heapify_down(self, index):
        item = self.__items[index]
        priority = item[0] if isinstance(item, tuple) else item
        left_idx = self.__left_child(index)
        right_idx = self.__right_child(index)
        smallest = index

        if left_idx < self.size():
            left = self.__items[left_idx]
            left_priority = left[0] if isinstance(left, tuple) else left
            if left_priority < priority:
                priority = left_priority
                smallest = left_idx
        
        if right_idx < self.size():
            right = self.__items[right_idx]
            right_priority = right[0] if isinstance(right, tuple) else right
            if right_priority < priority:
                priority = right_priority
                smallest = right_idx

        if smallest != index:
            self.__items.swap(index, smallest)
            self.__heapify_down(smallest)


    def size(self) -> int:
        return self.__items.size()
    
    def empty(self) -> bool:
        return self.__items.empty()