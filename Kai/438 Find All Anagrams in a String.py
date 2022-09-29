# https://leetcode.com/problems/find-all-anagrams-in-a-string/

from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        p_dict = defaultdict(int)
        for c in p:
            p_dict[c] += 1
        i = 0
        j = len(p) - 1
        for c in s[i:j+1]:
            p_dict[c] -= 1
        if all([v == 0 for v in p_dict.values()]):
            res.append(i)
        i += 1
        j += 1
        while j < len(s):
            p_dict[s[i-1]] += 1
            p_dict[s[j]] -= 1
            if all([v == 0 for v in p_dict.values()]):
                res.append(i)
            i += 1
            j += 1
        return res
            