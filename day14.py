import re


class Reindeer(object):
    def __init__(self, name, speed, active_time, cooldown):
        self.name = name
        self.speed = speed
        self.active_time = active_time
        self.cooldown = cooldown
        self.state = 'active'
        self.step_in = 0
        self.step = 0
        self.my_distance = 0
        self.points = 0

    def distance(self, time):
        for i in xrange(time):
            self.take_step()
        return self.my_distance

    def take_step(self):
        if self.state == 'active' and self.step_in == self.active_time:
            self.state = "cooldown"
            self.step_in = 0
        if self.state == 'cooldown' and self.step_in == self.cooldown:
            self.state = "active"
            self.step_in = 0
        if self.state == "active":
            self.my_distance += self.speed
        self.step_in += 1
        self.step += 1

    def add_point(self):
        self.points += 1


def parse(lines):
    pattern = "(.+) can fly (.+) km/s for (.+) seconds, but then must rest for (.+) seconds\."
    animals = list()
    for line in lines:
        match = re.match(pattern, line)
        name = match.group(1)
        speed = int(match.group(2))
        active_time = int(match.group(3))
        cooldown = int(match.group(4))
        animals.append(Reindeer(name, speed, active_time, cooldown))
    return animals


def solve1(reindeers, time):
    return max([x.distance(2503) for x in reindeers])


def solve2(reindeers, time):
    for i in xrange(time):
        for r in reindeers:
            r.take_step()
        largest = max([x.my_distance for x in reindeers])
        for r in reindeers:
            if r.my_distance == largest:
                r.add_point()

    return max([x.points for x in reindeers])


if __name__ == "__main__":
    all_reindeer = parse([x.strip() for x in open('day14.in').readlines()])
    print(solve1(all_reindeer, 2503))
    all_reindeer = parse([x.strip() for x in open('day14.in').readlines()])
    print(solve2(all_reindeer, 2503))
