import fileinput, re
from collections import deque


def process_command_part_one(command, stacks):
    nums = [int(s) for s in re.findall(r"-?\d+\.?\d*", command)]
    to_be_moved, from_stack, to_stack = nums[0], nums[1], nums[2]
    for i in range(to_be_moved):
        element = stacks[from_stack - 1].pop()
        stacks[to_stack - 1].append(element)
    return stacks


def process_command_part_two(command, stacks):
    nums = [int(s) for s in re.findall(r"-?\d+\.?\d*", command)]
    to_be_moved, from_stack, to_stack = nums[0], nums[1], nums[2]

    stacks[to_stack - 1].extend((stacks[from_stack - 1])[-to_be_moved:])
    stacks[from_stack - 1] = stacks[from_stack - 1][: len(stacks[from_stack - 1]) - to_be_moved]
    return stacks


def create_stacks(lines):
    # find the last number in the stack naming list
    num_stacks = int(re.findall(r"\d+", lines[len(lines) - 2].strip())[-1])
    stacks = []
    for i in range(num_stacks):
        stacks.append([])
    for line in reversed(lines[:-2]):
        for i in range(num_stacks):
            element = line[i * 4 + 1]
            if element.isupper():
                stacks[i].append(element)
    return stacks


def part_one():
    lines = []
    commands = []
    for line in fileinput.input():
        if line[0] == "m":
            commands.append(line.strip())
        else:
            lines.append(line)
    # part one
    stacks = create_stacks(lines)
    for command in commands:
        stacks = process_command_part_one(command, stacks)
    result = ""
    for stack in stacks:
        result += stack.pop()
    print("part one:", result)
    # part two
    stacks = create_stacks(lines)
    for command in commands:
        stacks = process_command_part_two(command, stacks)
    result = ""
    for stack in stacks:
        result += stack.pop()
    print("part two:", result)


part_one()
