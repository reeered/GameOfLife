import copy


class Map:
    def __init__(self, _table):
        height = len(_table)
        width = len(_table[0])
        self.table = []
        self.table.append([0 for _ in range(width + 2)])
        for item in _table:
            temp_row = [0]
            temp_row.extend(item)
            temp_row.append(0)
            self.table.append(temp_row)
        self.table.append([0 for _ in range(width + 2)])
        self.Height = height
        self.Width = width

    def Update(self):
        H = self.Height
        W = self.Width
        bias = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        temp_map = copy.deepcopy(self.table)
        for i in range(1, H + 1):
            for j in range(1, W + 1):
                count = 0
                for xx, yy in bias:
                    count = count + self.table[i + xx][j + yy]
                if self.table[i][j] == 1:
                    if count < 2 or count > 3:
                        temp_map[i][j] = 0
                elif count == 3:
                    temp_map[i][j] = 1
        self.table = temp_map

    def flip_cell(self, row, column):
        self.table[row + 1][column + 1] = not self.table[row + 1][column + 1]
