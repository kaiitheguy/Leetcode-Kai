# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = 10000
        buy2 = 10000
        sell1 = 0
        sell2 = 0
        for i in range(len(prices)):
            buy1 = min(buy1, prices[i]) 
            buy2 = min(buy2, prices[i] - sell1)
            sell1 = max(sell1, prices[i] - buy1)
            sell2 = max(sell2, prices[i] - buy2)
        return sell2