EAST = 1
SOUTH = 2
WEST = 3
NORTH = 4

class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def run(self, cmd):
        if cmd == 'G':
            self.go()
        elif cmd == 'L':
            self.turn_left()
        else:
            self.turn_right()

    def go(self):
        if self.direction == EAST:
            self.x += 1
        elif self.direction == WEST:
            self.x -= 1
        elif self.direction == NORTH:
            self.y += 1
        else:
            self.y -= 1

    def turn_left(self):
        if self.direction == EAST:
            self.direction = NORTH
        else:
            self.direction -= 1

    def turn_right(self):
        if self.direction == NORTH:
            self.direction = EAST
        else:
            self.direction += 1

class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        robot = Robot(0, 0, NORTH)
        for cmd in instructions:
            robot.run(cmd)

        return robot.direction != NORTH or (robot.x == 0 and robot.y == 0)
