# https://leetcode.com/problems/student-attendance-record-ii/

class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        ax = x = xl = 1
        axl = axll = xll = 0
        
        for _ in range(n-1):
            ax, axl, axll, x, xl, xll = (ax + x + xl + axl + axll + xll) % MOD, ax, axl, (x + xl + xll) % MOD, x, xl
            
        return (ax + x + xl + axl + axll + xll) % MOD