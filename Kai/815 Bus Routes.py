# https://leetcode.com/problems/bus-routes/

class Solution(object):
    def numBusesToDestination(self, routes, source, target):
        """
        :type routes: List[List[int]]
        :type source: int
        :type target: int
        :rtype: int
        """
        if source == target:
            return 0
        
        start_bus = []
        end_bus = []
        adj_mat = collections.defaultdict(list)
        for i in range(len(routes)):
            if source in routes[i] and target in routes[i]:
                return 1
            if source in routes[i]: 
                start_bus.append(i)
            if target in routes[i]: 
                end_bus.append(i) 
            for j in range(i+1, len(routes)):
                if set(routes[i]).intersection(set(routes[j])):
                    adj_mat[i].append(j)
                    adj_mat[j].append(i)                       
        
        min_dist = 500
        for i in start_bus:
            for j in end_bus:
                temp = self.bfs([], [], adj_mat, routes, i, j)
                if temp < min_dist and temp >= 0:
                    min_dist = temp
                    
        if min_dist < 500:
            return min_dist
        else:
            return -1

        
    def bfs(self, visited, queue, adj_mat, routes, source, target):        
        visited.append(source)
        queue.append((source,1))

        while queue:
            node = queue.pop(0) 
            if node[0] == target:
                return node[1]

            for neighbour in adj_mat[node[0]]:
                if neighbour == target:
                    return node[1]+1
                
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append((neighbour,node[1]+1))
                
        return -1