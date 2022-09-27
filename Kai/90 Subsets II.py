# https://leetcode.com/problems/subsets-ii/

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []
        
        def backtrack(i, tmp):
            if i >= len(nums):
                res.append(tmp[:])
                return
            
            tmp.append(nums[i])
            backtrack(i+1, tmp)
            
            tmp.pop()
            j = i + 1
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            backtrack(j, tmp)
            
        backtrack(0, [])
        
        return res