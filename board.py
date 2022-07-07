class Board:
    def __init__(self):
        self.row_key = 1
        self.rows = {}

    @property
    def row_count(self):
        return len(self.rows.values())

    def add(self, row_input):
        row = [number for number in row_input.strip().split(' ') if number != '']
        self.rows[self.row_key] = row
        self.row_key += 1

    def mark(self, number):
        for row_num in self.rows:
            row = self.rows[row_num]
            for i in range(0, len(row)):
                if row[i] == number:
                    row[i] = 'X'
            self.rows[row_num] = row

    def wins(self):
        # Also need to check for columns
        complete_rows = [row for row in self.rows.values() if len(set(row)) == 1]
        return any(complete_rows)

    def sum_unmarked(self):
        return sum(int(num) for row in self.rows.values() for num in row if num != 'X')

    def printout(self):
        for row in self.rows.values():
            print(row)
