# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        buys = [10000 for _ in range(k)]
        sells = [0 for _ in range(k)]
        for i in range(len(prices)):
            for j in range(k):
                buys[j] = min(buys[j], prices[i]) if j==0 else min(buys[j], prices[i] - sells[j-1])
                sells[j] = max(sells[j], prices[i] - buys[j])
        return sells[-1]