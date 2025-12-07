from functools import lru_cache


@lru_cache(maxsize=None)
def num_solutions(lines, r, c):
    if r == len(lines):
        return 1
    if lines[r][c] == '^':
        return num_solutions(lines, r + 1, c - 1) + num_solutions(lines, r + 1, c + 1)
    else:
        return num_solutions(lines, r + 1, c)


def part2():
    lines = open('day07.in').readlines()
    lines = [x.strip() for x in lines]
    beams = [lines[0].find('S')]
    lines = tuple([tuple(x) for x in lines])
    print(num_solutions(lines, 0, beams[0]))


def part1():
    lines = open('day07.in').readlines()
    lines = [x.strip() for x in lines]
    beams = [lines[0].find('S')]
    splits = 0
    for row in range(1, len(lines)):
        new_beams = set()
        for beam in beams:
            if lines[row][beam] == '^':
                splits += 1
                new_beams.add(beam - 1)
                new_beams.add(beam + 1)
            else:
                new_beams.add(beam)
        beams = new_beams
    print(splits)


if __name__ == "__main__":
    #part1()
    part2()
