class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seat_dict = {}
        for row, col in reservedSeats:
            if row not in seat_dict.keys():
                seat_dict[row] = [1, 1, 1]
            if col in [2, 3]:
                seat_dict[row][0] = 0
            elif col in [4, 5]:
                seat_dict[row][0] = 0
                seat_dict[row][1] = 0
            elif col in [6, 7]:
                seat_dict[row][1] = 0
                seat_dict[row][2] = 0
            elif col in [8, 9]:
                seat_dict[row][2] = 0
        count = 0
        for row in seat_dict.keys():
            count += max(seat_dict[row][1], seat_dict[row][0]+seat_dict[row][2])
        return count + (n - len(seat_dict.keys())) * 2