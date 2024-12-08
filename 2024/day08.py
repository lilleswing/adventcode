from collections import defaultdict


def bounds_check(board, r, c):
    if r < 0 or r >= len(board):
        return False
    if c < 0 or c >= len(board[0]):
        return False
    return True


def get_antennas1(board):
    antennas = defaultdict(list)
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == '.':
                continue
            my_char = board[r][c]
            antennas[my_char].append((r, c))
    return antennas


def get_antinodes1(board, antenna):
    antinodes = set()
    for v1 in antenna:
        for v2 in antenna:
            if v1 == v2:
                continue
            dr = v2[0] - v1[0]
            dc = v2[1] - v1[1]
            nr = v2[0] + dr
            nc = v2[1] + dc
            if not bounds_check(board, nr, nc):
                continue
            antinodes.add((nr, nc))
    return antinodes


def reduce_fraction(a, b):
    """Reduces a fraction to its lowest terms.

    Args:
      a: The numerator of the fraction.
      b: The denominator of the fraction.

    Returns:
      A tuple (new_numerator, new_denominator) representing the reduced fraction.
    """

    def gcd(a, b):
        """Calculates the greatest common divisor of two numbers."""
        while b:
            a, b = b, a % b
        return a

    gcd_value = gcd(abs(a), abs(b))
    return a // gcd_value, b // gcd_value


def get_antinodes2(board, antenna):
    antinodes = set(antenna)
    for v1 in antenna:
        for v2 in antenna:
            if v1 == v2:
                continue
            dr = v2[0] - v1[0]
            dc = v2[1] - v1[1]
            dr, dc = reduce_fraction(dr, dc)
            nr = v1[0] + dr
            nc = v1[1] + dc
            while bounds_check(board, nr, nc):
                antinodes.add((nr, nc))
                nr += dr
                nc += dc
    return antinodes


def part1(fname):
    lines = open(fname).readlines()
    board = [list(x.strip()) for x in lines]
    antennas = get_antennas1(board)
    all_antinodes = set()
    for k, v in antennas.items():
        antinodes = get_antinodes1(board, v)
        all_antinodes.update(antinodes)
    print(len(all_antinodes))


def part2(fname):
    lines = open(fname).readlines()
    board = [list(x.strip()) for x in lines]
    antennas = get_antennas1(board)
    all_antinodes = set()
    for k, v in antennas.items():
        antinodes = get_antinodes2(board, v)
        all_antinodes.update(antinodes)
    print(len(all_antinodes))


if __name__ == "__main__":
    # part1('day08.in')
    part2('day08.in')
