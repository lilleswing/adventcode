import networkx as nx

directions = {
    'N': (-1, 0),
    'S': (1, 0),
    'E': (0, 1),
    'W': (0, -1)
}

turns = {
    'N': ['W', 'E'],
    'S': ['E', 'W'],
    'E': ['N', 'S'],
    'W': ['S', 'N']
}

def bounds_check(board, r, c):
    return r >= 0 and r < len(board) and c >= 0 and c < len(board[0])

def parse(fname):
    lines = [x.strip() for x in open(fname).readlines()]

    # node space is (r, c, direction, straight_moves)
    # if straight_moves == 3 don't allow it to be -4
    g = nx.DiGraph()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            for straight_move in range(4):
                for dir_name, (dr, dc) in directions.items():
                    for turn_name in turns[dir_name]:
                        tdr, tdc = directions[turn_name]
                        nr, nc = r + tdr, c + tdc
                        if not bounds_check(lines, nr, nc):
                            continue
                        heat_loss = int(lines[nr][nc])
                        g.add_edge((r, c, dir_name, straight_move), (nr, nc, turn_name, 1), weight=heat_loss, move_type='turn')
                    if straight_move == 3:
                        continue
                    nr, nc = r + dr, c + dc
                    if not bounds_check(lines, nr, nc):
                        continue
                    heat_loss = int(lines[nr][nc])
                    g.add_edge((r, c, dir_name, straight_move), (nr, nc, dir_name, straight_move + 1),
                               weight=heat_loss, move_type='straight')
    # tie together all the startin
    source = (0, 0, 'E', 0)
    sink = (len(lines) - 1, len(lines[0]) - 1, '*', 0)
    for dir_name in directions:
        for straight_move in range(4):
            hash_sink = (len(lines) - 1, len(lines[0]) - 1, dir_name, straight_move)
            g.add_edge(hash_sink, sink, weight=0)
    return g, source, sink

def parse2(fname):
    lines = [x.strip() for x in open(fname).readlines()]

    # node space is (r, c, direction, straight_moves)
    # if straight_moves == 3 don't allow it to be -4
    g = nx.DiGraph()
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            for straight_move in range(11):
                for dir_name, (dr, dc) in directions.items():
                    for turn_name in turns[dir_name]:
                        if straight_move < 4:
                            continue
                        tdr, tdc = directions[turn_name]
                        nr, nc = r + tdr, c + tdc
                        if not bounds_check(lines, nr, nc):
                            continue
                        heat_loss = int(lines[nr][nc])
                        g.add_edge((r, c, dir_name, straight_move), (nr, nc, turn_name, 1), weight=heat_loss, move_type='turn')
                    if straight_move == 10:
                        continue
                    nr, nc = r + dr, c + dc
                    if not bounds_check(lines, nr, nc):
                        continue
                    heat_loss = int(lines[nr][nc])
                    g.add_edge((r, c, dir_name, straight_move), (nr, nc, dir_name, straight_move + 1),
                               weight=heat_loss, move_type='straight')
    # tie together all the startin
    source = (0, 0, 'E', 0)
    sink = (len(lines) - 1, len(lines[0]) - 1, '*', 0)
    for dir_name in directions:
        for straight_move in range(11):
            hash_sink = (len(lines) - 1, len(lines[0]) - 1, dir_name, straight_move)
            g.add_edge(hash_sink, sink, weight=0)
    return g, source, sink


def get_weighted_path_len(g, path):
    total = 0
    for i in range(len(path) - 1):
        total += g[path[i]][path[i + 1]]['weight']
        # print(g[path[i]][path[i + 1]])
    return total

def part1(fname):
    g, source, sink = parse(fname)
    path = nx.shortest_path(g, source, sink, weight='weight')
    print(path)
    print(get_weighted_path_len(g, path))

def print_board(path, fname):
    lines = [x.strip() for x in open(fname).readlines()]
    lines = [list(x) for x in lines]
    char_lookup = {
        'N': '^',
        'S': 'v',
        'E': '>',
        'W': '<',
        '*': 'X'
    }
    for point in path:
        lines[point[0]][point[1]] = char_lookup[point[2]]
    l = []
    for row in lines:
        l.append(''.join(row))
    print("\n".join(l))


def part2(fname):
    g, source, sink = parse2(fname)
    new_node = (0,0,'*', 0)
    g.add_edge(new_node, source, weight=0)
    g.add_edge(new_node, (0,0,'S', 0), weight=0)
    path = nx.shortest_path(g, new_node, sink, weight='weight')
    print(path)
    print_board(path, fname)
    print(get_weighted_path_len(g, path))


if __name__ == "__main__":
    # part1('day17.in')
    part2('day17.in')
