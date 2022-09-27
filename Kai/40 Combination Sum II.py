# https://leetcode.com/problems/combination-sum-ii/

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        candidates.sort()
        
        def backtrack(i, tmp, target):
            if i >= len(candidates):
                return 
            if candidates[i] == target:
                tmp.append(candidates[i])
                res.append(tmp[:])
                tmp.pop()
                return
            elif candidates[i] > target:
                return
            else:
                tmp.append(candidates[i])
                backtrack(i+1, tmp, target-candidates[i])
                tmp.pop()
                j = i+1
                while j < len(candidates) and candidates[j] == candidates[i]:
                    j += 1
                backtrack(j, tmp, target)
        
        backtrack(0, [], target)
        
        return res