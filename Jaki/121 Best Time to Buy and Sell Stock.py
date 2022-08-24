# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        profit = 0
        for i in prices:
            for j in prices[prices.index(i):len(prices)]:
                if j-i>profit:
                    profit = j-i
        return profit
        """
        """
        profit = 0
        for i in prices:
            val = max(prices[prices.index(i):len(prices)])
            if val>i and val-i>profit:
                profit = val-i
        return profit
        """
        small = 10000
        profit = 0
        for i in prices:
            if i< small:
                small = i
            if i-small>profit:
                profit = i-small
        return profit
        
        