import fileinput

results = {}
calculations = {}


def read_input():
    for line in fileinput.input():
        defines = line[0:4]
        if line[6:].strip().isnumeric():
            results[defines] = int(line[6:].strip())
        else:
            calculations[defines] = line[6:].strip()


def calculate(part1, part2, operation):
    if operation == "*":
        return part1 * part2
    if operation == "+":
        return part1 + part2
    if operation == "/":
        return int(part1 / part2)
    if operation == "-":
        return part1 - part2


def solve_part_one():
    print(results.keys())
    finished = False
    while not finished:
        for key in calculations:
            calculation = calculations[key]
            part1 = calculation[0:4]
            part2 = calculation[7:]
            operation = calculation[5:6]
            if part1 in results.keys() and part2 in results.keys():
                print(part1, operation, part2)
                print(calculate(results[part1], results[part2], operation))
                results[key] = calculate(results[part1], results[part2], operation)
        if "root" in results:
            finished = True
    print(results["root"])


def find_root_answer(humn, root_part):
    finished = False
    local_results = dict(results)

    while not finished:
        for key in calculations:
            calculation = calculations[key]
            part1 = calculation[0:4]
            part2 = calculation[7:]
            operation = calculation[5:6]
            if part1 in local_results.keys() and part2 in local_results.keys():
                part1_val = (humn, int(local_results[part1]))[part1 != "humn"]
                part2_val = (humn, int(local_results[part2]))[part2 != "humn"]
                local_results[key] = calculate(part1_val, part2_val, operation)

            if root_part in local_results:
                finished = True
    return local_results[root_part]


def solve_part_two():
    root1 = calculations["root"][0:4]
    root2 = calculations["root"][7:]
    low, high = 0, 1000000000000000
    while low != high:
        mid = int((low + high) / 2)
        if abs(find_root_answer(mid, root1) == find_root_answer(mid, root2)):
            low = mid
            high = mid
            continue

        diff1 = abs(find_root_answer(low, root1) - find_root_answer(high, root2))

        diff2 = abs(find_root_answer(high, root1) - find_root_answer(high, root2))
        if diff2 < diff1:
            low = mid + 1
        else:
            high = mid - 1

    print(high)


read_input()
solve_part_one()
solve_part_two()
