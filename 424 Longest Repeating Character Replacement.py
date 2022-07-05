# https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        l = 0
        r = 1
        
        key = set(list(s))
        value = [0 for _ in range(len(key))]
        dic = dict(zip(key, value))
        maxLen = 0
        
        dic[s[0]] += 1
        dic[s[1]] += 1
        while r < len(s):
            if r - l + 1 - max(dic.values()) <= k:
                if r- l + 1 > maxLen:
                    maxLen = r- l + 1
                r += 1
                if r < len(s):
                    dic[s[r]] += 1
            else:
                dic[s[l]] -= 1
                l += 1
                
        return maxLen