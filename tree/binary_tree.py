from queue import Queue
class Node:
    def __init__(self, value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
class BinaryTree:

    def __init__(self):
        self.__root = None
        self.__size = 0

    def __iter__(self):
        self.__nodes = []
        if self.__root:
            self.__nodes.append(self.__root)
        return self
    
    def __next__(self):
        if len(self.__nodes) != 0:
            node = self.__nodes.pop()
            item = node.value
            if node.left:
                self.__nodes.append(node.left)
            if node.right:
                self.__nodes.append(node.right)

            return item
        else:
            raise StopIteration

    def __len__(self) -> int:
        return self.__size
    
    def __str__(self) -> str:
        items = []
        queue = Queue()
        
        if self.__root:
            queue.put(self.__root)

        while not queue.empty():
            levelSize = queue.qsize()
            while levelSize != 0:
                cur = queue.get()
                items.append(cur.value)
                if cur.left:
                    queue.put(cur.left)
                elif cur.right:
                    items.append(None)
                
                if cur.right:
                    queue.put(cur.right)
                elif cur.left:
                    items.append(None)

                levelSize -= 1

        return str(items)

    def insert(self, item):
        def __insert(cur: Node, item):
            if item > cur.value:
                if cur.right:
                    __insert(cur.right, item)
                else:
                    cur.right = Node(value=item)
            else:
                if cur.left:
                    __insert(cur.left, item)
                else:
                    cur.left = Node(value=item)

        if self.__root:
            __insert(self.__root, item)
        else:
            self.__root = Node(value=item)
            self.__nodes = [self.__root]
        self.__size += 1

    
    def dfs(self, item) -> bool:
        def __dfs(cur: Node, item) -> bool:
            return cur != None and (cur.value == item or __dfs(cur.left, item) or __dfs(cur.right, item))
        
        return __dfs(cur=self.__root, item=item)
    
    def bfs(self, item) -> bool:
        if not self.__root:
            return False
        
        q = Queue()
        q.put(self.__root)

        while not q.empty():
            cur = q.get()
            if cur.value == item:
                return True
            
            if cur.left:
                q.put(cur.left)

            if cur.right:
                q.put(cur.right)

        return False
            
    def preorder_traversal(self) -> list: 
        traversal = []
        def __preorder_traversal(cur: Node):
            if not cur:
                return
            traversal.append(cur.value)
            __preorder_traversal(cur.left)
            __preorder_traversal(cur.right)
            
        __preorder_traversal(self.__root)
        return traversal

    def inorder_traversal(self) -> list: 
        traversal = []
        def __inorder_traversal(cur: Node):
            if not cur:
                return
            __inorder_traversal(cur.left)
            traversal.append(cur.value)
            __inorder_traversal(cur.right)

        __inorder_traversal(self.__root)
        return traversal
    
    def postorder_traversal(self) -> list: 
        traversal = []

        def __postorder_traversal(cur: Node):
            if not cur:
                return
            __postorder_traversal(cur.left)
            __postorder_traversal(cur.right)
            traversal.append(cur.value)
        
        __postorder_traversal(self.__root)
        return traversal
    
    def size(self) -> int:
        return self.__size

    def empty(self) -> bool:
        return self.__size == 0
    
    def contains(self, item) -> bool:
        def __contains(cur: Node, item) -> bool:
            if item == cur.value:
                return True
            if item > cur.value:
                if cur.right:
                    return __contains(cur.right, item)
                else:
                    return False
            else:
                if cur.left:
                    return __contains(cur.left, item)
                else:
                    return False
                
        if self.__root:
            return __contains(self.__root, item)
        
        return False

    def clear(self):
        self.__root = None
        self.__size = 0