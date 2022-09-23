# https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        queue = [intervals[0]]
        count = 1
        for interval in intervals[1:]:
            earliest_end = queue[0][1]
            if earliest_end <= interval[0]:
                queue[0][1] = interval[1]
            else:
                count += 1
                queue.append(interval)
            queue.sort(key = lambda x:x[1])
        return count
            