# https://leetcode.com/problems/number-of-1-bits/

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n:
            """
            n & 1: Performing and operation on unit digit number and 1
            1 & 0 = 0
            1 & 1 = 1
            
            n >> 1: shifting n by 1 bit
            """
            result += (n & 1)
            n = n >> 1
            
        return result