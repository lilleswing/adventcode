import traceback
import collections
from networkx.exception import NetworkXNoPath
import networkx as nx
from networkx.algorithms.shortest_paths.generic import shortest_path, all_shortest_paths


def read_file(fname):
    with open(fname) as fin:
        return [x.strip() for x in fin.readlines()]


class Elf(object):
    def __init__(self, r, c, attack=3):
        self.team = 'elf'
        self.character = 'E'
        self.hp = 200
        self.attack = attack
        self.r = r
        self.c = c


class Goblin(object):
    def __init__(self, r, c):
        self.team = 'goblin'
        self.character = 'G'
        self.hp = 200
        self.attack = 3
        self.r = r
        self.c = c


def get_adj_squares(board, r, c):
    retval = []
    for dr, dc in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
        nr, nc = r + dr, c + dc
        if nr < 0 or c < 0:
            continue
        if nr > len(board) or nc > len(board[0]):
            continue
        retval.append((nr, nc))
    return retval


def manhattan_distance(p1, p2):
    """
    Gives a lower bound for the path length from p1 to p2
    """
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    return dx + dy


def make_graph(board, combatant):
    g = nx.Graph()
    for r, row in enumerate(board):
        for c, pixel in enumerate(row):
            if pixel != '.':
                continue
            adj_squares = get_adj_squares(board, r, c)
            for r2, c2 in adj_squares:
                pixel2 = board[r2][c2]
                if pixel2 == '.':
                    g.add_edge((r, c), (r2, c2))
    adj_squares = get_adj_squares(board, combatant.r, combatant.c)
    for r2, c2 in adj_squares:
        pixel2 = board[r2][c2]
        if pixel2 == '.':
            g.add_edge((combatant.r, combatant.c), (r2, c2))
    return g


