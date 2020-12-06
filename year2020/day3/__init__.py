def day3():
    full_array = []
    with open("year2020/day3/input.txt", "r") as f:
        full_array = f.read().splitlines()

    print(part1(full_array))
    print(part2(full_array))


# answer = 178
def part1(full_array):
    return check_trees_hit(full_array, 3, 1)


# answer = 3492520200
def part2(full_array):
    a = check_trees_hit(full_array, 1, 1)
    b = check_trees_hit(full_array, 3, 1)
    c = check_trees_hit(full_array, 5, 1)
    d = check_trees_hit(full_array, 7, 1)
    e = check_trees_hit(full_array, 1, 2)
    return a*b*c*d*e


def check_trees_hit(full_array, horizontal_increment, vertical_increment):
    horizontal = 0
    vertical = 0
    count_trees = 0
    while vertical < len(full_array):
        if full_array[vertical][horizontal] == '#':
            count_trees += 1

        horizontal = (horizontal + horizontal_increment)%len(full_array[0])
        vertical += vertical_increment

    return count_trees
