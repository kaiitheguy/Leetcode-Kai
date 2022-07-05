# https://leetcode.com/problems/partition-equal-subset-sum/

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        subSum = totalSum / 2
        dp = [[0 for _ in range(subSum+1)] for _ in range(len(nums)+1)]
        dp[0][0] = 1
        for i in range(1, len(nums)+1):
            for j in range(1, subSum+1):
                if dp[i-1][j] == True or (j >= nums[i-1] and dp[i-1][j-nums[i-1]] == True):
                    dp[i][j] = 1
        return dp[len(nums)][subSum]