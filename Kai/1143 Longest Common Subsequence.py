# https://leetcode.com/problems/longest-common-subsequence/

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text2)
        n = len(text1)
        grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[j] == text2[i]:
                    grid[i][j] = grid[i+1][j+1] + 1
                else:
                    grid[i][j] = max(grid[i+1][j], grid[i][j+1])
        return grid[0][0]