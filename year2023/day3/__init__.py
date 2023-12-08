import helpers

import math as m, re

board = list(open('year2023/day3/input.txt'))
chars = {(r, c): [] for r in range(140) for c in range(140)
                    if board[r][c] not in '01234566789.'}

for r, row in enumerate(board):
    for n in re.finditer(r'\d+', row):
        edge = {(r, c) for r in (r-1, r, r+1)
                       for c in range(n.start()-1, n.end()+1)}

        for o in edge & chars.keys():
            chars[o].append(int(n.group()))


print(sum(sum(p)    for p in chars.values()),
      sum(m.prod(p) for p in chars.values() if len(p)==2))

def run():
    with open("year2023/day3/input.txt", "r") as f:
        full_string = f.read()

    lines = full_string.splitlines()

    print("--- PART 1 ---")
    print("Sum of all part numbers ")
    print(part1(lines))
    print("--- PART 2 ---")
    print("")
    print(part2(lines))


# answer = 535351
def part1(lines):
    valid_part_indexes = set()
    # create all indexes that are valid
    for row_index, line in enumerate(lines):
        for col_index, character in enumerate(line):
            if character in '[@#$%&*/+_-=':
                for new_index in get_all_valid_indexes(row_index, col_index):
                    valid_part_indexes.add(new_index)

    all_parts = []
    running_total = 0
    for row_index, line in enumerate(lines):
        current_part = {
            'str_value': '',
            'is_valid_part_num': False,
        }
        for col_index, character in enumerate(line):

            if (current_part['str_value'] != '' or character.isnumeric()) and (row_index, col_index) in valid_part_indexes:
                current_part['is_valid_part_num'] = True

            if character.isnumeric():
                current_part['str_value'] += character
            elif current_part['str_value'] != '':
                all_parts.append(current_part)
                if current_part['is_valid_part_num']:
                    running_total += int(current_part['str_value'])
                current_part = {
                    'str_value': '',
                    'is_valid_part_num': False,
                }

            col_index += 1
        if current_part['str_value'] != '':
            if current_part['is_valid_part_num']:
                running_total += int(current_part['str_value'])
            all_parts.append(current_part)

    # print(all_parts)
    return running_total


# answer = TODO
def part2(lines):

    return 0


def get_all_valid_indexes(row_index, col_index):
    indexes = []
    x = row_index
    y = col_index

    indexes.append((x - 1, y - 1))  # topLeft
    indexes.append((x, y - 1))  # top
    indexes.append((x + 1, y - 1))  # topRight

    indexes.append((x - 1, y))  # midLeft
    indexes.append((x + 1, y))  # midRight

    indexes.append((x - 1, y + 1))  # botLeft
    indexes.append((x, y + 1))  # bot
    indexes.append((x + 1, y + 1))  # botRight

    if (4, 102) in indexes:
        pass
    return indexes