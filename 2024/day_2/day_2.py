
def report_is_safe(report):
    increasing = report[0] < report[1]
    ok = True
    for i in range(len(report) - 1):
        diff = abs(report[i] - report[i + 1])
        diff_ok = 1 <= diff <= 3
        monotone = report[i] < report[i + 1] if increasing else report[i] > report[i + 1]
        if not (diff_ok and monotone):
            ok = False
    return ok


def report_is_safe_with_problem_dampener(report):
    for i in range(len(report)):
        temp = report[:i] + report[i+1:]
        if report_is_safe(temp):
            return True
    return False


def part_one():
    safe = 0
    with open("input.txt", "r") as file:
        for line in file:
            split_line = line.split()
            report = [int(x) for x in split_line]
            if report_is_safe(report):
                safe += 1
    return safe


def part_two():
    safe = 0
    with open("input.txt", "r") as file:
        for line in file:
            split_line = line.split()
            report = [int(x) for x in split_line]
            if report_is_safe(report) or report_is_safe_with_problem_dampener(report):
                safe += 1
            else:
                print()
    return safe


solution_part_one = part_one()
solution_part_two = part_two()
print(f"Solution Part 1: {solution_part_one}")
print(f"Solution Part 2: {solution_part_two}")
