# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return 0
        queue = [(0,0,k,0)]
        visited = set((0,0,k))
        if k > (m-1 + n-1):
            return m-1 + n-1
        while queue:
            i, j, k_curr, step = queue.pop(0)
            for direction in [(-1,0),(0,1),(1,0),(0,-1)]:
                i_new = i + direction[0]
                j_new = j + direction[1]
                if (i_new>=0 and i_new<=m-1 and j_new>=0 and j_new<=n-1):
                    if grid[i_new][j_new] == 1 and (k_curr > 0) and (i_new,j_new,k_curr-1) not in visited:
                        queue.append((i_new,j_new,k_curr-1,step+1))
                        visited.add((i_new,j_new,k_curr-1))
                    if grid[i_new][j_new] == 0 and (i_new,j_new,k_curr) not in visited:
                        if i_new == m-1 and j_new == n-1:
                            return step+1
                        queue.append((i_new,j_new,k_curr,step+1))
                        visited.add((i_new,j_new,k_curr))
        return -1
        """
        m = len(grid)
        n = len(grid[0])
        if m == 1 and n == 1:
            return 0
        queue = [[0,0,k,0]]
        visited =[[[k+1,m*n] for _ in range(n)] for _ in range(m)]
        visited[0][0] = [k,0]
        while queue:
            i, j, k_curr, step = queue.pop()
            for direction in [(0,1),(1,0),(0,-1),(-1,0)]:
                i_new = i + direction[0]
                j_new = j + direction[1]
                if (i_new>=0 and i_new<=m-1 and j_new>=0 and j_new<=n-1):
                    if grid[i_new][j_new] == 1:
                        if (k_curr > 0):
                            if k_curr-1!=visited[i_new][j_new][0] and visited[i_new][j_new][1]>step+1:
                                queue.append([i_new,j_new,k_curr-1,step+1])
                                visited[i_new][j_new] = [k_curr-1,step+1] 
                    else:
                        if k_curr!=visited[i_new][j_new][0] and visited[i_new][j_new][1]>step+1:
                            queue.append([i_new,j_new,k_curr,step+1])
                            visited[i_new][j_new] = [k_curr,step+1] 
        if visited[m-1][n-1][1] < m*n:
            return visited[m-1][n-1][1] 
        else:
            return -1
        """
        """
        m = len(grid)
        n = len(grid[0])
        
        def bfs(grid, visited, i, j, k):
            if i==m-1 and j==n-1:
                return 0
            visited.append((i,j))
            min_steps = m*n+1
            for direction in [(0,1),(1,0),(0,-1),(-1,0)]:
                i_new = i + direction[0]
                j_new = j + direction[1]
                if (i_new, j_new) not in visited and i_new>=0 and i_new<=m-1 and j_new>=0 and j_new<=n-1:
                    if grid[i_new][j_new] != 1:
                        temp_steps = bfs(grid, visited.copy(), i_new, j_new, k)
                    else:
                        if k > 0:
                            temp_steps = bfs(grid, visited.copy(), i_new, j_new, k-1)
                        else:
                            temp_steps = -1
                    if temp_steps != -1:
                        min_steps = min(min_steps, temp_steps)
            if min_steps != m*n+1:
                return min_steps + 1
            else:
                return -1
    
        return bfs(grid, [], 0, 0, k)
        """