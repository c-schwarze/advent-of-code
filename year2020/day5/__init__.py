def day5():
    with open("year2020/day5/input.txt", "r") as f:
        full_array = f.read().splitlines()

    print('Part 1 - Highest Seat ID:')
    print(part1(full_array))
    print('Part 2 - TODO')
    print(part2(full_array))


# answer = 838
def part1(full_array):
    highest_seat_id = 0
    seat_ids = convert_to_seat_ids(full_array)

    for seat_id in seat_ids:
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
    return highest_seat_id


# answer = 714
def part2(full_array):
    seat_ids = convert_to_seat_ids(full_array)
    seat_ids.sort()

    found_seats = False
    for i in range(0, 127):
        for j in range(0, 7):
            a_real_seat = (i*8)+j
            if a_real_seat in seat_ids:
                found_seats = True
            if found_seats:
                if a_real_seat not in seat_ids:
                    return a_real_seat

    return 'none found'


def convert_to_seat_ids(full_array):
    seat_ids = []
    for line in full_array:
        binary_line = line.replace('B', '1').replace('F', '0').replace('R', '1').replace('L', '0')
        first_part = binary_line[:7]
        second_part = binary_line[7:]
        new_seat_id = (count_binary(first_part, 64) * 8) + count_binary(second_part, 4)
        seat_ids.append(new_seat_id)
    return seat_ids


def count_binary(binary_string, multiply_start):
    total = 0
    for num in binary_string:
        total += multiply_start * int(num)
        multiply_start = multiply_start/2

    return int(total)
