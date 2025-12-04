def parse_input():
    lines = []
    while True:
        try:
            lines.append(input().strip())
        except EOFError:
            break
    
    lines =[list(line) for line in lines]

    return lines

def is_paper_roll(grid, i, j):
    if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0]):
        return grid[i][j] == "@"
    return False

def count_neighbours(grid, i, j):
    search_steps = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
    return sum([1 for step in search_steps if is_paper_roll(grid, i + step[0], j + step[1])])

def is_liftable(grid, i, j):
    return is_paper_roll(grid, i, j) and count_neighbours(grid, i, j) < 4

def remove_paper_rolls(grid):
    # Remove paper rolls from grid using problem 2 logic
    nodes = set()
    for i in range(len(grid)):
        for j in range(len(grid)):
            if is_liftable(grid, i, j):
                nodes.add((i, j))
    
    while len(nodes) > 0:
        node = nodes.pop()
        i, j = node
        if is_liftable(grid, node[0], node[1]):
            grid[i][j] = "." # Lift paper roll
        else:
            continue
        search_steps = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        for step in search_steps:
            if is_liftable(grid, i + step[0], j + step[1]):
                nodes.add((i + step[0], j + step[1]))
    return grid

def solve_part_1(grid):
    liftable_rolls = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if is_liftable(grid, i, j):
                liftable_rolls += 1
    return liftable_rolls

def count_removable_rolls(grid):

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if is_paper_roll(grid, i, j):
                count += 1
    return count 

def solve_part_2(grid):

    old_count = count_removable_rolls(grid)

    grid = remove_paper_rolls(grid)
    
    new_count = count_removable_rolls(grid)

    return old_count - new_count

if __name__ == "__main__":
    print("AOC 2025 Day 4 🎄")
    grid = parse_input()
    #print(grid)
    print("Part 1 Answer:", solve_part_1(grid))
    #print(count_neighbours(grid, 0, 0))
    print("Part 2 Answer:", solve_part_2(grid))
    