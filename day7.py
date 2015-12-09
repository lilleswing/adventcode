class Gate(object):
    def __init__(self, st):
        self.satisfied = False
        vars = st.split(" -> ")
        self.output = vars[1]
        self.input_vars = vars[0].split(' ')
        self.value = None


def is_done(gate_map):
    for value in gate_map.values():
        if not value.satisfied:
            return False
    return True


def not_value(value):
    d = {"1": "0", "0": "1"}
    s = str(bin(value))[2:].zfill(16)
    compliment = "".join([d[x] for x in s])
    return int(compliment, 2)


def get_value(key, gate_map):
    if key not in gate_map:
        try:
            return int(key)
        except ValueError:
            return None
    val = gate_map[key]
    if val.satisfied:
        return val.value
    return None


def satisfy(gate, gate_map):
    def satisfy_value(gate, gate_map):
        if len(gate.input_vars) != 1:
            return False
        val = get_value(gate.input_vars[0], gate_map)
        if val is None:
            return False
        gate.value = val
        gate.satisfied = True
        return True

    def satisfy_not(gate, gate_map):
        if gate.input_vars[0] == 'NOT':
            val = gate_map[gate.input_vars[1]]
            if val.satisfied:
                my_val = not_value(val.value)
                gate.value = my_val
                gate.satisfied = True
                return True
        return False

    def satisfy_or(gate, gate_map):
        if len(gate.input_vars) == 3 and gate.input_vars[1] == 'OR':
            val1 = gate_map[gate.input_vars[0]]
            val2 = gate_map[gate.input_vars[2]]
            if val1.satisfied and val2.satisfied:
                my_val = val1.value | val2.value
                gate.value = my_val
                gate.satisfied = True
                return True
        return False

    def satisfy_and(gate, gate_map):
        if len(gate.input_vars) == 3 and gate.input_vars[1] == 'AND':
            val1 = get_value(gate.input_vars[0], gate_map)
            if val1 is None:
                return False
            val2 = get_value(gate.input_vars[2], gate_map)
            if val2 is None:
                return False
            my_val = val1 & val2
            gate.value = my_val
            gate.satisfied = True
            return True
        return False

    def satisfy_lshift(gate, gate_map):
        if len(gate.input_vars) == 3 and gate.input_vars[1] == 'LSHIFT':
            val1 = gate_map[gate.input_vars[0]]
            val2 = int(gate.input_vars[2])
            if val1.satisfied:
                my_val = val1.value << val2
                gate.value = my_val
                gate.satisfied = True
                return True
        return False

    def satisfy_rshift(gate, gate_map):
        if len(gate.input_vars) == 3 and gate.input_vars[1] == 'RSHIFT':
            val1 = gate_map[gate.input_vars[0]]
            val2 = int(gate.input_vars[2])
            if val1.satisfied:
                my_val = val1.value >> val2
                gate.value = my_val
                gate.satisfied = True
                return True
        return False

    if gate.satisfied:
        return
    if satisfy_value(gate, gate_map):
        return
    if satisfy_not(gate, gate_map):
        return
    if satisfy_or(gate, gate_map):
        return
    if satisfy_and(gate, gate_map):
        return
    if satisfy_lshift(gate, gate_map):
        return
    if satisfy_rshift(gate, gate_map):
        return
    return


def solve1(gate_map):
    while not is_done(gate_map):
        for gate in gate_map.values():
            satisfy(gate, gate_map)

    return gate_map['a'].value


def solve2(gate_map):
    gate_map['b'].value = 16076
    gate_map['b'].satisfied = True
    while not is_done(gate_map):
        for gate in gate_map.values():
            satisfy(gate, gate_map)
    return gate_map['a'].value


if __name__ == "__main__":
    all_lines = [Gate(y) for y in [x.strip() for x in open("day7.in").readlines()]]
    all_gate_map = {x.output: x for x in all_lines}
    print(solve1(all_gate_map))
    all_lines = [Gate(y) for y in [x.strip() for x in open("day7.in").readlines()]]
    all_gate_map = {x.output: x for x in all_lines}
    print(solve2(all_gate_map))
