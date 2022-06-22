# https://leetcode.com/problems/dungeon-game/

class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        
        res = [[None for _ in range(n)] for _ in range(m)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                res[i][j] = self.findMinCost(i, j, dungeon, res)
        
        """
        visited = []
        queue = []
        
        visited.append((m-1, n-1))
        queue.append((m-1, n-1))
        
        while queue:
            node = queue.pop(0)
            i = node[0]
            j = node[1]
            
            res[i][j] = self.findMinCost(i, j, dungeon, res)
            
            if (node[0]-1, node[1]) not in visited and node[0]-1 >= 0:
                queue.append((node[0]-1, node[1]))
            
            if (node[0], node[1]-1) not in visited and node[1]-1 >= 0:
                queue.append((node[0], node[1]-1))
        """
            
        return res[0][0]
    
    def findMinCost(self, i, j, dungeon, res):
        m = len(dungeon)
        n = len(dungeon[0])
        
        if i >= m-1 and j >= n-1:
            return abs(min(dungeon[i][j], 0)) + 1
        elif i >= m-1:
            return max(res[i][j+1] - dungeon[i][j], 1)
        elif j >= n-1:
            return max(res[i+1][j] - dungeon[i][j], 1)
        else:
            return max(min(res[i][j+1], res[i+1][j]) - dungeon[i][j], 1)
            
        
        