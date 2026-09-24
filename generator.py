from cell import Cell
from grid import Grid


def dfs(current: Cell, maze: Grid) -> None:
    current.visited = True
    visited: list[Cell] = [current]
    while visited:
        current = visited[-1]
        next = maze.select_neighbor(current)
        if next:
            visited.append(next)
            next.visited = True
            maze.RemoveWalls(current, next)
        else:
            visited.pop()


def open_more_cells(grid: list[Cell], maze: Grid) -> None:
    for cell in grid:
        if cell.visited and cell not in maze.cells_42:
            cell.late_visited = False

    for cell in grid:
        if cell not in maze.cells_42:
            neighbors = maze.get_neighbors(cell)
            if neighbors:
                for neighbor in neighbors:
                    if not maze.CheckWalls(cell, neighbor):
                        if cell.count_walls() == 3:
                            maze.RemoveWalls(cell, neighbor)
                            break


def init_42(maze: Grid):
    if maze.width >= 9 and maze.height >= 7:
        mid = 0
        for cell in maze.grid:
            if cell.position == (maze.height // 2, maze.width // 2):
                mid = maze.grid.index(cell)
                if maze.height == 7 and maze.width == 9:
                    mid = mid - maze.width + 1
                break
        maze.grid[mid - 1].visited = True
        maze.grid[mid - 2].visited = True
        maze.grid[mid - 3].visited = True
        maze.grid[mid - maze.width - 3].visited = True
        maze.grid[mid - maze.width - maze.width - 3].visited = True
        maze.grid[mid + maze.width - 1].visited = True
        maze.grid[mid + maze.width + maze.width - 1].visited = True
        maze.grid[mid - maze.width + 3].visited = True
        maze.grid[mid + 1].visited = True
        maze.grid[mid + 2].visited = True
        maze.grid[mid + 3].visited = True
        maze.grid[mid + maze.width + maze.width + 1].visited = True
        maze.grid[mid + maze.width + maze.width + 2].visited = True
        maze.grid[mid + maze.width + maze.width + 3].visited = True
        maze.grid[mid + maze.width + 1].visited = True
        maze.grid[mid - maze.width - maze.width + 1].visited = True
        maze.grid[mid - maze.width - maze.width + 2].visited = True
        maze.grid[mid - maze.width - maze.width + 3].visited = True
        for cell in maze.grid:
            if cell.visited:
                cell.late_visited = True
                maze.cells_42.append(cell)
