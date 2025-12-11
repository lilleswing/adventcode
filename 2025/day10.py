import re
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

# The main regular expression to parse the three high-level components
# This regex is highly optimized for extracting the three main parts of the line.
MAIN_REGEX = re.compile(r"""
    ^
    \[([.#]+)\]                             # Group 1: The bracketed pattern (e.g., .##.)
    \s*
    ((?:\s*\(\d+(?:,\d+)*\))+?)             # Group 2: The entire intermediate sequence of (X,Y,Z) groups
    \s*
    \{(\d+(?:,\d+)*)\}                      # Group 3: The curly-braced set (e.g., 3,5,4,7)
    $
""", re.VERBOSE) # re.VERBOSE allows multi-line regex with comments
SEQUENCE_REGEX = re.compile(r"\(([^)]+)\)")

def parse(line):
    """
    [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
    [...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
    [.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
    :param s:
    :return:
    """
    match = MAIN_REGEX.match(line)
    if match:
        pattern = match.group(1)
        intermediate_raw = match.group(2).strip()
        final_set_raw = match.group(3)

        # 1. Parse the Final Set (Group 3)
        # Convert the comma-separated string to a list of integers
        final_set = [int(x.strip()) for x in final_set_raw.split(',')]

        # 2. Parse the Intermediate Sequences (Group 2)
        # Use the secondary regex to find all sequences inside parentheses
        sequence_matches = SEQUENCE_REGEX.findall(intermediate_raw)

        intermediate_sequences = []
        for seq_str in sequence_matches:
            # Convert each comma-separated sequence string into a list of integers
            # If the sequence is empty, we skip it (though unlikely with this data)
            if seq_str:
                sequence_list = [int(x.strip()) for x in seq_str.split(',')]
                intermediate_sequences.append(sequence_list)



        # # Print the results for verification
        # print(f"\nOriginal Line: {line}")
        # print(f"  Pattern: {pattern}")
        # print(f"  Sequences: {intermediate_sequences}")
        # print(f"  Final Set: {final_set}")
        return {
            "pattern": pattern,
            "buttons": intermediate_sequences,
            "counts": final_set,
        }
    else:
        print(f"\nCould not parse line: {line}")

from collections import deque

def flip(pattern, button):
    pattern = list(pattern)
    for idx in button:
        if pattern[idx] == '.':
            pattern[idx] = '#'
        else:
            pattern[idx] = '.'
    return tuple(pattern)

def bfs(pattern, buttons):
    pattern = tuple(list(pattern))
    # print(pattern, buttons)
    starting_pattern = tuple(['.']*len(pattern))
    solutions = {starting_pattern: 0}
    expanded = set()
    solutions[starting_pattern] = 0
    q = deque([starting_pattern])
    while len(q) > 0:
        # print(solutions)
        my_pattern = q.popleft()
        if my_pattern == pattern:
            return solutions[my_pattern]
        if my_pattern in expanded:
            continue
        expanded.add(my_pattern)
        for button in buttons:
            new_pattern = flip(my_pattern, button)
            if new_pattern in solutions:
                continue
            solutions[new_pattern] = solutions[my_pattern] + 1
            q.append(new_pattern)
    return -1






def part1():
    lines = open('day10.in').readlines()
    lines = [x.strip() for x in lines]
    data = [parse(x) for x in lines]
    total = 0
    for d in data:
        num_presses = bfs(d['pattern'], d['buttons'])
        print(num_presses)
        total += num_presses
    print(f"{total}: total")


def solve2(buttons, counts):
    num_counts = len(counts)
    num_buttons = len(buttons)

    b = np.array(counts, dtype=np.float64)
    A = np.zeros((num_counts, num_buttons))
    for col, button in enumerate(buttons):
        for row in button:
            A[row][col] = 1

    constraints = LinearConstraint(A, lb=b, ub=b)
    bounds = Bounds(lb=0, ub=np.inf)

    integrality = np.ones(num_buttons)
    c = np.ones(num_buttons)

    res = milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)


    if not res.success:
        raise ValueError("No Solution!")
    solution = np.round(res.x, 2).astype(int)
    if not np.allclose(np.dot(A, solution), b):
        print(np.dot(A, solution), b)
        print(res.x)
        raise ValueError("Solution does not exactly match totals!")

    print(solution)
    return np.sum(solution)


def part2():
    lines = open('day10.in').readlines()
    lines = [x.strip() for x in lines]
    data = [parse(x) for x in lines]
    total = 0
    for d in data:
        num_presses = solve2(d['buttons'], d['counts'])
        print(num_presses)
        total += num_presses
    print(f"Total: {total}")


if __name__ == "__main__":
    # part1()
    part2()