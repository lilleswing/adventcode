from aoc2019 import read_file

class Point(object):
    def __init__(self, x, y, grid=None):
        if grid is None:
            self.grid = {}
        else:
            self.grid = grid
        self.x = x
        self.y = y
        self.step_count = 0
    
    def to_key(self):
        return (self.x, self.y)
    
    def update_grid(self):
        key = self.to_key()
        if key not in self.grid:
            self.grid[key] = self.step_count
            
    def move(self, s):
        move_dict = {
            'R': (0,1),
            'L': (0,-1),
            'U': (-1, 0),
            'D': (1, 0)
        }
        my_dir = move_dict[s[0]]
        s = int(s[1:])

        for i in range(s):
            self.step_count += 1
            self.x += my_dir[1]
            self.y += my_dir[0]
            self.update_grid()
        return
        
def solve1(l):
    p1 = Point(0, 0)
    for elem in l[0]:
        p1.move(elem)
    p2 = Point(0,0)
    for elem in l[1]:
        p2.move(elem)
    g1, g2 = set(p1.grid.keys()), set(p2.grid.keys())
    intersections = list(g1.intersection(g2))
    intersections = sorted(intersections, key=lambda x: abs(x[0]) + abs(x[1]))
    return intersections[0], abs(intersections[0][0]) + abs(intersections[0][1])


def total_steps(point, g1, g2):
    return g1[point] + g2[point]

def solve2(l):
    p1 = Point(0, 0)
    for elem in l[0]:
        p1.move(elem)
    p2 = Point(0,0)
    for elem in l[1]:
        p2.move(elem)
    g1, g2 = p1.grid, p2.grid
    k1, k2 = set(p1.grid.keys()), set(p2.grid.keys())
    intersections = list(k1.intersection(k2))
    intersections = sorted(intersections, key=lambda x: total_steps(x, g1, g2))
    return intersections[0], total_steps(intersections[0], g1, g2)



def test_solve_1():
    l = read_file('day3.in')
    l = [x.split(',') for x in l]
    _, retval = solve1(l)
    assert retval == 403
    
    
def test_solve_2():
    l = read_file('day3.in')
    l = [x.split(',') for x in l]
    _, retval = solve2(l)
    assert retval == 4158
