# https://leetcode.com/problems/merge-intervals/

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x:x[0])
        res = []
        for i in intervals:
            if len(res) == 0:
                res.append(i)
            else:
                lastI = res[-1]
                if i[0] > lastI[1]:
                    res.append(i)
                elif i[1] > lastI[1]:
                    res[-1][1] = i[1]
        return res