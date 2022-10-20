# https://leetcode.com/problems/maximum-number-of-visible-points/

import math

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        extra = 0
        angles = []
        for point in points:
            if point[0] == location[0] and point[1] == location[1]:
                extra += 1
            else:
                angles.append((math.degrees(math.atan2(location[1]-point[1], location[0]-point[0]))+360)%360)
        angles.sort()
        for i in range(len(angles)):
            angles.append(angles[i]+360)
        count = 0
        i = 0
        j = 0
        while j <= len(angles) - 1:
            if angles[j] - angles[i] <= angle:
                count = max(count, j - i + 1)
                j += 1
            else:
                i += 1
        return count + extra