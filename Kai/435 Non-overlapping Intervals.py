# https://leetcode.com/problems/non-overlapping-intervals/

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x:x[0])
        lastEnd = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < lastEnd:
                lastEnd = min(lastEnd, interval[1])
                count += 1
            else:
                lastEnd = interval[1]
        return count