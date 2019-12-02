def read_file(fname):
    with open(fname) as fin:
        return [x.strip() for x in fin.readlines()]
