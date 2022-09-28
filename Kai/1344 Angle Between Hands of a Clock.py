# https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_min_angle = 6
        one_hour_angle = 30
        
        min_angle = 6 * minutes
        hour_angle = 30 * ((hour % 12) + (minutes / 60.0))
        
        return min(abs(min_angle - hour_angle), 360 - abs(min_angle - hour_angle))