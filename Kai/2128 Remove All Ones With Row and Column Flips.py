# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/

class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        for i in range(len(grid)):
            if grid[i] != grid[0] and grid[i] != [0 if n==1 else 1 for n in grid[0]]:
                return False
        return True
                