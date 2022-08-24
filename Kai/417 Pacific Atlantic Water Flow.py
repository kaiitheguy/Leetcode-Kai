# https://leetcode.com/problems/pacific-atlantic-water-flow/

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        self.m = len(heights)
        self.n = len(heights[0])
        self.grid = [[[0,0] for _ in range(self.n)] for _ in range(self.m)]
        
        for i in range(self.m):
            for j in range(self.n):
                if i == 0 or j == 0:
                    self.grid[i][j][0] = 1
                if i == self.m-1 or j == self.n-1:
                    self.grid[i][j][1] = 1
                    
        for i in range(self.m):
            self.dfs(heights, i, 0, 0)
            self.dfs(heights, i, self.n-1, 1)
        for j in range(self.n):
            self.dfs(heights, 0, j, 0)
            self.dfs(heights, self.m-1, j, 1)
    
        res = []
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j][0]==1 and self.grid[i][j][1]==1:
                    res.append([i,j])
        return res
        
        
    def dfs(self, heights, i, j, pos):
        height = heights[i][j]
        if i > 0 and heights[i-1][j] >= height and self.grid[i-1][j][pos] != 1:
            self.grid[i-1][j][pos] = 1
            self.dfs(heights, i-1, j, pos)
        if i < len(self.grid)-1 and heights[i+1][j] >= height and self.grid[i+1][j][pos] != 1:
            self.grid[i+1][j][pos] = 1
            self.dfs(heights, i+1, j, pos)
        if j > 0 and heights[i][j-1] >= height and self.grid[i][j-1][pos] != 1:
            self.grid[i][j-1][pos] = 1
            self.dfs(heights, i, j-1, pos)
        if j < len(self.grid[0])-1 and heights[i][j+1] >= height and self.grid[i][j+1][pos] != 1:
            self.grid[i][j+1][pos] = 1
            self.dfs(heights, i, j+1, pos)
        