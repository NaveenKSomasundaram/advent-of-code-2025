import re
def parse_input():
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break

    row_len = max([len(l) for l in lines])

    # Pad trailing spaces
    lines = [l + " " * (row_len - len(l)) for l in lines]

    lines = [list(l) for l in lines]

    return lines

def findSource(grid):
    source = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                source.append((i, j))
    return source

def solve_part_1(grid):
    nodes = set(findSource(grid))
    n_rows = len(grid)
    n_cols = len(grid[0])
    activated_splitters = set()

    while len(nodes)>0:
        cn = nodes.pop()
        if cn[0] + 1 >= n_rows:
            continue
        elif grid[cn[0] + 1][cn[1]] == ".":
            nodes.add((cn[0] + 1, cn[1]))
        elif grid[cn[0]+1][cn[1]] == "^":
            activated_splitters.add((cn[0] + 1, cn[1]))
            if cn[1] - 1 >= 0:
                nodes.add((cn[0] + 1, cn[1] - 1))
            if cn[1] + 1 < n_cols:
                nodes.add((cn[0] + 1, cn[1] + 1))
        else:
            raise ValueError("Unknown grid item")

    return len(activated_splitters)

def solve_part_2(grid):

    n_rows = len(grid)
    n_cols = len(grid[0])

    # dict with ray node and the number of rays
    start_col = grid[0].index("S")
    paths_in_row = {(0, start_col): 1}

    for i in range(0, n_rows-1):
        paths_in_next_row = dict()
        for cn in paths_in_row :
            nn = (cn[0] + 1, cn[1])
            if grid[nn[0]][nn[1]] == ".":
                paths_in_next_row[nn] = paths_in_next_row.get(nn, 0) + paths_in_row [cn]
            if grid[nn[0]][nn[1]] == "^":
                if nn[1] - 1 >= 0:
                    nn = (cn[0] + 1, cn[1] - 1)
                    paths_in_next_row[nn] = paths_in_next_row.get(nn, 0) + paths_in_row [cn]
                if nn[1] + 1 < n_cols:
                    nn = (cn[0] + 1, cn[1] + 1)
                    paths_in_next_row[nn] = paths_in_next_row.get(nn, 0) + paths_in_row [cn]

        paths_in_row = paths_in_next_row

    return sum([paths_in_row[r] for r in paths_in_row ])

if __name__ == "__main__":
    print("AOC 2025 Day 7 🎄")
    lines = parse_input()
    print("Part 1 Answer:", solve_part_1(lines))
    print("Part 2 Answer:", solve_part_2(lines))
