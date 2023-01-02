def day4():
    f = open("year2022/day4/input.txt", "r")
    lines = []
    for x in f:
        lines.append(x.strip().split(','))

    print("--- PART 1 ---")
    print("Title 1: ")
    print(part1(lines))
    print("--- PART 2 ---")
    print("Title 2: ")
    print(part2(lines))


# answer = 487
def part1(lines):
    count = 0
    for line in lines:
        first_elf = line[0]
        start1, end1 = first_elf.split('-')
        first_elf_area = [*range(int(start1), int(end1)+1, 1)]

        second_elf = line[1]
        start2, end2 = second_elf.split('-')
        second_elf_area = [*range(int(start2), int(end2)+1, 1)]

        check1 = all(item in first_elf_area for item in second_elf_area)
        check2 = all(item in second_elf_area for item in first_elf_area)

        if check1 or check2:
            count += 1

    return count


# answer = 849
def part2(lines):
    count = 0
    for line in lines:
        first_elf = line[0]
        start1, end1 = first_elf.split('-')
        first_elf_area = [*range(int(start1), int(end1) + 1, 1)]

        second_elf = line[1]
        start2, end2 = second_elf.split('-')
        second_elf_area = [*range(int(start2), int(end2) + 1, 1)]

        check1 = any(item in first_elf_area for item in second_elf_area)
        check2 = any(item in second_elf_area for item in first_elf_area)

        if check1 or check2:
            count += 1

    return count
