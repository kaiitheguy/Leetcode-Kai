# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        pos, neg, zero, res = [], [], [], set()
        
        for n in nums:
            if n > 0: pos.append(n)
            elif n < 0: neg.append(n)
            else: zero.append(n)
        
        POS = set(pos)
        NEG = set(neg)
        
        if len(zero) >= 1:
            for p in POS:
                if -p in NEG: 
                    res.add((-p, 0, p))
                    
        if len(zero) >= 3: 
            res.add((0, 0, 0))

        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                if -(pos[i] + pos[j]) in NEG:
                    res.add(tuple(sorted([-(pos[i] + pos[j]), pos[i], pos[j]])))
                    
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                if -(neg[i] + neg[j]) in POS:
                    res.add(tuple(sorted([-(neg[i] + neg[j]), neg[i], neg[j]])))
                    
        return res