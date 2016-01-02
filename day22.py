import copy


def boss_turn_expand(game):
    if game.is_loser():
        return None
    if game.is_winner():
        return game
    game.boss_turn()
    if game.is_loser():
        return None
    return game


class Game(object):
    def __init__(self, hard_mode=False):
        self.hp = 50
        self.mana = 500
        self.bosshp = 71
        self.bossdamage = 10
        self.poison = 0
        self.shield = 0
        self.recharge = 0
        self.manaspend = 0
        self.hard_mode = hard_mode
        self.actions = list()

    def apply_buffs(self):
        if self.poison > 0:
            self.bosshp -= 3
        if self.recharge > 0:
            self.mana += 101
        self.poison -= 1
        self.recharge -= 1
        self.shield -= 1

    def spend_mana(self, value):
        self.mana -= value
        self.manaspend += value

    def boss_turn(self):
        self.apply_buffs()
        if self.bosshp <= 0:
            return
        bossdamage = self.bossdamage
        if self.shield > 0:
            bossdamage = 3
        self.hp -= bossdamage

    def _magic_missile(self):
        game = self.take_turn()
        game.actions.append("magic missile")
        game.apply_buffs()
        if game.mana < 53:
            return None
        game.bosshp -= 4
        game.spend_mana(53)
        return boss_turn_expand(game)

    def _drain(self):
        game = self.take_turn()
        game.actions.append("drain")
        game.apply_buffs()
        if game.mana < 73:
            return None
        game.bosshp -= 2
        game.hp += 2
        game.spend_mana(73)
        return boss_turn_expand(game)

    def _shield(self):
        game = self.take_turn()
        game.actions.append("shield")
        game.apply_buffs()
        if game.mana < 113 or game.shield > 0:
            return None
        game.shield = 6
        game.spend_mana(113)
        return boss_turn_expand(game)

    def _poison(self):
        game = self.take_turn()
        game.actions.append("poison")
        game.apply_buffs()
        if game.mana < 173 or game.poison > 0:
            return None
        game.poison = 6
        game.spend_mana(173)
        return boss_turn_expand(game)

    def _recharge(self):
        game = self.take_turn()
        game.actions.append("recharge")
        game.apply_buffs()
        if game.mana < 229 or game.recharge > 0:
            return None
        game.recharge = 5
        game.spend_mana(229)
        return boss_turn_expand(game)

    def take_turn(self):
        game = copy.deepcopy(self)
        if game.hard_mode:
            game.hp -= 1
        return game

    def is_winner(self):
        return self.bosshp <= 0

    def is_loser(self):
        return self.hp <= 0


def solve_helper(game):
    solutions = list()

    def dfs(g):
        if g is None:
            return
        if g.is_winner():
            solutions.append(g)
            return
        if g.is_loser():
            return
        dfs(g._shield())
        dfs(g._recharge())
        dfs(g._poison())
        dfs(g._magic_missile())
        #dfs(g._drain())

    dfs(game)
    manaspends = sorted(solutions, key=lambda x: x.manaspend)
    print(manaspends[0].actions)
    manaspends = [x.manaspend for x in manaspends]
    return manaspends


def solve1():
    return solve_helper(Game())


def solve2():
    return solve_helper(Game(hard_mode=True))


def main():
    print(solve1())
    print(solve2())


if __name__ == "__main__":
    main()
