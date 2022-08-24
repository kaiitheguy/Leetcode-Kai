# https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        check = set()
        for i in nums:
            check.add(i)
        if len(check) == len(nums):
            return False
        else:
            return True
        
        """
        check = {}
        for i in nums:
            check[i]=i;
        if len(check) == len(nums):
            return False
        else:
            return True
        """