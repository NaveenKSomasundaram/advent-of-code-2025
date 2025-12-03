def parse_input():
    lines = []
    while True:
        try:
            lines.append(input().strip())
        except EOFError:
            break

    for i in range(len(lines)):
        lines[i] = list(map(int, list(lines[i])))
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

def get_joltage(batteries, digits=12):
    max_joltage = [0] * digits
    for i in range(len(batteries)):
        starting_digit_position = min(digits, len(batteries) - i)
        for digit_position in range(starting_digit_position - 1, -1, -1):
            if batteries[i] > max_joltage[digit_position]:
                max_joltage[digit_position] = batteries[i]
                while digit_position-1 >= 0:
                    digit_position -= 1 
                    max_joltage[digit_position] = 0
                break
    max_joltage.reverse()
    return int("".join(map(str,max_joltage)))

def solve_part_1(lines):
    sum_joltage = 0
    return sum([get_joltage(b, 2) for b in lines])

def solve_part_2(ids):
    sum_joltage = 0
    return sum([get_joltage(b, 12) for b in lines])

if __name__ == "__main__":
    print("AOC 2025 Day 3 🎄")
    lines = parse_input()
    #print(lines)
    print("Part 1 Answer:", solve_part_1(lines))
    print("Part 2 Answer:", solve_part_2(lines))
    