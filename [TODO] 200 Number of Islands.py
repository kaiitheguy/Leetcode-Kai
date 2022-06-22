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
        self.visited = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    self.bfs(grid, i, j)
                    count += 1
        return count

    def bfs(self, grid, i, j):
        queue = []
        self.visited.append((i, j))
        queue.append((i, j))
        while queue:
            node = queue.pop()
            if node[0] < len(grid)-1 and grid[node[0]+1][node[1]] == "1":
                self.visited.append((node[0]+1, node[1]))
                queue.append((node[0]+1, node[1]))
            if node[1] < len(grid[0])-1 and grid[node[0]][node[1]+1] == "1":
                self.visited.append((node[0], node[1]+1))
                queue.append((node[0], node[1]+1))

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