def parse_input():
    lines = []
    while True:
        try:
            lines.append(input().strip())
        except EOFError:
            break

    lines = lines[0].split(",")
    for i in range(len(lines)):
        lines[i] = lines[i].split("-")
    return lines

def is_invalid_1(id):    
    mid = len(id) >> 1 # Divide by 2 using bitshift
    if id[:mid] == id[mid:]:
        return True
    return False

def is_invalid_2(id):
    for i in range(len(id)//2):
        pattern = id[:i+1]
        num_repetitions = len(id) // len(pattern)
        if pattern * num_repetitions == id:
            return True
    return False

def solve_part_1(ids):
    invalid_sum = 0
    
    for id_range in ids:
        number_range = range(int(id_range[0]), int(id_range[1]) + 1) 
        invalid_sum += sum([num for num in number_range if is_invalid_1(str(num))])
    return invalid_sum

def solve_part_2(ids):
    invalid_sum = 0
    
    for id_range in ids:
        number_range = range(int(id_range[0]), int(id_range[1]) + 1) 
        invalid_sum += sum([num for num in number_range if is_invalid_2(str(num))])
    return invalid_sum

if __name__ == "__main__":
    print("AOC 2025 Day 2 🎄")
    id_ranges = parse_input()
    print("Part 1 Answer:", solve_part_1(ids = id_ranges))
    print("Part 2 Answer:", solve_part_2(ids = id_ranges))
    