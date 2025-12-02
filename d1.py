
def parse_input():
    lines = []
    while True:
        try:
            lines.append(input().strip())
        except EOFError:
            break
    return lines


def solve(moves, start=50, method=None):

    dial_position = start
    TOTAL_POS = 100
    START_POS = 0
    END_POS = 99
    password = 0

    for m in moves:

        try:
            change = int(m[1:])
        except ValueError:
            raise ValueError("Cannot find move value!")
        if m[0] == "R":
            pass
        elif m[0] == "L":
            change = -change
        else:
            raise ValueError("Unknown move direction. Must be L or R.")
        
        if method == "0x434C49434B":
            # Count full rotations
            password += abs(change) // TOTAL_POS

            # Check cross of zero when starting from non zero position
            if dial_position != 0:
                if change > 0:
                    if dial_position + (change % TOTAL_POS) > END_POS:
                        password += 1
                else:
                    if dial_position -(abs(change) % TOTAL_POS) <= START_POS:
                        password += 1
            
            dial_position = (dial_position + change) % TOTAL_POS

        else:
            dial_position = (dial_position + change) % TOTAL_POS
        
            if dial_position == 0:
                password += 1 

    return password

def solve_part_1(moves):
    return solve(moves=moves)

def solve_part_2(moves):
    return solve(moves=moves, method="0x434C49434B")

if __name__ == "__main__":
    print("AOC 2025 Day 1 🎄")
    moves = parse_input()
    print("Part 1 Answer:", solve_part_1(moves=moves))
    print("Part 2 Answer:", solve_part_2(moves=moves))


