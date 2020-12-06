def day1():
    f = open("year2020/day1/input.txt", "r")
    expense_report_nums = []
    for x in f:
        expense_report_nums.append(int(x))

    print(part1(expense_report_nums))
    print(part2(expense_report_nums))


# answer = 1018944
def part1(expense_report_nums):

    for a in expense_report_nums:
        for b in expense_report_nums:
            if a+b == 2020:
                return a*b

    return 'Nothing found?'


# answer = 8446464
def part2(expense_report_nums):
    for a in expense_report_nums:
        for b in expense_report_nums:
            for c in expense_report_nums:
                if a+b+c == 2020:
                    return a*b*c

    return 'Nothing found?'