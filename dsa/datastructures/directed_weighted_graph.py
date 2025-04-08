class Node:
    def __init__(self, key):
        self.key = key


class Edge:
    def __init__(self, key, weight, directed):
        self.key = key
        self.weight = weight
        self.directed = directed


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, weight):
        startEdge = Edge(end, weight, True)
        endEdge = Edge(start, weight, False)
        if start in self.graph.keys():
            self.graph[start].add(startEdge)
        else:
            self.graph[start] = set([startEdge])
        if end in self.graph.keys():
            self.graph[end].add(endEdge)
        else:
            self.graph[end] = set([endEdge])

    def dfs(self, start, end):
        visited = []
        self.dfs_r(visited, start, end)
        return visited

    def dfs_r(self, visited, current, target):
        visited.append(current)
        if current == target:
            return
        neighbours = self.graph[current]
        for n in neighbours:
            if n not in visited:
                self.dfs_r(visited, n, target)
