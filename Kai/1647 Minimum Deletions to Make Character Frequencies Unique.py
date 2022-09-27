#https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

from collections import Counter

class Solution:
    def minDeletions(self, s: str) -> int:
        res = 0
        count_dict = Counter(s)
        count_list = sorted(count_dict.items(), key=lambda x:x[1], reverse = True)
        count_next_unique = count_list[0][1]
        for _, count in count_list:
            count_next_unique = min(count_next_unique, count)
            res += count - count_next_unique
            if count_next_unique > 0:
                count_next_unique -= 1
        return res
            
            