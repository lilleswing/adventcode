ON = "#"
OFF = "."
SIZE = 100


def create_empty():
    b = []
    for i in xrange(SIZE):
        b.append([OFF] * SIZE)
    return b


def count_on(board):
    total = 0
    for i in xrange(len(board)):
        for j in xrange(len(board)):
            if board[i][j] == ON:
                total += 1
    return total


def create_board():
    my_input = [x.strip() for x in open('day18.in').readlines()]
    board = list()
    for line in my_input:
        board.append(list(line))
    return board


def evaluate_pos(board, row, col):
    num_on = 0
    for i in xrange(row - 1, row + 2):
        for j in xrange(col - 1, col + 2):
            if (i == row and j == col) or i < 0 or i >= len(board) or j < 0 or j >= len(board):
                continue
            if board[i][j] == ON:
                num_on += 1
    if board[row][col] == ON:
        if num_on == 2 or num_on == 3:
            return ON
        return OFF
    if num_on == 3:
        return ON
    return OFF


def take_step(board, new_board):
    for row in xrange(len(board)):
        for col in xrange(len(board)):
            value = evaluate_pos(board, row, col)
            new_board[row][col] = value
    return new_board


def display_board(board):
    print()
    print()
    for row in board:
        print "".join(row)


def solve1():
    board = create_board()
    for i in xrange(100):
        new_board = create_empty()
        take_step(board, new_board)
        board = new_board
    return count_on(board)


def solve2():
    def set_corners(my_board):
        my_board[0][0] = ON
        my_board[0][-1] = ON
        my_board[-1][0] = ON
        my_board[-1][-1] = ON
    board = create_board()
    set_corners(board)
    for i in xrange(100):
        new_board = create_empty()
        take_step(board, new_board)
        board = new_board
        set_corners(board)
    return count_on(board)


def main():
    print(solve1())
    print(solve2())


if __name__ == "__main__":
    main()
