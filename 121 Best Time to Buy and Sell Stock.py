# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = [0 for _ in range(len(prices))]
        min_price = prices[0]
        for i in range(len(prices)):
            p = prices[i]
            if p < min_price:
                min_price = p
            res[i] = p - min_price
        return max(res)

        # Two Pointer
        """
        if len(prices) == 1: 
            return 0
        left = 0
        right = 1
        res = prices[right] - prices[left]
        while right < len(prices):
            if prices[right] - prices[left] > res:
                res = prices[right] - prices[left]
            if prices[left] > prices[right]:
                left = right
                right += 1
            else:
                right += 1
        return res if res > 0 else 0
        """