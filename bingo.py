from board import Board


class Bingo:
    def __init__(self, input_file):
        self.input_file = input_file
        self.bingo_balls = None
        self.boards = []
        self.winning_board = None
        self.winning_number = None
        self.setup()
        self.round = 1

    def setup(self):
        with open(self.input_file) as file:
            file_data = file.readlines()
            self.bingo_balls = self.build_bingo_balls(file_data[0])
            self.boards = self.build_boards(file_data[2:])

    def build_bingo_balls(self, inputs_line):
        return inputs_line.strip().split(',')

    def build_boards(self, board_lines):
        boards = []
        id = 1
        board = Board(id=id)
        for line in board_lines:
            if line == '\n':
                boards.append(board)
                id += 1
                board = Board(id=id)
                continue
            board.add(line)
        boards.append(board)
        return boards

    def play(self):
        self.announce_start()
        for bingo_ball in self.bingo_balls:
            self.announce_round(bingo_ball)
            self.round += 1
            self.mark_boards(bingo_ball)
            if self.winning_board:
                self.announce_winner()
                break

    def mark_boards(self, bingo_ball):
        for board in self.boards:
            board.mark(bingo_ball)
            if board.wins():
                self.winning_number = bingo_ball
                self.winning_board = board
                break

    def score(self):
        return self.winning_board.sum_unmarked() * int(self.winning_number)

    def announce_round(self, bingo_ball):
        print(f"~~~ Round {self.round} ~~~")
        print(f"Your bingo ball is: {bingo_ball}")

    def announce_start(self):
        print(f"~~~ Welcome to Bingo ~~~")
        print(f"We have {len(self.boards)} players!\n")
        for board in self.boards:
            print(f"Player {board.id}:")
            board.printout()
            print('\n')

    def announce_winner(self):
        print("~~~ We have a winner! ~~~")
        print(f"The winning board is Player {self.winning_board.id} "
              f"with a score of {self.score()}\n")
        self.winning_board.printout()


bingo = Bingo(input_file='./test_input.txt')
bingo.play()
