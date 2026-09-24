class Cell:
    def __init__(self) -> None:
        self.North = 1
        self.East = 1
        self.South = 1
        self.West = 1
        self.position = (0, 0)
        self.visited = False
        self.late_visited = False
        self.parent = self

    def hexa_cell(self) -> str:
        bit_list = []
        for direction in [self.West, self.South, self.East, self.North]:
            if direction:
                bit_list.append(1)
            else:
                bit_list.append(0)
        cell_decimal_value = 0
        if bit_list[0]:
            cell_decimal_value += 8
        if bit_list[1]:
            cell_decimal_value += 4
        if bit_list[2]:
            cell_decimal_value += 2
        if bit_list[3]:
            cell_decimal_value += 1
        return hex(cell_decimal_value)[2:].capitalize()

    def count_walls(self) -> int:
        walls_counter = 0
        walls_counter += self.South + self.West + self.East + self.North
        return walls_counter
