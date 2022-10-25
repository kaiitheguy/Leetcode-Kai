# https://leetcode.com/problems/number-of-matching-subsequences/

from collections import defaultdict
from bisect import bisect_left

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = collections.defaultdict(list)
        for i, ch in enumerate(s):
            d[ch].append(i)
            
        ans = 0
        for word in words:
            lastPos = -1
            cnt = 0
            for ch in word:
                if ch not in d:
                    break
                else:
                    j = bisect.bisect_left(d[ch], lastPos+1)
                    if j == len(d[ch]):
                        break
                    lastPos = d[ch][j]
                    cnt += 1  
            if cnt == len(word):  
                ans += 1

        return ans 