class Battle(object):
    def __init__(self, board, elf_attack=3):
        self.board = [list(x) for x in board]
        self.combatants = self._make_combatants(elf_attack)
        self.finished = False
        self.round = 0
        self.finishing_round = -1

    def _make_combatants(self, elf_attack):
        combatants = []
        for r, row in enumerate(self.board):
            for c, pixel in enumerate(row):
                if pixel == 'G':
                    g = Goblin(r, c)
                    combatants.append(g)
                if pixel == 'E':
                    e = Elf(r, c, elf_attack)
                    combatants.append(e)
        return combatants

    def _get_enemies(self, team):
        return [x for x in self.combatants if x.team != team]

    def _pick_move3(self, combatant, target_squares):
        """
        BFS
        """
        target_squares = set(target_squares)
        my_loc = (combatant.r, combatant.c)
        starting_squares = get_adj_squares(self.board, my_loc[0], my_loc[1])
        starting_squares = [(r, c) for r, c in starting_squares if self.board[r][c] == '.']
        seen = set()
        q = collections.deque()
        for elem in starting_squares:
            q.append([elem, elem, 0])
            seen.add(elem)
        max_depth = 100000000
        answers = set()
        while len(q) > 0:
            next_move, expand_node, depth = q.popleft()
            if depth > max_depth:
                break
            if expand_node in target_squares:
                answers.add((next_move, expand_node))
                max_depth = depth
                continue
            to_enqueue = get_adj_squares(self.board, expand_node[0], expand_node[1])
            to_enqueue = [(r, c) for r, c in to_enqueue if self.board[r][c] == '.']
            for elem in to_enqueue:
                if elem in seen:
                    continue
                q.append([next_move, elem, depth + 1])
                seen.add(elem)
        if len(answers) == 0:
            return None
        # Sort by reading order of landing location
        answers = sorted(answers, key=lambda x: x[1])
        return answers[0][0]

    def _pick_move2(self, combatant, target_squares):
        """
        BFS
        """
        target_squares = set(target_squares)
        my_loc = (combatant.r, combatant.c)
        starting_squares = get_adj_squares(self.board, my_loc[0], my_loc[1])
        starting_squares = [(r, c) for r, c in starting_squares if self.board[r][c] == '.']
        seen = set()
        q = collections.deque()
        for elem in starting_squares:
            q.append([elem, elem])
            seen.add(elem)
        while len(q) > 0:
            next_move, expand_node = q.popleft()
            if expand_node in target_squares:
                return next_move
            to_enqueue = get_adj_squares(self.board, expand_node[0], expand_node[1])
            to_enqueue = [(r, c) for r, c in to_enqueue if self.board[r][c] == '.']
            for elem in to_enqueue:
                if elem in seen:
                    continue
                q.append([next_move, elem])
                seen.add(elem)
        return None

    def _pick_move(self, combatant, target_squares):
        g = make_graph(self.board, combatant)
        my_loc = (combatant.r, combatant.c)
        target_squares = sorted(target_squares, key=lambda x: manhattan_distance(my_loc, x))
        best_path_length = 100000000000000
        move = None
        for target_square in target_squares:
            try:
                if manhattan_distance(my_loc, target_square) > best_path_length:
                    continue
                shortest_paths = list(all_shortest_paths(g, my_loc, target_square))
                shortest_path_length = len(shortest_paths[0])
                if shortest_path_length > best_path_length:
                    continue
                best_path_length = shortest_path_length
                possible_next_steps = [x[1] for x in shortest_paths]
                move = sorted(possible_next_steps)[0]
            except NetworkXNoPath as e:
                pass
            except Exception as e:
                traceback.print_exc()
                raise ValueError()
        return move

    def _move(self, combatant, enemies):
        """
        mutate self coordinants and board state
        """
        adj_enemies = self._get_adj_enemies(combatant, enemies)
        if len(adj_enemies) > 0:
            return
        target_squares = self._get_target_squares(enemies)
        if len(target_squares) == 0:
            return
        new_square = self._pick_move3(combatant, target_squares)
        if new_square is None:
            return
        self._update_board_state(combatant, new_square)

    def _update_board_state(self, combatant, new_square):
        old_square = (combatant.r, combatant.c)
        self.board[old_square[0]][old_square[1]] = '.'
        self.board[new_square[0]][new_square[1]] = combatant.character
        combatant.r = new_square[0]
        combatant.c = new_square[1]

    def _attack(self, combatant, enemies):
        adj_enemies = self._get_adj_enemies(combatant, enemies)
        if len(adj_enemies) == 0:
            return
        adj_enemies = sorted(adj_enemies, key=lambda x: x.hp)
        to_attack = adj_enemies[0]
        to_attack.hp -= combatant.attack
        self._remove_dead_combatants()

    def _get_adj_enemies(self, combatant, enemies):
        adj_squares = get_adj_squares(self.board, combatant.r, combatant.c)
        retval = []
        for enemy in enemies:
            enemy_loc = (enemy.r, enemy.c)
            if enemy_loc in adj_squares:
                retval.append(enemy)
        return retval

    def _act(self, combatant):
        enemies = self._get_enemies(combatant.team)
        if len(enemies) == 0:
            self.finished = True
            return
        self._move(combatant, enemies)
        self._attack(combatant, enemies)

    def fight_round(self):
        self.combatants = sorted(self.combatants, key=lambda x: (x.r, x.c))
        for index, combatant in enumerate(self.combatants):
            if combatant.hp <= 0:
                continue
            if self.finished:
                self.finishing_round = self.round
                return
            self._act(combatant)
        if self.finished:
            self.finishing_round = self.round
        self.round += 1

    def fight_to_completion(self):
        while not self.finished:
            self.fight_round()

    def _get_target_squares(self, enemies):
        retval = set()
        for enemy in enemies:
            adj_squares = get_adj_squares(self.board, enemy.r, enemy.c)
            for adj_square in adj_squares:
                pixel = self.board[adj_square[0]][adj_square[1]]
                if pixel == '.':
                    retval.add(adj_square)
        return list(retval)

    def _remove_dead_combatants(self):
        for combatant in self.combatants:
            if combatant.hp > 0:
                continue
            r, c = combatant.r, combatant.c
            self.board[r][c] = '.'
        self.combatants = [x for x in self.combatants if x.hp > 0]

    def outcome(self):
        if not self.finished:
            raise ValueError("Only can get outcome after a battle is finished")
        total_hp = sum([x.hp for x in self.combatants])
        return self.finishing_round * total_hp

    def print_board(self):
        for row in self.board:
            print("".join(row))
        print()

    def count_elfs(self):
        return sum([1 for x in self.combatants if x.team == 'elf'])


def run_file(fname):
    board = read_file(fname)
    battle = Battle(board)
    battle.fight_to_completion()
    battle.print_board()
    for combatant in battle.combatants:
        print("HP:%s" % combatant.hp)
    print("Finished on Round: %s" % battle.finishing_round)
    return battle.outcome()


def solve1():
    return run_file('day15.in')


def test_1():
    assert run_file('day15.sample') == 27730


def test_2():
    assert 36334 == run_file('day15.sample2')


def test_3():
    assert 39514 == run_file("day15.sample3")


def test_4():
    assert 28944 == run_file('day15.sample4')


def test_5():
    assert 18740 == run_file('day15.sample5')


def do_elves_die(elf_attack):
    board = read_file('day15.in')
    battle = Battle(board, elf_attack)
    starting_elfs = battle.count_elfs()
    battle.fight_to_completion()
    ending_elfs = battle.count_elfs()
    print(starting_elfs, ending_elfs)
    if starting_elfs == ending_elfs:
        return battle.outcome()
    else:
        return -1


def solve2():
    outcome = -1
    attack = 3
    while outcome == -1:
        attack += 1
        outcome = do_elves_die(attack)
    return outcome


if __name__ == "__main__":
    # test_5()
    solve2()
