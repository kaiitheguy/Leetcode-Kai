# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for e in edges:
            i = e[0]
            j = e[1]
            graph[i].append(j)
            graph[j].append(i)
        
        count = 0
        visited = [] 
        queue = []
        for node in range(n):
            if node not in visited:
                count += 1
                visited.append(node)
                queue.append(node)
            while queue:
                node = queue.pop()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        visited.append(neighbour)
                        queue.append(neighbour)
        
        return count