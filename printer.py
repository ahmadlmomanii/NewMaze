from cell import Cell
from grid import Grid
from typing import TextIO

def print_hexa_cells(self, output_file: str) -> None:
    counter = 0
    file: TextIO = open(output_file, "w")
    for line in range(self.height):
        hexa_line: str = ""
        for cell in range(self.width):
            hexa_line += (self.grid[counter].hexa_cell())
            counter += 1
        file.writelines(hexa_line)
        if line != self.height - 1:
            file.writelines("\n")


def print_grid(
    maze: Grid,
    start_cell: Cell,
    end_cell: Cell,
    color: list[tuple[str, str, str]]
) -> None:
    maze.color_rotate_counter %= 5
    for line in range(maze.height):
        # Cell roof
        for cell in range(maze.width):
            current = maze.grid[line * maze.width + cell]
            print(color[maze.color_rotate_counter][0], end="")
            print("+", end="")
            print(color[5][2], end="")

            if current.North:
                print(color[maze.color_rotate_counter][0], end="")
                print("===", end="")
                print(color[5][2], end="")
            else:
                print("   ", end="")

            if cell == maze.width - 1:
                print(color[maze.color_rotate_counter][0], end="")
                print("+", end="")
                print(color[5][2], end="")

        print()

        # Cell walls
        for cell in range(maze.width):
            current = maze.grid[line * maze.width + cell]
            if current.West:
                print(color[maze.color_rotate_counter][0], end="")
                print("║", end="")
                print(color[5][2], end="")
            else:
                print(" ", end="")
            if current.position == start_cell.position:
                print(color[5][0], end="")
                print("███", end="")
                print(color[5][2], end="")

            elif current.position == end_cell.position:
                print(color[5][1], end="")
                print("███", end="")
                print(color[5][2], end="")

            elif current in maze.path_cells and maze.path_toggle % 2 == 1:
                print(color[maze.color_rotate_counter][2], end="")
                print(" ◆ ", end="")
                print(color[5][2], end="")

            elif current in maze.cells_42:
                print(color[maze.color_rotate_counter][1], end="")
                print("███", end="")
                print(color[5][2], end="")

            else:
                print("   ", end="")

            if cell == maze.width - 1:
                print(color[maze.color_rotate_counter][0], end="")
                print("║", end="")
                print(color[5][2], end="")

        print()

    # Bottom walls
    for cell in range(maze.width):
        current = maze.grid[(maze.height - 1) * maze.width + cell]

        print(color[maze.color_rotate_counter][0], end="")
        print("+", end="")
        print(color[5][2], end="")
        if current.South:
            print(color[maze.color_rotate_counter][0], end="")
            print("===", end="")
            print(color[5][2], end="")
        else:
            print("    ", end="")

        if cell == maze.width - 1:
            print(color[maze.color_rotate_counter][0], end="")
            print("+", end="")
            print(color[5][2], end="")

    print()
