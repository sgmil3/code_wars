"""
Name: Escape the maze
Link: https://www.codewars.com/kata/5877027d885d4f6144000404
Level: 4kyu
Desc.: Escape from a 2D maze by provided  rotation and forward directions in sequence
Finished: Yes
"""

import heapq


class Cell(object):
    def __init__(self, x: int, y: int, reachable: bool):
        self.reachable = reachable
        self.x = x
        self.y = y
        self.parent: "Cell" | None = None
        self.g = 0
        self.h = 0
        self.f = 0

    # def __eq__(self, other: "Cell"):
    #     return self.x == other.x and self.y == other.y

    def __lt__(self, other: "Cell"):
        return self.f < other.f

    def __repr__(self):
        return "#" if not self.reachable else "."


class AStar(object):
    def __init__(self, maze: list[list[int]]):
        self.opened = []
        heapq.heapify(self.opened)
        self.closed = set()
        self.cells = []
        *self.start, self.orientation = self.get_loc(maze)
        self.ends = self.find_all_exits(maze)
        self.init_grid(maze)
        self.start = self.get_cell(*self.start)
        self.current = self.start

    def __repr__(self):
        # print indexes
        print("  " + "".join(str(i) for i in range(len(self.cells[0]))))
        for i, row in enumerate(self.cells):
            print(
                f"{i}",
                "".join(
                    [
                        (
                            str(cell)
                            if cell != self.current
                            else [">", "<", "^", "v"][self.orientation]
                        )
                        for cell in row
                    ]
                ),
            )
        return ""

    def get_loc(self, maze: list) -> tuple[int, int, int]:
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] in (pos := [">", "<", "^", "v"]):
                    return i, j, pos.index(maze[i][j])

    def convert_to_one_zero_grid(self, maze: list) -> list[list[int]]:
        return [[1 if c == "#" else 0 for c in row] for row in maze]

    def init_grid(self, grid: list[list[int]]):
        new_grid = self.convert_to_one_zero_grid(grid)
        for i in range(len(grid)):
            self.cells.append(
                [Cell(i, j, new_grid[i][j] == 0) for j in range(len(grid[0]))]
            )

    def find_all_exits(self, maze: list) -> list[tuple[int, int]]:
        exits = []
        heapq.heapify(exits)
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == " ":
                    if i == 0 or i == len(maze) - 1 or j == 0 or j == len(maze[0]) - 1:
                        # add to heap by lowest distance to start
                        heapq.heappush(
                            exits,
                            (abs(i - self.start[0]) + abs(j - self.start[1]), (i, j)),
                        )

        return exits

    def get_heuristic(self, cell: Cell) -> int:
        return 10 * abs(cell.x - self.end.x) + 10 * abs(cell.y - self.end.y)

    def get_cell(self, x: int, y: int) -> Cell:
        return self.cells[x][y]

    def get_adjacent_cells(self, cell: Cell) -> list[Cell]:
        cells = []
        if cell.x < len(self.cells) - 1:
            cells.append(self.cells[cell.x + 1][cell.y])
        if cell.y > 0:
            cells.append(self.cells[cell.x][cell.y - 1])
        if cell.x > 0:
            cells.append(self.cells[cell.x - 1][cell.y])
        if cell.y < len(self.cells[0]) - 1:
            cells.append(self.cells[cell.x][cell.y + 1])
        return cells

    def display_path(self):
        cell = self.end
        while cell.parent is not self.start:
            cell = cell.parent
            yield (cell.x, cell.y)

    def update_cell(self, adj: Cell, cell: Cell):
        adj.g = cell.g + 10
        adj.h = self.get_heuristic(adj)
        adj.parent = cell
        adj.f = adj.h + adj.g

    def solve(self):
        while self.ends:
            self.opened = []
            heapq.heapify(self.opened)
            self.closed = set()
            heapq.heappush(self.opened, (self.start.f, self.start))
            self.end = self.get_cell(*heapq.heappop(self.ends)[1])
            while len(self.opened):
                _, cell = heapq.heappop(self.opened)
                self.closed.add(cell)
                if cell == self.end:
                    self.end = cell
                    return self.display_path()
                adj_cells = self.get_adjacent_cells(cell)
                for adj_cell in adj_cells:
                    if adj_cell.reachable and adj_cell not in self.closed:
                        if (adj_cell.f, adj_cell) in self.opened:
                            if adj_cell.g > cell.g + 10:
                                self.update_cell(adj_cell, cell)
                        else:
                            self.update_cell(adj_cell, cell)
                            heapq.heappush(self.opened, (adj_cell.f, adj_cell))
        else:
            return []

    def convert_to_moves(self, path: list[tuple[int, int]]) -> list[str]:
        if path == []:
            return []
        # reconstruct moves by following path in reverse,
        # start off by getting which way the exit is (edge of maze)
        moves = []
        path = (
            [(self.start.x, self.start.y)]
            + list(path)[::-1]
            + [(self.end.x, self.end.y)]
        )

        for i, (x, y) in enumerate(path[1:]):
            if path[i][0] == x:
                if path[i][1] < y:
                    if self.orientation == 0:
                        moves.append("F")
                    elif self.orientation == 1:
                        moves.append("BF")
                    elif self.orientation == 2:
                        moves.append("RF")
                    else:
                        moves.append("LF")

                    self.orientation = 0

                else:
                    if self.orientation == 0:
                        moves.append("BF")

                    elif self.orientation == 1:
                        moves.append("F")

                    elif self.orientation == 2:
                        moves.append("LF")

                    else:
                        moves.append("RF")

                    self.orientation = 1
            else:
                if path[i][0] > x:
                    if self.orientation == 0:
                        moves.append("LF")
                    elif self.orientation == 1:
                        moves.append("RF")
                    elif self.orientation == 2:
                        moves.append("F")
                    else:
                        moves.append("BF")

                    self.orientation = 2

                else:
                    if self.orientation == 0:
                        moves.append("RF")
                    elif self.orientation == 1:
                        moves.append("LF")
                    elif self.orientation == 2:
                        moves.append("BF")
                    else:
                        moves.append("F")

                    self.orientation = 3

            self.current = self.get_cell(x, y)

        moves.append("F")

        return list("".join(moves))


def escape(maze):
    print(maze)
    Maze = AStar(maze)
    print("Start: ", (Maze.start.x, Maze.start.y))
    print("Solving:")
    return Maze.convert_to_moves(Maze.solve())


if __name__ == "__main__":
    basic_mazes = []

    # Add your own tests in these!
    your_valid_mazes = []
    your_invalid_mazes = []

    basic_mazes.append(
        [
            "##########",
            "#        #",
            "#  ##### #",
            "#  #   # #",
            "#  #^# # #",
            "#  ### # #",
            "#      # #",
            "######## #",
        ]
    )

    for i, maze in enumerate(basic_mazes):
        print()
        print(f"Maze {i}:")
        print(escape(maze))
