# https://leetcode.com/problems/coin-change/

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        res = [0 for _ in range(amount+1)]
        for c in coins:
            res[c] = 1
        for i in range(1, amount+1):
            if res[i] != 0:
                for c in coins:
                    if i+c <= amount:
                        if res[i+c] != 0:
                            res[i+c] = min(res[i+c], res[i]+1)
                        else:
                            res[i+c] = res[i]+1
        if res[-1] == 0:
            return -1
        else:
            return res[-1]

print(Solution().coinChange([1,2,5], 11))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1], 0))
print(Solution().coinChange([3,10], 12))