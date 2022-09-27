# https://leetcode.com/problems/longest-happy-string/

from collections import Counter

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        
        if a==0 and b==0 and c==0:
            return ""
        
        counter = Counter(a=a, b=b, c=c)
        res = "start"
        
        while True:
            
            (l1, c1), (l2, c2) = counter.most_common(2)
            
            if res[-2] == res[-1] == l1:
                if c2 == 0:
                    break
                res += l2
                counter[l2] -= 1
            else:
                if c1 == 0:
                    break
                res += l1
                counter[l1] -= 1
        
        return res[5:]
            