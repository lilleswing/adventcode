class Sue(object):
    def __init__(self, name, d):
        self.name = name
        self.d = d


def parse(lines):
    sues = list()
    for line in lines:
        vals = line.split(":", 1)
        name = vals[0]
        d = dict()
        for var in vals[1].split(', '):
            key, value = var.split(':')
            key = key.strip()
            d[key] = int(value)
        sues.append(Sue(name, d))
    return sues


def solve1(target, all_sues):
    for sue in all_sues:
        is_valid = True
        for key in sue.d.keys():
            if sue.d[key] != target.d[key]:
                is_valid = False
        if is_valid:
            print sue.name


def solve2(target, all_sues):
    for sue in all_sues:
        is_valid = True
        for key in sue.d.keys():
            if key == 'cats' or key == 'trees':
                if sue.d[key] <= target.d[key]:
                    is_valid = False
            elif key == 'pomeranians' or key == 'goldfish':
                if sue.d[key] >= target.d[key]:
                    is_valid = False
            else:
                if sue.d[key] != target.d[key]:
                    is_valid = False
        if is_valid:
            print sue.name


def main():
    my_sue_d = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
    }
    mySue = Sue("target", my_sue_d)
    all_sues = parse([x.strip() for x in open('day16.in').readlines()])
    solve1(mySue, all_sues)
    solve2(mySue, all_sues)


if __name__ == "__main__":
    main()
