# https://leetcode.com/problems/palindromic-substrings/

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            count += 1
            if i <= len(s) - 1:
                count += self.countSubstringsHelper(s, i, i+1)
            if i <= len(s) - 2:
                count += self.countSubstringsHelper(s, i, i+2)
        return count

    def countSubstringsHelper(self, s, l, r):
        count = 0
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                count += 1
                l -= 1
                r += 1  
            else:
                break
        return count

print(Solution().countSubstrings("abc"))
print(Solution().countSubstrings("aaa"))
print(Solution().countSubstrings("cabac"))