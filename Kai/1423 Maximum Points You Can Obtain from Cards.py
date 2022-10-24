# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total = sum(cardPoints[:k])
        max_total = total
        for i in range(k-1,-1,-1):
            j = len(cardPoints) - (k-i)
            total -= cardPoints[i]
            total += cardPoints[j]
            max_total = max(max_total, total)
        return max_total