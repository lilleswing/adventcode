class Op(object):
    def __init__(self, x, op_name, y, output_name):
        self.x = x
        self.y = y
        self.op_name = op_name
        self.output_name = output_name
        self.resolved = False

    def execute(self, a, b, op):
        if op == 'AND':
            if a == 1 and b == 1:
                return 1
            else:
                return 0
        if op == 'OR':
            if a == 1 or b == 1:
                return 1
            else:
                return 0
        if op == 'XOR':
            if a == b:
                return 0
            else:
                return 1
        raise ValueError("Unknown op")

    def fill_vals(self, vals):
        if self.resolved:
            return
        if self.x in vals and self.y in vals:
            a, b = vals[self.x], vals[self.y]
            vals[self.output_name] = self.execute(a, b, self.op_name)
            self.resolved = True



    def __repr__(self):
        return f"{self.output_name} = {self.x} {self.op_name} {self.y}"


def part1():
    values = {}
    lines = [x.strip() for x in open('day24.in').readlines()]
    while lines[0] != "":
        n, v = lines[0].split(':')
        v = int(v)
        values[n] = v
        lines = lines[1:]
    lines = lines[1:]
    ops = []
    while len(lines) > 0:
        vars = lines[0].split(' ')
        my_op = Op(vars[0], vars[1], vars[2], vars[4])
        lines = lines[1:]
        ops.append(my_op)

    total_filled = 0
    while total_filled != len(ops):
        for op in ops:
            op.fill_vals(values)
        total_filled = len([x for x in ops if x.resolved])

    key_vals = [(k,v) for k, v in values.items()]
    key_vals = [ x for x in key_vals if x[0].startswith('z')]
    key_vals = sorted(key_vals, reverse=True)
    print(key_vals)
    key_vals = "".join([str(x[1]) for x in key_vals])
    print(key_vals)
    key_vals = f"0b{key_vals}"
    print(int(key_vals, 2))




if __name__ == "__main__":
    part1()
