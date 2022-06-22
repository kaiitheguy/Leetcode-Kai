# https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = [0 for _ in range(len(nums))]
        res[0] = nums[0]
        max_prod = nums[0]
        for i in range(1, len(nums)):
            if res[i-1] > 0:
                res[i] = nums[i] * res[i-1]
            else:
                res[i] = nums[i]
            if res[i] > max_prod:
                max_prod = res[i]
        return max_prod

print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))