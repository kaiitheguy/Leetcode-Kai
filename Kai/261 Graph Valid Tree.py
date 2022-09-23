# https://leetcode.com/problems/graph-valid-tree/

from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        visited = set()
        self.dfs(graph, visited, 0)
        return len(visited) == n
        
    def dfs(self, graph, visited, node):
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour not in visited:
                self.dfs(graph, visited, neighbour)
