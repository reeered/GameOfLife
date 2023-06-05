import random


class Map:

    def __init__(self, _table: list):
        self.height = len(_table)
        self.width = len(_table[0])
        self.table = []
        self.table.append([0 for _ in range(self.width + 2)])
        for item in _table:
            temp_row = [0]
            temp_row.extend(item)
            temp_row.append(0)
            self.table.append(temp_row)
        self.table.append([0 for _ in range(self.width + 2)])

    def Update(self):
        count = self.get_neighbor_count_map()
        for i in range(self.height):
            for j in range(self.width):
                if self.get_cell(i, j) == 1:
                    if count[i][j] < 2 or count[i][j] > 3:
                        self.set_cell(i, j, 0)
                elif count[i][j] == 3:
                    self.set_cell(i, j, 1)

    def flip_cell(self, row: int, col: int):
        if 0 <= row <= self.height and 0 <= col <= self.width:
            self.table[row + 1][col + 1] = not self.table[row + 1][col + 1]
        else:
            raise ValueError('Invalid row or col')

    def get_neighbor_count_map(self):
        count = [[0 for _ in range(self.width)] for _ in range(self.height)]
        bias = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for i in range(self.height):
            for j in range(self.width):
                for xx, yy in bias:
                    count[i][j] = count[i][j] + self.table[i + 1 + xx][j + 1 + yy]
        return count

    def get_cell(self, row: int, col: int):
        if 0 <= row <= self.height and 0 <= col <= self.width:
            return self.table[row + 1][col + 1]
        else:
            raise ValueError('Invalid row or col')

    def set_cell(self, row: int, col: int, state: int):
        if 0 <= row <= self.height and 0 <= col <= self.width:
            if state not in [0, 1]:
                raise ValueError('State should be zero or one')
            self.table[row + 1][col + 1] = state
        else:
            raise ValueError('Invalid row or col')

    def reset(self, possibility: float):
        for i in range(self.height):
            for j in range(self.width):
                self.table[i + 1][j + 1] = 1 if random.random() <= possibility else 0
