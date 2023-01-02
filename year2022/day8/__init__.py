def run():
    # UPDATE THIS LINE
    f = open("year2022/day8/input.txt", "r")
    lines = []
    for x in f:
        current_line = []
        line = x.strip()
        for char in line:
            current_line.append(char)
        lines.append(current_line)

    print("--- PART 1 ---")
    print("Visible trees: ")
    print(part1(lines))
    print("--- PART 2 ---")
    print("Title 2: ")
    print(part2(lines))


# answer = 1763
def part1(lines):
    total_trees = 0
    for i, row in enumerate(lines):
        for j, tree in enumerate(row):
            # check for visibility on edges
            if i == 0 or i == len(lines) - 1 or j == 0 or j == len(row) - 1:
                total_trees += 1
                continue

            # check for visibility inside
            # try each direction
            # NORTH
            count_tree = True
            modifier = 1
            while i - modifier >= 0:
                check_tree = lines[i - modifier][j]
                if tree <= check_tree:
                    count_tree = False
                    break
                modifier += 1
            if count_tree:
                total_trees += 1
                continue

            # SOUTH
            count_tree = True
            modifier = 1
            while i + modifier < len(lines):
                check_tree = lines[i + modifier][j]
                if tree <= check_tree:
                    count_tree = False
                    break
                modifier += 1
            if count_tree:
                total_trees += 1
                continue

            # WEST
            count_tree = True
            modifier = 1
            while j - modifier >= 0:
                check_tree = lines[i][j - modifier]
                if tree <= check_tree:
                    count_tree = False
                    break
                modifier += 1
            if count_tree:
                total_trees += 1
                continue

            # EAST
            count_tree = True
            modifier = 1
            while j + modifier < len(lines[i]):
                check_tree = lines[i][j + modifier]
                if tree <= check_tree:
                    count_tree = False
                    break
                modifier += 1
            if count_tree:
                total_trees += 1
                continue

    return total_trees


# answer = 671160
def part2(lines):
    best_viewing_score = 0
    for i, row in enumerate(lines):
        for j, tree in enumerate(row):
            # check for visibility inside
            # try each direction
            # NORTH
            count_tree = True
            modifier = 1
            while i - modifier >= 0:
                check_tree = lines[i - modifier][j]
                if tree <= check_tree:
                    modifier += 1 # to fix the amount later
                    break
                modifier += 1
            north_amount = modifier - 1

            # SOUTH
            count_tree = True
            modifier = 1
            while i + modifier < len(lines):
                check_tree = lines[i + modifier][j]
                if tree <= check_tree:
                    modifier += 1 # to fix the amount later
                    break
                modifier += 1
            south_amount = modifier - 1

            # WEST
            count_tree = True
            modifier = 1
            while j - modifier >= 0:
                check_tree = lines[i][j - modifier]
                if tree <= check_tree:
                    modifier += 1 # to fix the amount later
                    break
                modifier += 1
            west_amount = modifier - 1

            # EAST
            count_tree = True
            modifier = 1
            while j + modifier < len(lines[i]):
                check_tree = lines[i][j + modifier]
                if tree <= check_tree:
                    modifier += 1 # to fix the amount later
                    break
                modifier += 1
            east_amount = modifier - 1

            tree_score = north_amount * south_amount * west_amount * east_amount
            if tree_score > best_viewing_score:
                best_viewing_score = tree_score

    return best_viewing_score
