import fileinput


def is_unique_sequence(sequence):
    chars = set([*sequence])
    if len(chars) == len(sequence):
        return True
    return False


def find_start_of_packet(line, length):
    for i in range(len(line) - length):
        if is_unique_sequence(line[i : i + length]):
            return i + length


def solve():
    for line in fileinput.input():
        print("part one:", find_start_of_packet(line.strip(), 4))
        print("part two:", find_start_of_packet(line.strip(), 14))


solve()
