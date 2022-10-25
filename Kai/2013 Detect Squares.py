# https://leetcode.com/problems/detect-squares/

from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.map[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        res = 0
        for x2, y2 in self.map.keys():
            if abs(x1-x2) == abs(y1-y2) and x1!=x2 and y1!=y2:
                if (x1,y2) in self.map.keys() and (x2,y1) in self.map.keys():
                    res += self.map[(x1,y2)] * self.map[(x2,y1)] * self.map[(x2,y2)]
        return res


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)