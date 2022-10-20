# https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = [points[0][i] for i in range(n)]
        for i in range(1,m):
            left = [dp[0]] + [0 for _ in range(1,n)]
            for j in range(1,n):
                left[j] = max(left[j-1]-1, dp[j])
            right = [0 for _ in range(1,n)] + [dp[-1]]
            for j in range(n-2,-1,-1):
                right[j] = max(right[j+1]-1, dp[j])
            for j in range(n):
                dp[j] = points[i][j] + max(left[j], right[j])
        return max(dp)