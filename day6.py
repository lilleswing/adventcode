import re

ON = "ON"
OFF = "OFF"
TOGGLE = "TOGGLE"


class Action(object):
    def __init__(self, action, startx, starty, stopx, stopy):
        self.action = action
        self.startx = startx
        self.starty = starty
        self.stopx = stopx
        self.stopy = stopy


def get_action(line):
    if line.startswith("turn off"):
        return OFF
    if line.startswith("turn on"):
        return ON
    if line.startswith("toggle"):
        return TOGGLE
    raise Exception()


def get_values(line):
    m = re.match(".*( \d+,\d+).*( \d+,\d+)", line)
    startx, starty = [int(x) for x in m.group(1).split(',')]
    stopx, stopy = [int(x) for x in m.group(2).split(',')]
    return startx, starty, stopx, stopy


def action_from_string(st):
    action = get_action(st)
    startx, starty, stopx, stopy = get_values(st)
    return Action(action, startx, starty, stopx, stopy)


def parse(lines):
    return [action_from_string(x) for x in lines]


def solve1(actions):
    def get_board():
        my_board = list()
        for i in xrange(1000):
            my_board.append([False] * 1000)
        return my_board

    def take_action(action, light_value):
        if action == TOGGLE:
            return not light_value
        if action == ON:
            return True
        if action == OFF:
            return False
        raise Exception()

    board = get_board()
    for action in actions:
        for x in xrange(action.startx, action.stopx + 1):
            for y in xrange(action.starty, action.stopy + 1):
                board[x][y] = take_action(action.action, board[x][y])

    total = 0
    for x in xrange(len(board)):
        for y in xrange(len(board[0])):
            if board[x][y]:
                total += 1
    return total


def solve2(actions):
    def get_board():
        my_board = list()
        for i in xrange(1000):
            my_board.append([0] * 1000)
        return my_board

    def take_action(action, light_value):
        if action == TOGGLE:
            return light_value + 2
        if action == ON:
            return light_value + 1
        if action == OFF:
            return max(0, light_value - 1)
        raise Exception()

    board = get_board()
    for action in actions:
        for x in xrange(action.startx, action.stopx + 1):
            for y in xrange(action.starty, action.stopy + 1):
                board[x][y] = take_action(action.action, board[x][y])

    total = 0
    for x in xrange(len(board)):
        for y in xrange(len(board[0])):
            total += board[x][y]
    return total


if __name__ == "__main__":
    in_data = [x.strip() for x in open('day6.in').readlines()]
    all_actions = parse(in_data)
    print(solve1(all_actions))
    print(solve2(all_actions))
