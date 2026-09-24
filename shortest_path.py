from cell import Cell
from grid import Grid


def bfs(start: Cell, goal: Cell, maze: Grid) -> list[Cell] | None:
    """
    Find the shortest path between two cells using breadth-first search.

    Args:
        start: The cell where the search begins.
        goal: The target cell to reach.
        maze: The maze containing the cells and their connections.

    Returns:
        A list of cells representing the shortest path from start to goal,
        or None if the goal cannot be reached.
    """
    queue = []
    queue.append(start)
    start.late_visited = True

    while len(queue):
        current = queue.pop(0)

        if current == goal:
            break

        neighbors = maze.get_neighbors(current)
        if neighbors:
            for neighbor in neighbors:
                if neighbor.late_visited is False:
                    if maze.CheckWalls(current, neighbor):
                        neighbor.late_visited = True
                        neighbor.parent = current
                        queue.append(neighbor)
    if goal.late_visited is False:
        return None

    path = []
    current = goal
    while current != start:
        path.append(current)
        current = current.parent

    path.append(start)
    return path[::-1]


def path_direction(path: list[Cell]) -> str:
    """
    Convert a cell path into movement directions.

    Args:
        path: An ordered list of cells representing a path through the maze.

    Returns:
        A string containing the movement directions:
        N for north, S for south, E for east, and W for west.
    """
    directions = ""
    counter = 0
    length = len(path)
    while counter + 1 < length:
        if path[counter].position[0] == path[counter + 1].position[0]:
            if (
                path[counter].position[1] > path[counter + 1].position[1]
            ):
                directions += "W"
            else:
                directions += "E"
        else:
            if path[counter].position[0] > path[counter + 1].position[0]:
                directions += "N"
            else:
                directions += "S"
        counter += 1
    return directions
