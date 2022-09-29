# https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dec = 1
        inc = 1
        res = 1
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                dec = inc + 1
                inc = 1
            elif arr[i] > arr[i+1]:
                inc = dec + 1
                dec = 1
            else:
                inc = 1
                dec = 1
            res = max(max(res, inc), dec)
        return res
    
    