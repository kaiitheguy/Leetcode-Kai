# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        queue=[]
        #create graph dict
        for i in edges:
            graph[i[0]].append(i[1])    
            graph[i[1]].append(i[0])         
        res=0
        for i in graph.keys():
            if i not in visited:
                self.bfs(graph,visited,queue,i)
                res+=1
        return res+(n-len(graph))
        #bfs
    def bfs(self,graph,visited,queue,node):
        visited.add(node)
        queue.append(node)
        while queue:         
            m = queue.pop(0) 
            for neighbour in graph[m]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
       
      
        