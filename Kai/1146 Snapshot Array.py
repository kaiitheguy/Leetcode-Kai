# https://leetcode.com/problems/snapshot-array/

from collections import defaultdict

class SnapshotArray:

    def __init__(self, length: int):
        self.lenght = length
        self.snap_dict = defaultdict(defaultdict)
        self.array_dict = defaultdict(int)
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array_dict[index] = val

    def snap(self) -> int:
        self.snap_dict[self.snap_id] = self.array_dict.copy()
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        return self.snap_dict[snap_id][index]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)