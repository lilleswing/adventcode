class Window(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def is_in(self, n):
        return self.low <= n and self.high >= n

    def __repr__(self) -> str:
        return f"[{self.low}, {self.high}]"


def parse(fname):
    lines = open(fname).readlines()
    lines = [x.strip() for x in lines]
    windows = []
    while lines[0] != "":
        v1, v2 = lines[0].split('-')
        v1, v2 = int(v1), int(v2)
        windows.append(Window(v1, v2))
        lines = lines[1:]
    ids = []
    lines = lines[1:]
    while len(lines) > 0:
        ids.append(int(lines[0]))
        lines = lines[1:]
    return windows, ids

def is_in_window(windows, n):
    for window in windows:
        if window.is_in(n):
            return True
    return False

def part1():
    windows, ids = parse('day05.in')
    total = 0
    for my_id in ids:
        if is_in_window(windows, my_id):
            total += 1
    print(total)


def part2():
    windows, ids = parse('day05.in')
    windows = sorted(windows, key=lambda x: (x.low, x.high))
    new_windows, windows = [windows[0]], windows[1:]
    for w in windows:
        if w.low <= new_windows[-1].high:
            new_windows[-1].high = max(w.high, new_windows[-1].high)
        else:
            new_windows.append(w)
    total = 0
    for w in new_windows:
        total += w.high - w.low + 1
    print(total)


if __name__ == "__main__":
    #part1()
    part2()
