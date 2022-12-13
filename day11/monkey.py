import fileinput


class Monkey:
    def __init__(self, items, calculation, divisor, throwToTrue, throwToFalse):
        self.items = items
        self.calculation = calculation
        self.divisor = divisor
        self.throwToTrue = throwToTrue
        self.throwToFalse = throwToFalse
        self.items_inspected = 0

    def __str__(self):
        return str(self.items)


def perform_test(worry_level, divisor):
    quotient = int(test.split()[2])
    return worry_level % quotient == 0


def perform_maths(input, calculation):
    param1, operation, param2 = calculation[6:].split()
    if param1 == "old":
        param1 = input
    if param2 == "old":
        param2 = input

    match (operation):
        case "*":
            return int(param1) * int(param2)
        case "+":
            return int(param1) + int(param2)


def simulate_round(monkeys):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            item = monkey.items.pop()
            worry_level = perform_maths(item, monkey.calculation)
            worry_level = int(worry_level / 3)
            if perform_test(worry_level, monkey.test):
                monkeys[monkey.throwToTrue].items.append(worry_level)

            else:
                monkeys[monkey.throwToFalse].items.append(worry_level)
            monkey.items_inspected += 1
    return monkeys


def perform_maths_2(input, calculation, divisor):
    param1, operation, param2 = calculation[6:].split()
    if param1 == "old":
        param1 = input
    if param2 == "old":
        param2 = input

    match (operation):
        case "*":
            return (int(param1) % divisor * int(param2) % divisor) % divisor
        case "+":
            return (int(param1) % divisor + int(param2) % divisor) % divisor


def simulate_round_part_two(monkeys):
    for monkey in monkeys:
        while len(monkey.items) > 0:
            worry_level = monkey.items.pop()
            for key in worry_level:
                worry_level_mod = worry_level[key]
                worry_level[key] = perform_maths_2(worry_level_mod, monkey.calculation, key)

            if worry_level[monkey.divisor] == 0:
                monkeys[monkey.throwToTrue].items.append(worry_level)
            else:
                monkeys[monkey.throwToFalse].items.append(worry_level)
            monkey.items_inspected += 1
    return monkeys


def read_monkey(lines):
    items = list(map(int, lines[1][18:].strip().split(", ")))
    calculation = lines[2][13:].strip()
    divisor = int(lines[3][8:].strip().split()[2])
    throw_to_true = int(lines[4][29:].strip())
    throw_to_false = int(lines[5][29:].strip())
    return Monkey(items, calculation, divisor, throw_to_true, throw_to_false)


def solve():
    monkeys = []
    lines = []
    divisors = []
    for line in fileinput.input():
        lines.append(line)

    for i in range(0, int(len(lines) / 7) + 1):
        monkeys.append(read_monkey(lines[i * 7 : i * 7 + 6]))

    for i in range(len(monkeys)):
        print("Monkey nr", i, monkeys[i], "divisor", monkeys[i].divisor, "calculation", monkeys[i].calculation)
        divisors.append(int(monkeys[i].divisor))

    for monkey in monkeys:
        for i in range(len(monkey.items)):
            worry_level_modulus = {}
            worry_level = monkey.items[i]
            for divisor in divisors:
                worry_level_modulus[divisor] = worry_level % divisor
            monkey.items[i] = worry_level_modulus

    for round in range(0, 10000):
        monkeys = simulate_round_part_two(monkeys)
    for i in range(len(monkeys)):
        print("Monkey nr", i, "items inspected", monkeys[i].items_inspected)


solve()
