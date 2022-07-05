# https://leetcode.com/problems/coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [10001 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c]+1)
        return dp[-1] if dp[-1] != 10001 else -1

print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1], 0))
print(Solution().coinChange([3,10], 12))