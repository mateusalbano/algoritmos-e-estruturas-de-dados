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


    def __iter__(self):
        self.__nodes = []
        if self.__root:
            self.__nodes.append(self.__root)
        return self

    def __next__(self) -> any:
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
    
    def empty(self) -> bool:
        return self.__size == 0

    def insert(self, item):
        if self.__root:
            self.__insert(self.__root, item)
        else:
            self.__root = Node(value=item)
            self.__nodes = [self.__root]
        self.__size += 1

    def __insert(self, cur: Node, item: any):
        if item > cur.value:
            if cur.right:
                self.__insert(cur.right, item)
            else:
                cur.right = Node(value=item)
        else:
            if cur.left:
                self.__insert(cur.left, item)
            else:
                cur.left = Node(value=item)

    def contains(self, item) -> bool:
        if self.__root:
            return self.__contains(self.__root, item)
        
        return False

    def __contains(self, cur: Node, item: any) -> bool:
        if item == cur.value:
            return True
        if item > cur.value:
            if cur.right:
                return self.__contains(cur.right, item)
            else:
                return False
        else:
            if cur.left:
                return self.__contains(cur.left, item)
            else:
                return False
            
    def dfs(self, item: any) -> bool:
        return self.__dfs(cur=self.__root, item=item)

    def __dfs(self, cur: Node, item: any) -> bool:
        if cur:
            print(cur.value)
        return cur != None and (cur.value == item or self.__dfs(cur=cur.left, item=item) or self.__dfs(cur=cur.right, item=item))

    def bfs(self, item: any) -> bool:
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
        self.__preorder_traversal(self.__root, traversal)
        return traversal
    
    def __preorder_traversal(self, cur: Node, list: list):
        if not cur:
            return
        list.append(cur.value)
        self.__preorder_traversal(cur.left, list)
        self.__preorder_traversal(cur.right, list)


    def inorder_traversal(self) -> list: 
        traversal = []
        self.__inorder_traversal(self.__root, traversal)
        return traversal
    
    def __inorder_traversal(self, cur: Node, list: list):
        if not cur:
            return
        self.__inorder_traversal(cur.left, list)
        list.append(cur.value)
        self.__inorder_traversal(cur.right, list)

    def postorder_traversal(self) -> list: 
        traversal = []
        self.__postorder_traversal(self.__root, traversal)
        return traversal
    
    def __postorder_traversal(self, cur: Node, list: list):
        if not cur:
            return
        self.__postorder_traversal(cur.left, list)
        self.__postorder_traversal(cur.right, list)
        list.append(cur.value)