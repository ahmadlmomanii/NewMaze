from cell import Cell
import random


class Grid:
    def __init__(self, cell: type[Cell], height: int, width: int, seed: int):
        self.height = height
        self.width = width
        self.cell = cell
        self.cells_42: list[Cell] = []
        self.grid: list[Cell] = []
        self.path_cells: list[Cell] = []
        self.rand = random.Random(seed)
        self.path_toggle = 0
        self.color_rotate_counter = 0
        self.output_file = ""

    def init_grid(self) -> None:
        self.grid = [
            self.cell() for i in range(self.width * self.height)]
        counter = 0
        # set position
        for x in range(self.height):
            for y in range(self.width):
                self.grid[counter].position = x, y
                counter += 1

    def path_init(self, path: list[Cell], start_position, end_position):
        for cell in path:
            self.path_cells.append(cell)

    def get_start_end(self, start_position, end_position) -> list[Cell]:
        start_end: list[Cell] = [Cell(), Cell()]
        for cell in self.grid:
            if cell.position == start_position:
                start_end[0] = cell
            if cell.position == end_position:
                start_end[1] = cell
        return start_end

    def select_neighbor(self, cell: Cell) -> Cell | None:
        neighbors: list[Cell] = []

        index = self.grid.index(cell)

        # Up
        if index >= self.width:
            neighbor = self.grid[index - self.width]
            if not neighbor.visited:
                neighbors.append(neighbor)

        # Right
        if index % self.width != self.width - 1:
            neighbor = self.grid[index + 1]
            if not neighbor.visited:
                neighbors.append(neighbor)

        # Down
        if index < len(self.grid) - self.width:
            neighbor = self.grid[index + self.width]
            if not neighbor.visited:
                neighbors.append(neighbor)

        # Left
        if index % self.width != 0:
            neighbor = self.grid[index - 1]
            if not neighbor.visited:
                neighbors.append(neighbor)

        if neighbors:
            random_neighbor = self.rand.choice(neighbors)
            return random_neighbor

        return None

    def get_neighbors(self, cell: Cell) -> list[Cell] | None:
        neighbors: list[Cell] = []

        index = self.grid.index(cell)

        # Up
        if index >= self.width:
            neighbor = self.grid[index - self.width]
            if not neighbor.late_visited:
                neighbors.append(neighbor)

        # Right
        if index % self.width != self.width - 1:
            neighbor = self.grid[index + 1]
            if not neighbor.late_visited:
                neighbors.append(neighbor)

        # Down
        if index < len(self.grid) - self.width:
            neighbor = self.grid[index + self.width]
            if not neighbor.late_visited:
                neighbors.append(neighbor)

        # Left
        if index % self.width != 0:
            neighbor = self.grid[index - 1]
            if not neighbor.late_visited:
                neighbors.append(neighbor)

        if neighbors:
            return neighbors
        return None

    def RemoveWalls(self, current: Cell, next: Cell) -> None:
        if current.position[0] == next.position[0]:
            if current.position[1] > next.position[1]:
                current.West = 0
                next.East = 0
            elif current.position[1] < next.position[1]:
                current.East = 0
                next.West = 0
        elif current.position[1] == next.position[1]:
            if current.position[0] > next.position[0]:
                current.North = 0
                next.South = 0
            elif current.position[0] < next.position[0]:
                current.South = 0
                next.North = 0

    def CheckWalls(self, current: Cell, next: Cell) -> bool:
        if current.position[0] == next.position[0]:
            if current.position[1] > next.position[1]:
                if current.West == 0 and next.East == 0:
                    return True
            if current.position[1] < next.position[1]:
                if current.East == 0 and next.West == 0:
                    return True
        if current.position[1] == next.position[1]:
            if current.position[0] > next.position[0]:
                if current.North == 0 and next.South == 0:
                    return True
            if current.position[0] < next.position[0]:
                if current.South == 0 and next.North == 0:
                    return True
        return False
