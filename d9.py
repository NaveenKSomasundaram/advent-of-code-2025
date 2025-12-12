from collections import Counter

def parse_input():
    lines = []
    while True:
        try:
            lines.append(input().strip())
        except EOFError:
            break
    
    lines =[tuple(map(int, line.split(','))) for line in lines]

    return lines

class GRID():

    def __init__(self,red_locs):
        
        self.red_locs = red_locs
        
        self.grid = []
        
        self.unique_i = set()
        self.unique_j = set()
        for i in range(len(self.red_locs)-1):
            self.unique_i.add(self.red_locs[i][1])
            self.unique_j.add(self.red_locs[i][0])
            self.unique_i.add(self.red_locs[i][1]-1)
            self.unique_j.add(self.red_locs[i][0]-1)
            self.unique_i.add(self.red_locs[i][1]+1)
            self.unique_j.add(self.red_locs[i][0]+1)
            
        self.unique_i = list(self.unique_i)
        self.unique_i.sort()
        self.unique_j = list(self.unique_j)
        self.unique_j.sort()

        self.i_map = dict()
        self.j_map = dict()
        count = 0
        for i in self.unique_i:
            self.i_map[i] = count
            count += 1
        count = 0
        for j in self.unique_j:
            self.j_map[j] = count
            count += 1

        self.grid = []
        for _ in range(len(self.i_map)):
            self.grid.append([" "] * len(self.j_map))
        
        for i in range(len(self.red_locs)):
            j = (i + 1) % len(self.red_locs)
            self.draw_line_in_grid(self.red_locs[i][1], self.red_locs[i][0], self.red_locs[j][1], self.red_locs[j][0])

        self.fill_interior_of_grid()

    def fill_interior_of_grid(self):
        n_rows = len(self.grid) 
        n_cols = len(self.grid[0])

        nodes = [(n_rows // 2, n_cols // 2 )] # Flood fill lucky guess
        # FIX ME Implement a fool proof start

        while len(nodes) > 0:
 
            i, j = nodes.pop()
            
            
            if self.grid[i][j] != " ":
                continue
            if i > 0 and self.grid[i - 1][j] == " ":
                nodes.append((i - 1, j))
            if i  + 1 < n_rows and self.grid[i + 1][j] == " ":
                nodes.append((i + 1, j))
            if j> 0 and self.grid[i][j-1] == " ":
                nodes.append((i, j - 1))
            if j  + 1 < n_cols and self.grid[i][j + 1] == " ":
                nodes.append((i, j + 1))
            self.grid[i][j] = "X"
    
    def print_grid(self):
        for l in self.grid:
            print("".join(l))
    
    def draw_line_in_grid(self, i1, j1, i2, j2):
        
        i1 = self.i_map[i1]
        j1 = self.j_map[j1]
        i2 = self.i_map[i2]
        j2 = self.j_map[j2]
        self.grid[i1][j1] = "#"
        self.grid[i2][j2] = "#"
        if i1 ==  i2:
            if j1 > j2:
                j1, j2  = j2, j1
            while j1 + 1 != j2:
                j1 += 1
                self.grid[i1][j1] = "X"
        elif j1 == j2:
            if i1 > i2:
                i1, i2  = i2, i1
            while i1 + 1 != i2:
                i1 += 1
                self.grid[i1][j1] = "X"
        else:
            print(i1, j1, i2, j2)
            raise ValueError()

    def is_tiled_square(self, i1, j1, i2, j2):
        i1 = self.i_map[i1]
        i2 = self.i_map[i2]
        j1 = self.j_map[j1]
        j2 = self.j_map[j2]
        if i1 > i2:
            i1, i2 = i2, i1
        if j1 > j2:
            j1, j2 = j2, j1
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                if self.grid[i][j] == " ":
                    return False
        return True

def get_area(c1, c2):
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1) 

def solve_part_1(coords):

    n_coords = len(coords)
    max_area = 0
    for i in range(n_coords - 1):
        for j in range(i + 1, n_coords):
            curr_area = get_area(coords[i], coords[j])
            if curr_area > max_area:
                max_area = curr_area
    return max_area  
        
def solve_part_2(coords):
    max_area = 0
    n_coords =  len(coords)

    # FIX ME ... Complicated approach ... may work better if switched to line intersections check
    grid = GRID(coords)
    #grid.print_grid()
    for i in range(n_coords - 1):
        for j in range(i + 1, n_coords):
            curr_area = get_area(coords[i], coords[j])
            if curr_area > max_area:
                if grid.is_tiled_square(coords[i][1], coords[i][0], coords[j][1], coords[j][0]):
                    max_area = curr_area
    return max_area  

if __name__ == "__main__":
    print("AOC 2025 Day 9")
    coords = parse_input()
    
    print("Part 1 Answer:", solve_part_1(coords))

    print("Part 2 Answer:", solve_part_2(coords))
    