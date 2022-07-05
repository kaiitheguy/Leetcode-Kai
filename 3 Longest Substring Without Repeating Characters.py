# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        l = 0
        r = 1
        
        key = set(list(s))
        value = [-1 for _ in range(len(key))]
        dic = dict(zip(key, value))
        
        res = 0
        dic[s[0]] = 0
        
        while r < len(s):
            curr = s[r]
            if dic[curr] != -1 and dic[curr] >= l:
                l = dic[curr] + 1
            dic[curr] = r
            res = max(res, r-l+1)
            r += 1
            
        return res