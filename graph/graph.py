import heapq

class Graph:

    def __init__(self):
        self.__nodes = {}

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
        return str(self.__nodes)
            
    def add_node(self, node):
        if node in self.__nodes:
            raise ValueError("Graph.add_node(node): node already in graph")
        
        self.__nodes[node] = {}

    def pop_node(self, node):
        if node not in self.__nodes:
            raise ValueError("Graph.pop_node(node): node not in graph")
        
        for n in self.__nodes:
            if node in self.__nodes[n]:
                self.__nodes[n].pop(node)
        
        return self.__nodes.pop(node)


    def add_edge(self, from_node, to_node, distance=1, directed=True):
        if from_node in self.__nodes and to_node in self.__nodes:
            self.__nodes[from_node][to_node] = distance
            if not directed:
                self.__nodes[to_node][from_node] = distance
        else:
            raise ValueError("Graph.add_edge(from_node, to_node, distance, directed=): one or both nodes not in graph")
        
    def remove_edge(self, from_node, to_node, directed=True):
        if from_node in self.__nodes and to_node in self.__nodes:
            self.__nodes[from_node].pop(to_node)
            if not directed:
                self.__nodes[to_node].pop(from_node)
        else:
            raise ValueError("Graph.remove_edge(from_node, to_node, directed): one or both nodes not in graph")

    def get_nodes(self):
        return list(self.__nodes)
    
    def get_edges(self):
        edges = []
        for from_node in self.__nodes:
            for to_node, weight in self.__nodes[from_node].items():
                edges.append((from_node, to_node, weight))
        
        return edges
    
    def dijkstra(self, start_node) -> dict:
        if start_node not in self.__nodes:
            raise ValueError("Graph.dijkstra(start_node): start node not in graph")
        
        heap = []
        heapq.heappush(heap, (0, start_node))
        visited = set()
        distances = {node: (float('inf'), None) for node in self.__nodes}
        distances[start_node] = (0, None)

        while heap:
            cur_distance, current = heapq.heappop(heap)
            if current in visited:
                continue
            visited.add(current)

            neighbors = self.__nodes[current]

            for neighbor, weight in neighbors.items():
                if neighbor not in visited:
                    distance, _ = distances[neighbor]
                    new_distance = cur_distance + weight
                    if new_distance < distance:
                        distances[neighbor] = (new_distance, current)
                        heapq.heappush(heap, (new_distance, neighbor))

        return distances
        
    def shortest_path(self, start_node, end_node):
        if start_node not in self.__nodes:
            raise ValueError("Graph.shortest_path(start_node, end_node): start node not in graph")
        
        if end_node not in self.__nodes:
            raise ValueError("Graph.shortest_path(start_node, end_node): end node not in graph")

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
    
    def has_path(self, start_node, end_node):
        if start_node == end_node:
            return True
        
        visited = set()
        def __has_path(cur):
            if cur == end_node:
                return True
            visited.add(cur)
            neighbors = self.__nodes[cur]
            for neighbor in neighbors:
                if not neighbor in visited and __has_path(neighbor):
                    return True
            
            return False
                
        return __has_path(start_node)
            
    
    def has_cycle(self):
        visited = {}

        def __has_cycle(previous, node):
            if visited.get(node) == 1:
                return True
            
            if visited.get(node) == 2:
                return False
            
            visited[node] = 1
            neighbors = self.__nodes[node]
            for neighbor in neighbors.keys():
                if previous != neighbor and __has_cycle(node, neighbor):
                    return True
                
            visited[node] = 2
            return False

        for node in self.get_nodes():
            if node not in visited:
                if __has_cycle(None, node):
                    return True
                visited = {}
        
        return False
    
    def size(self) -> int:
        return len(self.__nodes)
    
    def empty(self) -> bool:
        return len(self.__nodes) == 0
    
    def clear(self):
        self.__nodes = {}