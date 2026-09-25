class Cell:
    """
    a class to represent each cell.

    Attributes:
        North: an integer represinting the north wall of the cell.
        East: an integer represinting the east wall of the cell.
        South: an integer represinting the south wall of the cell.
        West: an integer represinting the south wall of the cell.
        position: a tuple that store 2 integer as postions of the cell.
        visitied: a boolean indecates if the cell has been visited.
        late_visited: a boolean indecates if the cell has been late visitet.
        perant: a cell object or None that stores the previous cell or none.
    """
    def __init__(self) -> None:
        """
        a constructor that initilize the Object variables with defalt values.

        args:
            self: the class object.

        returns:
            None.
        """
        self.North = 1
        self.East = 1
        self.South = 1
        self.West = 1
        self.position = (0, 0)
        self.visited = False
        self.late_visited = False
        self.parent = self

    def hexa_cell(self) -> str:
        """
        a function that return the value of the cell as hexa decimal.

        args:
            self: the class object.

        returns:
            str Value of the hexa decimal.
        """
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
        """
        a function that counts the close walls of the cell

        args:
            self: the class object.

        returns:
            int stors the number of open walls.
        """
        walls_counter = 0
        walls_counter += self.South + self.West + self.East + self.North
        return walls_counter
