# https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """if len(nums) == 1:
            return [[], nums]
        else:
            prev_res = self.subsets(nums[1:])
            new_res = copy.deepcopy(prev_res)
            for r in new_res:
                r.append(nums[0])
            return prev_res + new_res"""
        res = []
        
        def backtrack(i, tmp):
            if i >= len(nums):
                res.append(tmp[:])
                return
            
            tmp.append(nums[i])
            backtrack(i+1, tmp)
            
            tmp.pop()
            backtrack(i+1, tmp)
            
        backtrack(0, [])
        return res
            