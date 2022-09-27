# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        
        def backtrack(i, tmp):
            if i >= len(s):
                res.append(tmp[:])
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    tmp.append(s[i:j+1])
                    backtrack(j+1, tmp)
                    tmp.pop()
            
        backtrack(0, [])
        
        return res