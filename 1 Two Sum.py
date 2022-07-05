# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hist = {}
        for i, n in enumerate(nums):
            if n in hist:
                return [i, hist[n]]
            hist[target - n] = i