# https://leetcode.com/problems/longest-palindromic-substring/

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s
        max_count = 0
        max_p = ""
        for i in range(len(s)):
            if i <= len(s) - 1:
                res = self.longestPalindromeHelper(s, i, i+1)
                if len(res) > max_count:
                    max_count = len(res)
                    max_p = res
            if i <= len(s) - 2:
                res = self.longestPalindromeHelper(s, i, i+2)
                if len(res) > max_count:
                    max_count = len(res)
                    max_p = res
        return max_p

    def longestPalindromeHelper(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1  
            else:
                break
        return s[l+1:r]

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("cabac"))