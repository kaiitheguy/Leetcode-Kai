# https://leetcode.com/problems/word-search/

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        
        def backtrack(i, j, suffix):
            if board[i][j] != suffix[0]:
                return False
            elif len(suffix) == 1:
                return True
            temp = board[i][j]
            board[i][j] = '#'
            for d in [(-1,0),(1,0),(0,-1),(0,1)]:
                if i+d[0]>=0 and i+d[0]<m and j+d[1]>=0 and j+d[1]<n:
                    if backtrack(i+d[0], j+d[1], suffix[1:]):
                        return True
            board[i][j] = temp
            return False
        
        for i in range(m):
            for j in range(n):
                if backtrack(i, j, word):
                    return True
        return False
    