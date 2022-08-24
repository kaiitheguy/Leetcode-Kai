# https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        steps = nums[0]
        i = 0
        while steps > 0 and i < len(nums) - 1:
            i += 1
            steps -= 1
            if nums[i] > steps:
                steps = nums[i]
        if i >= len(nums) - 1:
            return True
        else:
            return False