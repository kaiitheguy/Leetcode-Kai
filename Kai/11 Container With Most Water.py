# https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = min(height[left], height[right]) * (right - left)
        
        while left < right:
            if height[left] < height[right]:
                if height[left] * (right - left) > maxArea:
                    maxArea = height[left] * (right - left)
                left += 1
            else:
                if height[right] * (right - left) > maxArea:
                    maxArea = height[right] * (right - left)
                right -= 1
        
        return maxArea