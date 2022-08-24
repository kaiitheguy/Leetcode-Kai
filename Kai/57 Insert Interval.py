# https://leetcode.com/problems/insert-interval/

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        res = []
        for i in range(len(intervals)):
            interval = intervals[i]
            if len(res) > 0:
                lastInterval = res[-1]
                if interval[0] > lastInterval[1]:
                    res.append(interval)
                elif interval[0] <= lastInterval[1] and interval[1] > lastInterval[1]:
                    res[-1][1] = interval[1]
            else:
                res.append(interval)
        return res