def parse_input():
    lines = []
    while True:
        try:
            lines.append(input().strip())
        except EOFError:
            break

    return lines


def extract_ingredients(lines):
    fresh_ingredients = []
    ingredients_list = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if line == "":
            break
        fresh_ingredients.append(tuple(map(int, line.split('-'))))
        #fresh_ingredients.append(list(line.split('-')))
        i += 1

    i += 1
    while i < len(lines):
        line = lines[i]
        ingredients_list.append(int(line))
        i += 1

    return fresh_ingredients, ingredients_list


def solve_part_1(fresh_ingredients, ingredients):
    count = 0
    i = 0
    j = 0
    while i < len(ingredients):
        while j < len(fresh_ingredients):
            if ingredients[i] >= fresh_ingredients[j][0] and ingredients[i] <= fresh_ingredients[j][1]:
                count += 1
                break
            elif ingredients[i] < fresh_ingredients[j][0]:
                break
            j += 1
        i += 1
    return count


def solve_part_2(fresh_ingredients):

    count = 0
    curr_ingredient = fresh_ingredients[0][0] - 1

    for i in range(len(fresh_ingredients)):
        if curr_ingredient > fresh_ingredients[i][1]:
            continue
        curr_ingredient = max(curr_ingredient, fresh_ingredients[i][0])
        count += fresh_ingredients[i][1] - curr_ingredient + 1
        curr_ingredient = fresh_ingredients[i][1] + 1

    return count


if __name__ == "__main__":
    print("AOC 2025 Day 5 🎄")
    lines = parse_input()

    fresh_ingredients, ingredients = extract_ingredients(lines)
    fresh_ingredients.sort()
    ingredients.sort()

    #print(grid)
    print("Part 1 Answer:", solve_part_1(fresh_ingredients, ingredients))
    print("Part 2 Answer:", solve_part_2(fresh_ingredients))
