# https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        dp = [arr[0] for _ in range(len(arr))]
        dp_dl = [arr[0] for _ in range(len(arr))]
        max_sum = arr[0]
        for i in range(1, len(arr)):
            dp[i] = max(dp[i-1] + arr[i], arr[i])
            dp_dl[i] = max(dp_dl[i-1] + arr[i], dp[i-1])
            max_sum = max(max_sum, dp[i], dp_dl[i])
        return max_sum