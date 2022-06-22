# https://leetcode.com/problems/climbing-stairs/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 3:
            return n
        return 2 * self.climbStairs(n-2)

print(Solution().climbStairs(2))
print(Solution().climbStairs(3))
print(Solution().climbStairs(5))