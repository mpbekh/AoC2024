# part 1
reports = []
with open('input2.txt', "r") as input:
    # split input into lines
    inputs = input.read().splitlines()
    for report in inputs:
        # split each line into list with white space as delitimer
        split = report.split(' ')
        # append each line as list of integer values
        reports.append([ int(x) for x in split])

def increasing(report) -> bool:
    # using zip() + all() to check for strictly increasing list
    return all(i < j for i, j in zip(report, report[1:]))

def decreasing(report) -> bool:
    # using zip() + all() to check for strictly decreasing list
    return all(i > j for i, j in zip(report, report[1:]))

def diff_less_than_three(report) -> bool:
    # using zip() + all() to check for diff value
    return all(abs(i-j) <= 3 for i, j in zip(report, report[1:]))

def safe(report) -> bool:
    return (increasing(report) or decreasing(report)) and diff_less_than_three(report)

count = 0
for report in reports:
    if safe(report):
        count += 1

print(f"Number of safe reports: {count}")

# part 2
def safe_when_level_is_removed(report) -> bool:
    # check whether removing one level from
    # the report would make it safe.
    # return True in that case, otherwise return false.
    for i, level in enumerate(report):
        temp_report = list(report)
        temp_report.pop(i)
        if safe(temp_report):
            return True
    return False

count = 0
for report in reports:
    if safe(report) or safe_when_level_is_removed(report):
        count += 1

print(f"Number of safe reports when removing a level: {count}")
