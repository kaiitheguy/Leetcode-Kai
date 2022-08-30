# https://leetcode.com/problems/longest-consecutive-sequence/

import collections

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        res = 0
        for n in counter.keys():
            if n-1 in counter.keys():
                continue
            temp = 1
            curr = n
            while curr+1 in counter.keys():
                temp += 1
                curr += 1
            res = max(res, temp)
        return res