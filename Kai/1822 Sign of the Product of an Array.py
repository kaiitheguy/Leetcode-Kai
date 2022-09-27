# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_count = 0
        for n in nums:
            if n == 0:
                return 0
            elif n < 0:
                neg_count += 1
        if neg_count % 2 == 0:
            return 1
        else:
            return -1