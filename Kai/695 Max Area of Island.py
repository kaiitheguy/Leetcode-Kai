# https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0
        self.m = len(grid)
        self.n = len(grid[0])
        queue = []
        visited = set()
            
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.bfs(grid, visited, queue, i, j)
        
        return self.max_area
    
    def bfs(self, grid, visited, queue, i, j):
        area = 1
        queue.append((i,j))
        visited.add((i,j))
        while queue:
            node = queue.pop()
            for direction in [(1,0), (-1,0), (0,1), (0,-1)]:
                new_i = node[0] + direction[0]
                new_j = node[1] + direction[1]
                if new_i >= 0 and new_i <= self.m-1 and new_j >= 0 and new_j <= self.n-1:
                    if grid[new_i][new_j] == 1:
                        if (new_i,new_j) not in visited:
                            area += 1
                            queue.append((new_i,new_j))
                            visited.add((new_i,new_j))
        if area >= self.max_area:
            self.max_area = area