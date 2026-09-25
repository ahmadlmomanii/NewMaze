from mazegen.cell import Cell
import random


class Grid:
    """
    Represent the maze grid and provide maze related operations.

    The grid manages the maze cells, their positions, visited states,
    paths, random neighbor selection, and wall manipulation.

    Attributes:
        height: The number of rows in the grid.
        width: The number of columns in the grid.
        cell: The cell class used to create grid cells.
        cells_42: Cells that form the 42 logo.
        grid: All cells contained in the maze.
        path_cells: Cells belonging to the solution path.
        rand: Random number generator initialized with the given seed.
        path_toggle: Controls path display state.
        color_rotate_counter: Tracks the current color palette.
        output_file: Path or name of the maze output file.
    """
    def __init__(
            self, cell: type[Cell], height: int,
            width: int, seed: int) -> None:
        """
        Initialize a maze grid.

        Args:
            cell: The class used to create individual maze cells.
            height: The number of rows in the grid.
            width: The number of columns in the grid.
            seed: Seed used to initialize the random number generator.

        returns:
            None.
        """
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
        """
        Create and initialize all cells in the maze grid.

        Each cell is assigned its position based on its row and column.
        """
        self.grid = [
            self.cell() for i in range(self.width * self.height)]
        counter = 0
        # set position
        for x in range(self.height):
            for y in range(self.width):
                self.grid[counter].position = x, y
                counter += 1

    def path_init(self, path: list[Cell]) -> None:
        """
        Initialize the solution path.

        Args:
            path: Cells that belong to the solution path.
        """
        for cell in path:
            self.path_cells.append(cell)

    def get_start_end(self, start_position: tuple[int, int],
                      end_position: tuple[int, int]) -> list[Cell]:
        """
        Find the cells corresponding to the start and end positions.

        Args:
            start_position: Position of the starting cell.
            end_position: Position of the ending cell.

        Returns:
            A list containing the start cell followed by the end cell.
        """
        start_end: list[Cell] = [Cell(), Cell()]
        for cell in self.grid:
            if cell.position == start_position:
                start_end[0] = cell
            if cell.position == end_position:
                start_end[1] = cell
        return start_end

    def select_neighbor(self, cell: Cell) -> Cell | None:
        """
        Select a random unvisited neighboring cell.

        Args:
            cell: The cell whose neighbors are examined.

        Returns:
            A randomly selected unvisited neighboring cell, or None if
            no unvisited neighbors are available.
        """
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
        """
        Get all unvisited neighbors of a cell.

        Args:
            cell: The cell whose neighbors are examined.

        Returns:
            A list of unvisited neighboring cells, or None if there
            are no available neighbors.
        """
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
        """
        Remove the wall between two adjacent cells.

        Args:
            current: The first cell.
            next: The adjacent cell whose shared wall is removed.
        """
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
        """
        Check whether two adjacent cells have their shared wall removed.

        Args:
            current: The first cell.
            next: The adjacent cell to check.

        Returns:
            True if the shared wall between the cells is open,
            otherwise False.
        """
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
