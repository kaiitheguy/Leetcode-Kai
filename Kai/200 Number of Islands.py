# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        grid[i][j] = "0"
        if i > 0 and grid[i-1][j] == "1":
            self.bfs(grid, i-1, j)
        if i < len(grid)-1 and grid[i+1][j] == "1":
            self.bfs(grid, i+1, j)
        if j > 0 and grid[i][j-1] == "1":
            self.bfs(grid, i, j-1)
        if j < len(grid[0])-1 and grid[i][j+1] == "1":
            self.bfs(grid, i, j+1)

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(Solution().numIslands(grid))
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid))