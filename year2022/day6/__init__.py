def day6():
    f = open("year2022/day6/input.txt", "r")
    lines = []
    for x in f:
        lines.append(x.strip())

    print("--- PART 1 ---")
    print(part1(lines[0]))
    print("--- PART 2 ---")
    print(part2(lines[0]))


# answer = 1707
def part1(line):
    history = []
    for index, char in enumerate(line):
        if len(history) < 4:
            history.append(char)
        else:
            # remove the first, then append
            history.pop(0)
            history.append(char)

        if len(history) == 4:
            if len(set(history)) == len(history):
                return index + 1


# answer = 3697
def part2(line):
    history = []
    for index, char in enumerate(line):
        if len(history) < 14:
            history.append(char)
        else:
            # remove the first, then append
            history.pop(0)
            history.append(char)

        if len(history) == 14:
            if len(set(history)) == len(history):
                return index + 1
