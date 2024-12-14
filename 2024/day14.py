from collections import defaultdict
import matplotlib.pyplot as plt

import numpy as np
import tqdm


class Robot(object):
    def __init__(self, px, py, vx, vy):
        self.pos = np.array([px, py])
        self.vel = np.array([vx, vy])

    def move_steps(self, steps, mod_x=None, mod_y=None):
        if mod_x is None:
            a = self.pos + self.vel * steps
            return a
        a = self.pos + self.vel * steps
        return a[0] % mod_x, a[1] % mod_y

    def get_quadrant(self, steps, mod_x, mod_y):
        x, y = self.move_steps(steps)
        x = x % mod_x
        y = y % mod_y

        cutoff_x = mod_x // 2
        cutoff_y = mod_y // 2
        if x < cutoff_x and y < cutoff_y:
            return 1
        if x > cutoff_x and y < cutoff_y:
            return 2
        if x < cutoff_x and y > cutoff_y:
            return 3
        if x > cutoff_x and y > cutoff_y:
            return 4
        return -1

    def __str__(self):
        return f'pos: {self.pos}, vel: {self.vel}'


def robot_from_line(line):
    line = line.split(' ')
    px, py = line[0].split('=')[1].split(',')
    vx, vy = line[1].split('=')[1].split(',')
    px, py = int(px), int(py)
    vx, vy = int(vx), int(vy)
    return Robot(px, py, vx, vy)


def part1(fname):
    if fname == 'day14.sample':
        wide = 11
        tall = 7
        steps = 100
    else:
        wide = 101
        tall = 103
        steps = 100
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    robots = [robot_from_line(x) for x in lines]
    # positions = [x.move_steps(100) for x in robots]
    quadrants = [x.get_quadrant(steps, wide, tall) for x in robots]
    d = defaultdict(int)
    for v in quadrants:
        d[v] += 1
    total = 1
    for k, v in d.items():
        if k == -1:
            continue
        total *= v
    print(total)


def get_variance(robots, steps, mod_x, mod_y):
    positions = [x.move_steps(steps, mod_x, mod_y) for x in robots]
    positions = np.array(positions)
    var_x = np.var(positions[:, 0])
    var_y = np.var(positions[:, 1])
    return var_x, var_y


def plot_var(a):
    var_x = [x[0] for x in a]
    plt.scatter(range(len(var_x)), var_x)
    plt.title('Variance of x')
    plt.savefig('var_x.png')
    plt.cla()
    plt.clf()

    var_y = [x[1] for x in a]
    plt.scatter(range(len(var_y)), var_y)
    plt.title('Variance of y')
    plt.savefig('var_y.png')


def part2(fname):
    wide = 101
    tall = 103
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    robots = [robot_from_line(x) for x in lines]

    variances = []
    for i in tqdm.tqdm(range(1, wide * tall)):
        my_var = get_variance(robots, i, wide, tall)
        variances.append((my_var, i))
    # plot_var([x[0] for x in variances])
    variances = sorted(variances, key=lambda x: sum(x[0]))
    print("Variation: ", variances[0][0])
    print("Frame: ", variances[0][1])


if __name__ == "__main__":
    # part1('day14.in')
    part2('day14.in')
