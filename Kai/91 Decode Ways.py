# https://leetcode.com/problems/decode-ways/

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s[0] == "0":
            return 0
        res = [0 for _ in range(len(s)+1)]
        res[0] = 1
        res[1] = 1
        for i in range(1, len(s)):
            if int(s[i]) != 0:
                res[i+1] = res[i]
            if int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1]) >= 10:
                res[i+1] += res[i-1]
        return res[-1]

print(Solution().numDecodings("11106"))
print(Solution().numDecodings("12"))
print(Solution().numDecodings("226"))
print(Solution().numDecodings("06"))