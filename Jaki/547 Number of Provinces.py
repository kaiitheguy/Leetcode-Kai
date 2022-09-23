# https://leetcode.com/problems/number-of-provinces/

from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            now = i+1
            for j in range(len(isConnected[i])):
                check_now = j+1
                if now!=check_now and isConnected[i][j]==1:
                    graph[now].append(check_now)
        visited = set()
        res=0
        for k in range(len(isConnected)):
            if k+1 not in visited:
                self.dfs(visited,graph,k+1)
                res += 1
        return res
        
    def dfs(self,visited, graph, node):
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                self.dfs(visited, graph, neighbour)

            