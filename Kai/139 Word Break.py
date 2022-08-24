# https://leetcode.com/problems/word-break/

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        res = [0 for _ in range(len(s)+1)]
        res[0] = 1
        for i in range(len(s)+1):
            for j in range(i):
                if s[j:i] in wordDict and res[j] == 1:
                    res[i] = 1
        print(res)
        return bool(res[-1])