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

def get_edges(coords):
    edges = []
    for i in range(len(coords) - 1):
        for j in range(i+1, len(coords)):
            distance = sum([(coords[i][k] - coords[j][k])**2 for k in range(3)])
            distance = distance ** 0.5
            edges.append((distance, i, j))
    edges.sort()
    return edges

class DSU():

    def __init__(self,num_v):
        self.num_v = num_v
        self.parent = [i for i in range(num_v)]
        self.size = [1] * num_v
        self.max_size = 1
    
    def find_set(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find_set(self.parent[v])
        return self.parent[v]

    def set_union(self, v1, v2):
        v1 = self.find_set(v1)
        v2 = self.find_set(v2)
        if v1 != v2:
            if self.size[v1] < self.size[v2]:
                v1, v2 = v2, v1
            self.parent[v2] = v1
            self.size[v1] += self.size[v2]
        if self.size[v1] > self.max_size:
            self.max_size = self.size[v1]
        return 0

    def get_set_lengths(self):
        set_lengths = []
        for v in range(self.num_v):
            if v == self.parent[v]:
                set_lengths.append(self.size[v])
        set_lengths.sort(reverse=True)
        return set_lengths
    
    def is_fully_connected(self):
        return self.max_size >= self.num_v
 
def solve_part_1(coords, edges):

    num_e = len(edges)
    num_v = len(coords)
    
    dsu_obj = DSU(num_v)
    
    NUM_CONNECTIONS_ALLOWED = 1000

    # Create connectivity graph
    for ind in range(num_e):
        i = edges[ind][1]
        j = edges[ind][2]
        dsu_obj.set_union(i, j)

        if ind + 1 >= NUM_CONNECTIONS_ALLOWED:
            break

    set_lengths = dsu_obj.get_set_lengths()[0:3]        
    ans = set_lengths[0] * set_lengths[1] * set_lengths[2]
    return ans   
        
def solve_part_2(coords, edges):
    
    dsu_object = DSU(len(coords))

    for e in edges:
        i = e[1]
        j = e[2]
        dsu_object.set_union(i, j)

        if dsu_object.is_fully_connected():
            return coords[i][0] * coords[j][0]

    return None   

if __name__ == "__main__":
    print("AOC 2025 Day 8 🎄")
    coords = parse_input()
    edges = get_edges(coords)
    #print(coords)
    print("Part 1 Answer:", solve_part_1(coords, edges))
    #print(count_neighbours(grid, 0, 0))
    print("Part 2 Answer:", solve_part_2(coords, edges))
    