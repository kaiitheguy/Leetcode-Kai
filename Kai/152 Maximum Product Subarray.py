# https://leetcode.com/problems/maximum-product-subarray/

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxProd = [0 for _ in range(len(nums))]
        minProd = [0 for _ in range(len(nums))]
        maxProd[0] = nums[0]
        minProd[0] = nums[0]
        maxRes = nums[0]
        for i in range(1, len(nums)):
            maxProd[i] = max(nums[i], maxProd[i-1] * nums[i], minProd[i-1] * nums[i])
            minProd[i] = min(nums[i], maxProd[i-1] * nums[i], minProd[i-1] * nums[i])
            maxRes = max(maxRes, maxProd[i])
        return maxRes

print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))