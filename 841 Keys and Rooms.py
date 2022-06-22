# https://leetcode.com/problems/keys-and-rooms/

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        graph = dict(zip(range(len(rooms)), rooms))   
        
        visited = set()
        
        self.dfs(visited, graph, 0)
        
        return sorted(list(visited)) == range(len(rooms))

    def dfs(self, visited, graph, node):
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                self.dfs(visited, graph, neighbour)