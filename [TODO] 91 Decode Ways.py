# https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s)-1, 0, -1):
            if s[i] == '0':
                return self.numDecodings(s[:i-1])
            elif s[i-1] == '0':
                return self.numDecodings(s[:i])
            elif int(s[i-1:i+1]) > 26:
                return self.numDecodings(s[:i])
            else:
                return 1 + self.numDecodings(s[:i])

print(Solution().numDecodings("11106"))
print(Solution().numDecodings("12"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("06"))