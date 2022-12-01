import fileinput


def part_one():
    calories, max = 0, 0
    for line in fileinput.input():
        if line.strip().isnumeric():
            calories += int(line)
        else:
            if calories > max:
                max = calories
            calories = 0
    if calories > max:
        max = calories
    print(max)


def part_two():
    calories = 0
    calories_pr_elf = []
    for line in fileinput.input():
        if line.strip().isnumeric():
            calories += int(line)
        else:
            calories_pr_elf.append(calories)
            calories = 0
    calories_pr_elf.append(calories)
    calories_pr_elf.sort()
    print(sum(calories_pr_elf[-3:]))


part_two()
