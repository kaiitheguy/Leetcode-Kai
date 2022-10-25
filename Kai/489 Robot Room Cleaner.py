# https://leetcode.com/problems/robot-room-cleaner/

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cleaned = set()
        def dfs(robot, x, y, direction):
            if (x, y) in cleaned:
                return
            robot.clean()
            cleaned.add((x, y))
            for i, (dx, dy) in enumerate(directions[direction:] + directions[:direction]):
                nx = x + dx
                ny = y + dy
                if robot.move():
                    dfs(robot, nx, ny, (direction + i) % 4)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                else:    
                    robot.turnLeft()
        dfs(robot, 0, 0, 0) 