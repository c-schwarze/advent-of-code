def day11():
    with open("year2020/day11/input.txt", "r") as f:
        full_array = f.read().splitlines()

    double_array = []
    for row in full_array:
        new_row = []
        for element in range(0, len(row)):
            new_row.append(row[element])
        double_array.append(new_row)

    print('Part 1 - # of occupied seats once it stabilizes')
    print(part1(double_array))
    print('Part 2 - ')
    print(part2(double_array))


# answer = 2247
def part1(double_array):
    did_seats_change = True
    while did_seats_change:
        double_array, did_seats_change = seat_iteration1(double_array)

    return count_open_seats(double_array)


# answer = 2011
def part2(double_array):
    did_seats_change = True
    while did_seats_change:
        double_array, did_seats_change = seat_iteration2(double_array)

    return count_open_seats(double_array)


def count_open_seats(full_array):
    count = 0
    for row in full_array:
        count += row.count('#')

    return count


def seat_iteration1(double_array):
    did_seats_change = False
    new_full_array = []

    for y, row in enumerate(double_array):
        new_row = []
        for x, spot in enumerate(row):
            new_spot = spot

            # get adjacent spots
            adjacent_seats = 0
            for y_modifier in [-1, 0, 1]:
                for x_modifier in [-1, 0, 1]:
                    if x_modifier == 0 and y_modifier == 0:
                        continue
                    if x+x_modifier < 0 or y+y_modifier < 0:
                        continue
                    try:
                        if double_array[y+y_modifier][x+x_modifier] == '#':
                            adjacent_seats += 1
                    except:
                        continue
            if spot == 'L' and adjacent_seats == 0:
                new_spot = '#'
                did_seats_change = True
            elif spot == '#' and adjacent_seats >= 4:
                new_spot = 'L'
                did_seats_change = True

            new_row.append(new_spot)
        new_full_array.append(new_row)

    return new_full_array, did_seats_change


def seat_iteration2(double_array):
    did_seats_change = False
    new_full_array = []

    for y, row in enumerate(double_array):
        new_row = []
        for x, spot in enumerate(row):
            new_spot = spot

            # get adjacent spots
            adjacent_seats = 0
            for y_modifier in [-1, 0, 1]:
                for x_modifier in [-1, 0, 1]:
                    new_x_modifier = x_modifier
                    new_y_modifier = y_modifier

                    if new_x_modifier == 0 and new_y_modifier == 0:
                        continue

                    keep_looking = True
                    while keep_looking:
                        if x+new_x_modifier < 0 or y+new_y_modifier < 0:
                            keep_looking = False
                            continue
                        try:
                            if double_array[y+new_y_modifier][x+new_x_modifier] == '#':
                                adjacent_seats += 1
                                keep_looking = False
                            elif double_array[y+new_y_modifier][x+new_x_modifier] == '.':
                                new_x_modifier += x_modifier
                                new_y_modifier += y_modifier
                            elif double_array[y+new_y_modifier][x+new_x_modifier] == 'L':
                                keep_looking = False
                        except:
                            keep_looking = False

            if spot == 'L' and adjacent_seats == 0:
                new_spot = '#'
                did_seats_change = True
            elif spot == '#' and adjacent_seats >= 5:
                new_spot = 'L'
                did_seats_change = True

            new_row.append(new_spot)
        new_full_array.append(new_row)

    return new_full_array, did_seats_change


def print_iteration(double_array):
    print('===================================')
    print('ANOTHER ITERATION')
    print('===================================')
    for y in double_array:
        print(''.join(y))
