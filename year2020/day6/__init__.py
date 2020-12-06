def day6():
    with open("year2020/day6/input.txt", "r") as f:
        full_array = f.read().split('\n\n')

    full_question_list = []
    for question_list in full_array:
        full_question_list.append(question_list.split('\n'))

    print('Part 1 - Sum of all questions SOMEONE answered yes')
    print(part1(full_question_list))
    print('Part 2 - Sum of all questions ALL people in group answered yes')
    print(part2(full_question_list))


# answer = 6521
def part1(full_question_list):
    total = 0
    for questions in full_question_list:
        num_unique = set()
        for question in questions:
            num_unique = num_unique.union(set(list(question)))
        total += len(num_unique)
    return total


# answer = 3305
def part2(full_question_list):
    total = 0
    for questions in full_question_list:
        num_unique = set(list(questions[0]))
        for question in questions:
            num_unique.intersection_update(set(list(question)))
        total += len(num_unique)
    return total
