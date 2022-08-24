# https://leetcode.com/problems/house-robber-ii/

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        return max(self.robHelper(nums[:-1]), self.robHelper(nums[1:]))
        
    def robHelper(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # DP
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        res = [0 for x in range(len(nums))]
        res[-1] = nums[-1]
        res[-2] = max(nums[-1], nums[-2])
        for i in range(len(nums)-3, -1, -1):
            res[i] = max(res[i+1], nums[i] + res[i+2])
        return res[0]
    