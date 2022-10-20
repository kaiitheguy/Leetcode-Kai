# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        a = nums[-4] - nums[0]
        b = nums[-3] - nums[1]
        c = nums[-2] - nums[2]
        d = nums[-1] - nums[3]
        return min(a,b,c,d)