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

    return lines

def process_lines(lines):

    transformed_lines = []
    for line in lines:
       transformed_lines.append(re.split(r'\s+', line.strip()))
    transformed_lines = [list(row) for row in zip(*transformed_lines)]
    return transformed_lines

def process_lines_2(lines):

    transformed_lines = []
    transformed_row = []

    j = len(lines[0])-1
    while j >= 0:
        curr_num = ""
        for i in range(len(lines)-1):
            if lines[i][j] != " ":
                curr_num += lines[i][j]

        if curr_num != "":
            transformed_row.append(curr_num)

        if lines[i+1][j] == "+" or lines[i+1][j] == "*":
            transformed_row.append(lines[i+1][j])
            transformed_lines.append(transformed_row)
            transformed_row = []

        j -= 1

    return transformed_lines

def solve_part_1(lines):

    transformed_lines = process_lines(lines)
    count = 0
    for row in transformed_lines:
        if row[-1] == "+":
            curr_count = 0
            for num in row[:len(row) - 1]:
                curr_count += int(num)
            count += curr_count
        else:
            curr_count = 1
            for num in row[:len(row) - 1]:
                curr_count *= int(num)
            count += curr_count

    return count

def solve_part_2(lines):

    transformed_lines = process_lines_2(lines)
    #for l in transformed_lines:
    #    print(l)
    count = 0
    for row in transformed_lines:
        if row[-1] == "+":
            curr_count = 0
            for num in row[:len(row) - 1]:
                curr_count += int(num)
            count += curr_count
        else:
            curr_count = 1
            for num in row[:len(row) - 1]:
                curr_count *= int(num)
            count += curr_count

    return count

if __name__ == "__main__":
    print("AOC 2025 Day 6 🎄")
    lines = parse_input()
    print("Part 1 Answer:", solve_part_1(lines))
    print("Part 2 Answer:", solve_part_2(lines))

