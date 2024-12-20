import copy
import re


class Workflow(object):
    def __init__(self, name: str, rules: list[str]):
        self.name = name
        self.rules = rules

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f"{self.name}: {self.rules}"


def apply_rule(rule: str, registers: dict[str, int]) -> tuple[bool, str]:
    if rule.find(':') == -1:
        return True, rule
    conditional, jump = rule.split(':')
    fn_lookup = {
        '<': lambda x, y: x < y,
        '>': lambda x, y: x > y,
    }
    my_register = conditional[0]
    conditional_fn = fn_lookup[conditional[1]]
    if conditional_fn(registers[my_register], int(conditional[2:])):
        return True, jump
    return False, ""


def program(workflows: dict[str, Workflow], registers: dict[str, int]) -> bool:
    current = workflows["in"]
    while True:
        is_new_workflow = False
        for rule in current.rules:
            success, next_workflow = apply_rule(rule, registers)
            if success and next_workflow in ("A", "R"):
                if next_workflow == 'A':
                    return True
                return False
            if success:
                current = workflows[next_workflow]
                is_new_workflow = True
                break
        if not is_new_workflow:
            raise ValueError("Shouldn't Get Here")


def part1(fname):
    lines = [x.strip() for x in open(fname).readlines()]
    workflows = {}
    while lines[0] != '':
        name_idx = lines[0].find('{')
        name = lines[0][:name_idx].strip()
        rest = lines[0][name_idx:]
        rest = rest.replace('{', '').replace('}', '')
        rules = rest.split(',')
        workflows[name] = Workflow(name, rules)
        lines = lines[1:]

    lines = lines[1:]
    total = 0
    for line in lines:
        vals = re.findall(r"\d+", line)
        vals = [int(x) for x in vals]
        registers = {
            'x': vals[0],
            'm': vals[1],
            'a': vals[2],
            's': vals[3],
        }
        if program(workflows, registers):
            total += sum(registers.values())
    print(total)


def apply_rule2(rule: str, registers: dict[str, tuple[int, int]]) -> list[tuple[bool, str, dict[str, tuple[int, int]]]]:
    if rule.find(':') == -1:
        retval = []
        retval.append((True, rule, copy.deepcopy(registers)))
        return retval
    retval = []
    conditional, jump = rule.split(':')
    my_register = conditional[0]
    conditional_chr = conditional[1]
    conditional_val = int(conditional[2:])
    existing_range = registers[my_register]
    if conditional_chr == '<':
        low_range = (existing_range[0], conditional_val)
        high_range = (conditional_val, existing_range[1])
        if low_range[0] < low_range[1]:
            new_registers = copy.deepcopy(registers)
            new_registers[my_register] = low_range
            retval.append((True, jump, new_registers))
        if high_range[0] < high_range[1]:
            new_registers = copy.deepcopy(registers)
            new_registers[my_register] = high_range
            retval.append((False, "", new_registers))
        return retval
    elif conditional_chr == '>':
        low_range = (existing_range[0], conditional_val + 1)
        high_range = (conditional_val + 1, existing_range[1])
        if low_range[0] < low_range[1]:
            new_registers = copy.deepcopy(registers)
            new_registers[my_register] = low_range
            retval.append((False, "", new_registers))
        if high_range[0] < high_range[1]:
            new_registers = copy.deepcopy(registers)
            new_registers[my_register] = high_range
            retval.append((True, jump, new_registers))
        return retval
    else:
        raise ValueError("Unknown conditional")


def dfs(workflows: dict[str, Workflow],
        registers: dict[str, tuple[int, int]],
        workflow_name: str,
        rule_number: int) -> int:
    if workflow_name == 'R':
        return 0
    if workflow_name == 'A':
        total = 1
        for r in registers.values():
            total *= (r[1] - r[0])
        return total
    current = workflows[workflow_name]
    rule = current.rules[rule_number]
    moves = apply_rule2(rule, registers)
    total = 0
    for should_jump, jump_location, new_registers in moves:
        if should_jump:
            total += dfs(workflows, new_registers, jump_location, 0)
        else:
            total += dfs(workflows, new_registers, workflow_name, rule_number + 1)
    return total


def part2(fname):
    lines = [x.strip() for x in open(fname).readlines()]
    workflows = {}
    while lines[0] != '':
        name_idx = lines[0].find('{')
        name = lines[0][:name_idx].strip()
        rest = lines[0][name_idx:]
        rest = rest.replace('{', '').replace('}', '')
        rules = rest.split(',')
        workflows[name] = Workflow(name, rules)
        lines = lines[1:]
    registers = {
        'x': (1, 4001),
        'm': (1, 4001),
        'a': (1, 4001),
        's': (1, 4001),
    }
    valid_ways = dfs(workflows, registers, 'in', 0)
    print(valid_ways)


if __name__ == "__main__":
    # part1('day19.in')
    part2('day19.in')
