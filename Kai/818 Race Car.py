# https://leetcode.com/problems/race-car/

class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1,0)])
        visited = set((0,1))
        while queue:
            pos, speed, steps = queue.popleft()
            if pos+speed == target:
                return steps+1
            pos_new = pos + speed
            speed_new = speed * 2
            if 0 <= pos_new <= 2 * target and (pos_new, speed_new) not in visited:
                a_next = (pos+speed, speed*2, steps+1)
                queue.append(a_next)
                visited.add((a_next[0], a_next[1]))
            r_next = (pos, 1, steps+1) if speed < 0 else (pos, -1, steps+1)
            if (r_next[0], r_next[1]) not in visited:
                queue.append(r_next)
                visited.add((r_next[0], r_next[1]))