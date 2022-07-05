# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 1:
                    matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])
        return sum([sum(m) for m in matrix])