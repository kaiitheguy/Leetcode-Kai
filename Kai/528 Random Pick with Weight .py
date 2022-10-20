# https://leetcode.com/problems/random-pick-with-weight/

import bisect

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.w = w
        self.sum = 0
        self.prefix_sum = []
        for i in w:
            self.sum += i
            self.prefix_sum.append(self.sum)

    def pickIndex(self):
        """
        :rtype: int
        """
        rand_sum = self.sum * random.random()
        return bisect.bisect(self.prefix_sum, rand_sum)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()