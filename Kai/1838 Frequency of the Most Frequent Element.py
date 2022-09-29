# https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        j = 0
        curr_sum = 0
        res = 0
        while j < len(nums):
            curr_sum += nums[j]
            while nums[j] * (j-i+1) - curr_sum > k:
                curr_sum -= nums[i]
                i += 1
            res = max(res, j-i+1)
            j += 1
        return res

            