import re

import datetime

base_mol = 'CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF'


class Expansion(object):
    def __init__(self, from_ch, to_ch):
        self.from_ch = from_ch
        self.to_ch = to_ch


def parse(lines):
    rules = list()
    for line in lines:
        match = re.match(r"(\w+) => (\w+)", line)
        rules.append(Expansion(match.group(1), match.group(2)))
    return rules


def get_extensions(rules, base):
    all_possible = set()
    for rule in rules:
        for match in re.finditer(rule.from_ch, base):
            start_index = match.start(0)
            end_index = match.end(0)
            my_mol = "%s%s%s" % (base[:start_index], rule.to_ch, base[end_index:])
            all_possible.add(my_mol)
    return all_possible


def solve1(rules):
    return len(get_extensions(rules, base_mol))


def dfs(rules, target, sofar, start_time):
    """
    Greedy DFS which pockets best answer so far
    Let it run for 5 seconds
    :param rules:
    :param target:
    :param sofar:
    :return:
    """
    total_best = [(False, float('inf'))]
    start_time = datetime.datetime.now()

    def dfs_helper(rules, target, sofar):
        if datetime.datetime.now() - start_time > datetime.timedelta(seconds=5):
            return total_best[0]
        if target == 'e':
            last_best = total_best[0]
            if last_best[1] > sofar:
                total_best[0] = (True, sofar)
            return True, 0
        is_solved = False
        best = float('inf')
        for rule in rules:
            for match in re.finditer(rule.to_ch, target):
                start_index = match.start(0)
                end_index = match.end(0)
                my_mol = "%s%s%s" % (target[:start_index], rule.from_ch, target[end_index:])
                retval, retdistance = dfs_helper(rules, my_mol, sofar + 1)
                if retval:
                    is_solved = retval
                    best = retdistance
        return is_solved, best + 1
    dfs_helper(rules, target, 0)
    return total_best


def solve2(rules):
    rules = sorted(rules, key=lambda x: len(x.to_ch) - len(x.from_ch), reverse=True)
    return dfs(rules, base_mol, 0, datetime.datetime.now())


def main():
    rules = parse([x.strip() for x in open('day19.in').readlines()])
    print(solve1(rules))
    print(solve2(rules))


if __name__ == "__main__":
    main()
