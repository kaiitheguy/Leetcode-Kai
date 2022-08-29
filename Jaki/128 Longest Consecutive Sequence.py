# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        longest = 0
        
        for i in nums_set:
            if i-1 not in nums_set:
                current = i
                currentlength = 1
                
                while current+1 in nums_set:
                    current +=1
                    currentlength +=1
                    
                longest = max(longest,currentlength)
                
        return longest
                
            