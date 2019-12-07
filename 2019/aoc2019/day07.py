from aoc2019 import read_file, Computer
from itertools import permutations


def get_output_from_phase(phase, l):
    last_output = 0
    for i in range(5):
        phase_number = phase[i]
        c = Computer(l, my_input=[phase_number, last_output])
        c.run_to_completion()
        last_output = c.outputs[-1]
    return last_output


def get_loop_output_from_phase(phase, instructions):
    last_output = 0
    computers = []
    for i in range(5):
        phase_number = phase[i]
        c = Computer(instructions, my_input=[phase_number, last_output])
        c.run_until_output()
        computers.append(c)
        last_output = c.outputs[-1]
    while not computers[-1].complete:
        for c in computers:
            c.input.append(last_output)
            c.run_until_output()
            last_output = c.outputs[-1]
    return last_output


def amp_for_file(fname):
    l = read_file(fname)
    instructions = [int(x) for x in l[0].split(',')]

    retval = -1
    best_phase = None
    for phase in permutations(range(5), r=5):
        output = get_output_from_phase(phase, instructions)
        if output > retval:
            best_phase = phase
            retval = output
    print('best_phase: %s' % str(best_phase))
    return retval


def amp_loop_for_file(fname):
    l = read_file(fname)
    instructions = [int(x) for x in l[0].split(',')]

    retval = -1
    best_phase = None
    for phase in permutations(range(5, 10), r=5):
        output = get_loop_output_from_phase(phase, instructions)
        if output > retval:
            best_phase = phase
            retval = output
    print('best_phase: %s' % str(best_phase))
    return retval


def solve1():
    return amp_for_file('day7.in')


def solve2():
    return amp_loop_for_file('day7.in')


if __name__ == "__main__":
    print(solve2())
