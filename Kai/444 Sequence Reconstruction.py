# https://leetcode.com/problems/sequence-reconstruction/

from collections import defaultdict

class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for sequence in sequences:
            for n in sequence:
                indegree[n] = 0
            for i in range(len(sequence)-1):
                graph[sequence[i]].append(sequence[i+1])
        for node in graph.keys():
            for neighbour in graph[node]:
                indegree[neighbour] += 1
                
        queue = []
        topo_order = []
        for node in indegree.keys():
            if indegree[node] == 0:
                queue.append(node)
               
        while queue:
            if len(queue) > 1:
                return False
            node = queue.pop()
            topo_order.append(node)
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return len(nums) == len(topo_order)
        