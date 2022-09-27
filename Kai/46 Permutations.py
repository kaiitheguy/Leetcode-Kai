# https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        if len(nums) == 1:
            return [nums]
        elif len(nums) == 2:
            return [nums, nums[::-1]]
        
        for i in range(len(nums)):
            tmp = self.permute(nums[:i] + nums[i+1:])
            for t in tmp:
                t.append(nums[i])
            res.extend(tmp)
            
        return res