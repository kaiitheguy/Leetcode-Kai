# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1: 
            return 0
        left = 0
        right = 1
        res = 0
        while right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                res += prices[right] - prices[left]
                left = right
                right += 1
        return res