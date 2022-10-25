# https://leetcode.com/problems/max-value-of-equation/

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        queue = collections.deque()
        res = -float('inf')
        for x, y in points:
            # queue[0][1] < x - k means x_j - x_i > k, we get rid of these
            while queue and queue[0][1] < x - k:
                # same as pop(0)
                queue.popleft()
            # what left is x_j - x_i <= k
            if queue: 
                # queue[0][0] + y + x means y_i - x_i + y_j + x_j
                res = max(res, queue[0][0] + y + x)
            # montonic stack 
            # remove smaller items before append to reserve the order
            while queue and queue[-1][0] <= y - x:
                queue.pop()
            queue.append([y - x, x])
        return res