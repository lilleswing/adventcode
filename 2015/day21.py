import itertools


class Boss(object):
    def __init__(self):
        self.hp = 104
        self.damage = 8
        self.armor = 1


class Player(object):
    def __init__(self):
        self.hp = 100
        self.damage = 0
        self.armor = 0
        self.cost = 0
        self.gear = []

    def add_gear(self, gear):
        if gear is None:
            return
        self.armor += gear.armor
        self.damage += gear.damage
        self.cost += gear.cost


class Gear(object):
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor


weapons = [
    Gear("Dagger", 8, 4, 0),
    Gear("Shortsword", 10, 5, 0),
    Gear("Warhammer", 25, 6, 0),
    Gear("Longsword", 40, 7, 0),
    Gear("Greataxe", 74, 8, 0),
]
armors = [
    Gear("Leather", 13, 0, 1),
    Gear("Chainmail", 31, 0, 2),
    Gear("Splintmail", 53, 0, 3),
    Gear("Bandedmail", 75, 0, 4),
    Gear("Platemail", 102, 0, 5),
    None
]
rings = [
    Gear("Damage +1", 25, 1, 0),
    Gear("Damage +2", 50, 2, 0),
    Gear("Damage +3", 100, 3, 0),
    Gear("Defense +1", 20, 0, 1),
    Gear("Defense +2", 40, 0, 2),
    Gear("Defense +3", 80, 0, 3),
    None,
    None
]


def win_fight(player, boss):
    b_hp = boss.hp
    p_hp = player.hp
    while True:
        damage = max(player.damage - boss.armor, 1)
        b_hp -= damage
        if b_hp <= 0:
            return True
        damage = max(boss.damage - player.armor, 1)
        p_hp -= damage
        if p_hp <= 0:
            return False


def solve1():
    boss = Boss()
    lowest_cost = float('inf')
    for weapon, armor, ring1, ring2 in itertools.product(weapons, armors, rings, rings):
        player = Player()
        player.add_gear(ring1)
        player.add_gear(ring2)
        player.add_gear(weapon)
        player.add_gear(armor)
        is_winner = win_fight(player, boss)
        if is_winner:
            lowest_cost = min(lowest_cost, player.cost)
    print(lowest_cost)


def solve2():
    boss = Boss()
    highest_cost = -1 * float('inf')
    for weapon, armor, ring1, ring2 in itertools.product(weapons, armors, rings, rings):
        if ring1 == ring2:
            continue
        player = Player()
        player.add_gear(ring1)
        player.add_gear(ring2)
        player.add_gear(weapon)
        player.add_gear(armor)
        is_winner = win_fight(player, boss)
        if not is_winner:
            highest_cost = max(highest_cost, player.cost)
    print(highest_cost)


if __name__ == "__main__":
    solve1()
    solve2()
