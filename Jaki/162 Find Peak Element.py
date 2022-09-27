# https://leetcode.com/problems/find-peak-element/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while (l < r):
            mid = (l + r) // 2
            print(mid)
            if nums[mid] > nums[mid+1]:
                # Left should have at least one peak
                r = mid
            elif nums[mid] < nums[mid+1]:
                # Right should have at least one peak
                l = mid + 1
        return l