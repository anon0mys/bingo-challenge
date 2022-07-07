# 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

# 22 13 17 11  0
#  8  2 23  4 24
# 21  9 14 16  7
#  6 10  3 18  5
#  1 12 20 15 19

#  3 15  0  2 22
#  9 18 13 17  5
# 19  8  7 25 23
# 20 11 10 24  4
# 14 21 16 12  6

# 14 21 17 24  4
# 10 16 15  9 19
# 18  8 23 26 20
# 22 11 13  6  5
#  2  0 12  3  7
from board import Board


def play_bingo(input_file):
    with open(input_file) as file:
        lines = file.readlines()
        inputs = lines[0].strip().split(',')
        boards = []
        board = Board()
        for line in lines[2:]:
            if line == '\n':
                boards.append(board)
                board = Board()
                continue
            board.add(line)
        boards.append(board)

    winning_board = None
    winning_number = None

    for number in inputs:
        for board in boards:
            board.mark(number)
            if board.wins():
                winning_number = number
                winning_board = board
                break
        if winning_board:
            break

    print(winning_board.sum_unmarked() * int(winning_number))


play_bingo('./test_input.txt')
