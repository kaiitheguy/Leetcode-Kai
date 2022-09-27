# https://leetcode.com/problems/meeting-rooms/

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if intervals == []:
            return True
        intervals.sort(key=lambda x:x[0])
        last_end = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < last_end:
                return False
            if interval[1] > last_end:
                last_end = interval[1]
        return True