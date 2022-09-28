# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        if len(colors) == 1:
            return 0
        
        i = 0
        j = 1
        cost = 0
        
        def findKthSmallestCost(k: int, l: int, r: int) -> int:
            return sum(sorted([t for t in neededTime[i:j]])[:k])
        
        while i < len(colors):
            while j < len(colors) and colors[i] == colors[j]:
                j += 1
            if len(colors[i:j]) >= 2:
                cost += findKthSmallestCost(len(colors[i:j])-1, i, j)
            i = j
            j = i + 1
                
        return cost
            