import networkx as nx


def bounds_check(board, r, c):
    if r < 0 or r >= len(board):
        return False
    if c < 0 or c >= len(board[0]):
        return False
    return True


def get_terminal_nodes(board):
    retval = []
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 9:
                retval.append((r, c))
    return retval


def make_graph1(board):
    g = nx.DiGraph()
    for r in range(len(board)):
        for c in range(len(board[0])):
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = dr + r, dc + c
                if not bounds_check(board, nr, nc):
                    continue
                v_old, v_new = board[r][c], board[nr][nc]
                if v_new - v_old == 1:
                    g.add_edge((r, c), (nr, nc))
    return g


def score1(g, p, end_states):
    pred, dist = nx.bellman_ford_predecessor_and_distance(g, source=p)
    total = 0
    for e in end_states:
        if e in dist:
            total += 1
    return total


def part1(fname):
    lines = open(fname).readlines()
    lines = [list(x.strip()) for x in lines]
    lines = [[int(y) for y in x] for x in lines]
    g = make_graph1(lines)

    end_states = get_terminal_nodes(lines)
    total = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == 0:
                p = (r, c)
                total += score1(g, p, end_states)
    print(total)
    return total


def score2(g, p, end_states):
    total = 0
    for e in end_states:
        paths = list(nx.all_simple_paths(g, p, e))
        total += len(paths)
    return total

# Do a top down DP instead of recalculating simple paths over and over
def dfs_memoize_cache(func):
    memoize = {}
    def wrapper(*args, **kwargs):
        if args[1] in memoize:
            return memoize[args[1]]
        retval = func(*args, **kwargs)
        memoize[args[1]] = retval
        return retval
    return wrapper

@dfs_memoize_cache
def dfs(g, p, end_states):
    if p in end_states:
        return 1
    total = 0
    for n in g[p]:
        total += dfs(g, n, end_states)
    return total

def score2_fast(g, p, end_states):
    return dfs(g, p, end_states)

def part2(fname):
    lines = open(fname).readlines()
    lines = [list(x.strip()) for x in lines]
    lines = [[int(y) for y in x] for x in lines]
    g = make_graph1(lines)

    end_states = get_terminal_nodes(lines)
    total = 0
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == 0:
                p = (r, c)
                total += score2_fast(g, p, end_states)
    print(total)
    return total


if __name__ == "__main__":
    #part1('day10.in')
    part2('day10.in')
