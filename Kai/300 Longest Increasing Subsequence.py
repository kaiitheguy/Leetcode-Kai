# https://leetcode.com/problems/longest-increasing-subsequence/

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary Search
        sub = []
        for n in nums:
            index = bisect_left(sub, n)
            if index == len(sub):
                sub.append(n)
            else:
                sub[index] = n
        return len(sub)
        
        # DP
        """
        res = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            max_sub = 1
            for j in range(0, i):
                if nums[j] < nums[i] and res[j] >= max_sub:
                    max_sub = res[j] + 1
                res[i] = max_sub
        return max(res)
        """