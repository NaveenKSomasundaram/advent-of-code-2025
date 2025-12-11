def parse_input():
    lines = []
    while True:
        try:
            lines.append(input().strip())
        except EOFError:
            break
    return lines

def get_connectivity_map(lines):
    connectivity_map = {}
    for l in lines:
        parent, children = l.split(": ")
        children = children.split(" ")
        if parent not in connectivity_map:
            connectivity_map[parent] = set()    
        for child in children:
            connectivity_map[parent].add(child)
    return connectivity_map

class Graph(object):
    def __init__(self, connectivity_map):
        self.edges = {}
        self.connectivity_map = connectivity_map
        self.count_paths_cache = {}



    def count_paths(self, start, end, visited=None):

        if (start, end) in self.count_paths_cache:
            return self.count_paths_cache[(start, end)]

        if visited is None:
            visited = set()

        if start == end:
            return 1

        visited.add(start)
        path_count = 0

        for neighbor in self.connectivity_map.get(start, []):
            if neighbor not in visited:
                path_count += self.count_paths(neighbor, end, visited)

        visited.remove(start)

        self.count_paths_cache[(start, end)] = path_count

        return path_count

def solve_part_1(graph):

    return graph.count_paths("you", "out")
    
def solve_part_2(graph):

    num_paths_1 = graph.count_paths("svr", "fft")
    num_paths_2 = graph.count_paths("fft", "dac")
    num_paths_3 = graph.count_paths("dac", "out")
    num_paths_4 = graph.count_paths("svr", "dac")
    num_paths_5 = graph.count_paths("dac", "fft")
    num_paths_6 = graph.count_paths("fft", "out")

    num_paths = (num_paths_1 * num_paths_2 * num_paths_3) + (num_paths_4 * num_paths_5 * num_paths_6)

    return num_paths

if __name__ == "__main__":
    print("AOC 2025 Day 11")
    lines = parse_input()

    graph = Graph(connectivity_map=get_connectivity_map(lines))

    print("Part 1 Answer:", solve_part_1(graph))

    print("Part 2 Answer:", solve_part_2(graph))
    