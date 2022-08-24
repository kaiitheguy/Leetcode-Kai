# https://leetcode.com/problems/minimum-window-substring/

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) > len(s):
            return ""
        
        counter = collections.Counter(t)
        l = 0
        r = 0
        minLen = len(s)
        minRes = ""
        tLen = len(t)
        
        if s[0] in counter:
            counter[s[0]] -= 1
            tLen -= 1
                
        while r < len(s):
            if tLen == 0:
                if r - l + 1 <= minLen:
                    minLen = r - l + 1
                    minRes = s[l:r+1]
                if s[l] in counter:
                    counter[s[l]] += 1
                    if counter[s[l]] > 0:
                        tLen += 1
                l += 1
            else:
                r += 1
                if r < len(s) and s[r] in counter:
                    counter[s[r]] -= 1
                    if counter[s[r]] >= 0:
                        tLen -= 1
                    
        return minRes