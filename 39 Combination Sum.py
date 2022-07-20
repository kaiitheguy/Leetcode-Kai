# https://leetcode.com/problems/combination-sum/

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(new_target, temp_res, start):
            if new_target == 0:
                res.append(list(temp_res))
                return
            elif new_target < 0:
                return
            else:
                for i in range(start, len(candidates)):
                    curr = candidates[i]
                    temp_res.append(curr)
                    backtrack(new_target - curr, temp_res, i)
                    temp_res.pop()

        backtrack(target, [], 0)

        return res
        
        """
        res = []
        for i in range(len(candidates)):
            if candidates[i] == target:
                res.append([candidates[i]])
            elif candidates[i] > target:
                continue
            else:
                new_target = target - candidates[i]
                sub_res = self.combinationSum(candidates, new_target)
                for r in sub_res:
                    r.append(candidates[i])
                    r = sorted(r)
                    if r not in res:
                        res.append(r)
        return res
        """