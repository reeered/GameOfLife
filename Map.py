import copy
class Map:
    def __init__(self, _table, _height, _width):
        self.table = []
        self.table.append([0 for _ in range(_width + 2)])
        for item in _table:
            temp_row = [ ]
            temp_row.append(0)
            temp_row.extend(item)
            temp_row.append(0)
            self.table.append(temp_row)
        self.table.append([0 for _ in range(_width + 2)])
        self.Height = _height
        self.Width = _width
    def Update(self):
        H = self.Height
        W = self.Width
        bias = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
        temp_map = copy.deepcopy(self.table)
        for i in range(1,H+1):
            for j in range(1,W+1):
                count = 0
                for xx,yy in bias:
                    count = count + self.table[i+xx][j+yy]
                if self.table[i][j] == 1:
                    if count < 2 or count > 3:
                        temp_map[i][j] = 0
                else :
                    if count == 3:
                        temp_map[i][j] = 1
        self.table = temp_map
    def Display(self):
        print(self.table)


map = [[1,0,1],[0,0,0],[0,1,0]]

Test =Map(map,3,3)
