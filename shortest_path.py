from cell import Cell
from grid import Grid


def bfs(start: Cell, goal: Cell, maze: Grid) -> list[Cell] | None:
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
    directions = ""
    cell_counter = 0
    length = len(path)
    while cell_counter + 1 < length:
        if path[cell_counter].position[0] == path[cell_counter + 1].position[0]:
            if path[cell_counter].position[1] > path[cell_counter + 1].position[1]:
                directions += "W"
            else:
                directions += "E"
        else:
            if path[cell_counter].position[0] > path[cell_counter + 1].position[0]:
                directions += "N"
            else:
                directions += "S"
        cell_counter += 1
    return directions
