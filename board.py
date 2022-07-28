class Board:
    def __init__(self, id):
        self.id = id
        self.row_number = 1
        self.rows_by_row_number = {}

    @property
    def row_count(self):
        return len(self.rows)

    @property
    def rows(self):
        return self.rows_by_row_number.values()

    def add(self, row_input):
        row = [number for number in row_input.strip().split(' ') if number != '']
        self.rows_by_row_number[self.row_number] = row
        self.row_number += 1

    def mark(self, bingo_ball):
        for row_number in self.rows_by_row_number:
            row = self.rows_by_row_number[row_number]
            updated_row = self.mark_if_found(bingo_ball, row)
            if updated_row:
                self.rows_by_row_number[row_number] = updated_row
                break

    def mark_if_found(self, bingo_ball, row):
        row_length = range(0, len(row))
        for index in row_length:
            if row[index] == bingo_ball:
                row[index] = 'X'
                return row

    def wins(self):
        # Also need to check for columns
        complete_rows = [row for row in self.rows if len(set(row)) == 1]
        if any(complete_rows):
            print("\nBINGO!!\n")
        return any(complete_rows)

    def sum_unmarked(self):
        return sum(int(num) for row in self.rows for num in row if num != 'X')

    def printout(self):
        for row in self.rows:
            print(row)
