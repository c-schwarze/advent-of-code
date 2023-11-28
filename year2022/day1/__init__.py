import helpers


def run():
    with open("year2022/day1/input.txt", "r") as f:
        full_string = f.read()

    lines = helpers.split_on_empty_lines(full_string)
    elves = []
    for line in lines:
        elves.append(line.replace('\n', ' ').replace('\r', '').split(' '))

    print("--- PART 1 ---")
    print("Highest amount of calories: ")
    print(part1(elves))
    print("--- PART 2 ---")
    print("Sum of calories of the 3 elves carrying the most: ")
    print(part2(elves))


# answer = 69289
def part1(elves):

    highest_total = 0
    for elf in elves:
        elf_sum = sum_elf_food(elf)

        if elf_sum > highest_total:
            highest_total = elf_sum

    return highest_total


# answer = 205615
def part2(elves):
    # create data
    elf_holder = []
    for index, elf in enumerate(elves):
        elf_holder.append({
            'index': index,
            'calories': int(sum_elf_food(elf))
        })

    # sort, then sum the top 3
    elf_holder.sort(key=lambda x: x['calories'], reverse=True)
    total_calories = 0
    for elf in elf_holder[0:3]:
        total_calories += elf['calories']

    return total_calories


def sum_elf_food(elf):
    elf_sum = 0
    for food in elf:
        elf_sum += int(food)
    return elf_sum
