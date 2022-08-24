# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        res = [0 for _ in range(n)]
        res[0] = 1
        res[1] = 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[-1]

print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(5))