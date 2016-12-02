instr = {
        "D": (1,0),
        "R": (0,1),
        "U": (-1, 0),
        "L": (0, -1)
        }

keypad1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]
data = [x.strip() for x in open('day02.in').readlines()]

def bound1(point):
    x, y = point[0], point[1]
    if x < 0:
        x = 0
    if x >= len(keypad1):
        x = len(keypad1) - 1
    if y < 0:
        y = 0
    if y >= len(keypad1):
        y = len(keypad1) - 1
    return (x,y)

def solve1():
    def move(loc, c):
        d = instr[c]
        my_loc = bound1((loc[0] + d[0], loc[1] + d[1]))
        return(my_loc)
    loc = (1,1)
    password = []
    for row in data:
        for c in row:
            loc = move(loc, c)
        password.append(loc)
    return [keypad1[x[0]][x[1]] for x in password]

keypad2 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 2, 3, 4, 0, 0],
        [0, 5, 6, 7, 8, 9, 0],
        [0, 0, 'A', 'B', 'C', 0, 0],
        [0, 0, 0, 'D', 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
]

def solve2():
    def move(loc, c):
        d = instr[c]
        new_loc = (loc[0] + d[0], loc[1] + d[1])
        if keypad2[new_loc[0]][new_loc[1]] == 0:
            return loc
        return new_loc
    loc = (3,1)
    password = []
    for row in data:
        for c in row:
            loc = move(loc, c)
        password.append(loc)
    return [keypad2[x[0]][x[1]] for x in password]

if __name__ == "__main__":
    print(solve1())
    print(solve2())
