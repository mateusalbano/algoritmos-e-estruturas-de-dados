import sys
from pathlib import Path

# Add parent directory to path for imports
parent_dir = str(Path(__file__).parent.parent)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

import importlib.util
queue_spec = importlib.util.spec_from_file_location("queue_module", str(Path(__file__).parent.parent / "queue" / "heap.py"))
queue_module = importlib.util.module_from_spec(queue_spec)
queue_spec.loader.exec_module(queue_module)
Heap = queue_module.Heap


class Node:
    def __init__(self, value):
        self.__value = value
        self.__neighbors = {}

    def __str__(self) -> str:
        return str(self.__value)

    def add_neighbor(self, neighbor, distance=1):
        self.__neighbors[neighbor] = distance

    def remove_neighbor(self, neighbor):
        self.__neighbors.pop(neighbor, None)

    def get_neighbors(self):
        return self.__neighbors
    
    @property
    def value(self):
        return self.__value

class Graph:

    def __init__(self):
        self.__nodes = set()

    def add_node(self, node):
        if node in self.__nodes:
            raise ValueError("Node already exists in graph")
        
        self.__nodes.add(node)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self) -> any:
        if self.__index < len(self):
            item = list(self.__nodes)[self.__index]
            self.__index += 1
            return item
        else:
            raise StopIteration

    def __len__(self) -> int:
        return len(self.__nodes)

    def __str__(self) -> str:
        if self.empty():
            return "[]"
        
        to_string = ""
        nodes = list(self.__nodes)
        def _to_string(i):
            nonlocal to_string
            to_string += str(nodes[i])
            to_string += " -> "
            neighbors = list(nodes[i].get_neighbors().items())

            if len(neighbors) == 0:
                to_string += "None"
                return

            for j in range(len(neighbors) - 1):
                to_string += str(neighbors[j][0]) + ", "
            to_string += str(neighbors[-1][0])
            

        for i in range(len(nodes) - 1):
            _to_string(i)
            to_string += "\n"

        _to_string(-1)
        return to_string
            

    def pop_node(self, node: Node) -> any:
        if self.empty():
            raise RuntimeError("graph is empty")
        self.__nodes.remove(node)
        node.get_neighbors().clear()

        for cur in self.__nodes:
            cur.remove_neighbor(node)
        
        return node.value


    def add_edge(self, from_node: Node, to_node: Node, distance=1, directed=True):
        if from_node in self.__nodes and to_node in self.__nodes:
            from_node.add_neighbor(to_node, distance)
            if not directed:
                to_node.add_neighbor(from_node, distance)
        else:
            raise ValueError("one or both nodes not in graph")
        
    def remove_edge(self, from_node, to_node, directed=True):
        if from_node in self.__nodes and to_node in self.__nodes:
            from_node.remove_neighbor(to_node)
            if not directed:
                to_node.remove_neighbor(from_node)
        else:
            raise ValueError("one or both nodes not in graph")

    def get_nodes(self):
        return list(self.__nodes)
    
    def empty(self) -> bool:
        return len(self.__nodes) == 0
    
    def dijkstra(self, start_node: Node) -> dict:
        heap = Heap()
        heap.enqueue((0, start_node))
        visited = set()
        distances = {node: (float('inf'), None) for node in self.__nodes}
        distances[start_node] = (0, None)

        while not heap.empty():
            cur_distance, current = heap.dequeue()
            if current in visited:
                continue
            visited.add(current)

            neighbors = current.get_neighbors()

            for neighbor, weight in neighbors.items():
                if neighbor not in visited:
                    distance, _ = distances[neighbor]
                    new_distance = cur_distance + weight
                    if new_distance < distance:
                        distances[neighbor] = (new_distance, current)
                        heap.enqueue((new_distance, neighbor))

        return distances
        
    
    def shortest_path(self, start_node, end_node):
        if start_node == end_node:
            return []
        distances = self.dijkstra(start_node)
        path = []
        node = end_node
        if distances[node][0] == float('inf'):
            return []
        
        while node != start_node:
            path.append(node)
            node = distances[node][1]
            
        path.append(node)
        path.reverse()
        return path
    
    def has_path(start_node: Node, end_node: Node):
        visited = set()
        def __has_path(cur):
            if cur == end_node:
                return True
            visited.add(cur)
            neighbors = cur.get_neighbors()
            for neighbor in neighbors:
                if not neighbor in visited and __has_path(neighbor):
                    return True
                
        return __has_path(start_node)
            
    
    def has_cycle(self):
        visited = {}

        def __has_cycle(node):
            if visited.get(node) == 1:
                return True
            
            if visited.get(node) == 2:
                return False
            
            visited[node] = 1
            neighbors = node.get_neighbors()
            for neighbor in neighbors.keys():
                if __has_cycle(neighbor):
                    return True
                
            visited[node] = 2
            return False

        for node in self.get_nodes():
            if node not in visited:
                if __has_cycle(node):
                    return True
                visited = {}
        
        return False