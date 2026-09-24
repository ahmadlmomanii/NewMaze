from colors import COLOR_CHOICES
from cell import Cell
from generator import init_42, dfs, open_more_cells
from grid import Grid
from parsing import load_config
from shortest_path import bfs, path_direction
from printer import print_grid, print_hexa_cells


def maze_init() -> tuple[Grid, Cell, Cell, str]:

    values = load_config()
    width, height, start_position, end_position, seed, perfect, file = values

    maze = Grid(Cell, height, width, seed)

    maze.init_grid()

    init_42(maze)

    grid = maze.grid

    start_cell, end_cell = maze.get_start_end(
        start_position,
        end_position
    )
    if start_cell in maze.cells_42 or end_cell in maze.cells_42:
        print("Enter valid Entry/Exit position that aren't in 42 cells")
        exit()
    dfs(grid[0], maze)
    if perfect is False:
        open_more_cells(maze.grid, maze)

    path = bfs(start_cell, end_cell, maze)

    if path:
        maze.path_init(
            path,
            start_position,
            end_position
        )
        direction = path_direction(path)
    print_grid(
        maze,
        start_cell,
        end_cell,
        COLOR_CHOICES
    )
    return (maze, start_cell, end_cell, direction)


def choices(maze: Grid, start_cell: Cell, end_cell: Cell):
    choice = 0
    while choice != 4:
        if choice in range(5):
            print("=== A-Maze-ing ===")
            print("1. Re-fenerate a new maze")
            print("2. SHow/Hide path from entry to exit")
            print("3. Rotate maze colors")
            print("4. Quit")
        try:
            choice = -1
            choice = int(input("Choice? (1-4): "))
        except KeyboardInterrupt:
            print()
            exit()
        except Exception:
            print("enter an integer!!!")
            continue
        if choice == 1:
            maze = maze_init()[0]
        elif choice == 2:
            maze.path_toggle += 1
            print_grid(maze, start_cell, end_cell, COLOR_CHOICES)
        elif choice == 3:
            maze.color_rotate_counter += 1
            print_grid(maze, start_cell, end_cell, COLOR_CHOICES)
        elif choice == 4:
            pass
        else:
            print("PLEASE ENTER A VALID NUMNBER!!! (1 - 4)")


def main():
    maze, start, end, direction = maze_init()
    choices(maze, start, end)

    start_pos = start.position
    end_pos = end.position

    print_hexa_cells(maze, "maze.txt")

    f = open("maze.txt", "a")

    f.write("\n\n")

    f.write(str(start_pos)[1: len(str(start_pos)) - 1])
    f.write("\n")

    f.write(str(end_pos)[1: len(str(end_pos)) - 1])

    f.write("\n")
    f.write(direction)


if __name__ == "__main__":
    main()
