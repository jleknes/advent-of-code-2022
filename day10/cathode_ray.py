import fileinput, sys


def calc_signal_strength(cycle, x):
    if cycle % 40 == 20:
        return cycle * x
    else:
        return 0


def pixel(cycle, x):
    position = (cycle - 1) % 40
    print("cycle:", cycle, "position:", position, "X:", x)
    if position >= x - 1 and position <= x + 1:
        return "#"
    else:
        return "."


def solve():
    x = 1
    cycle = 0
    signal_strength = 0
    crt = ""
    for line in fileinput.input():
        if line.startswith("noop"):
            cycle += 1
            signal_strength += calc_signal_strength(cycle, x)
            crt += pixel(cycle, x)
        else:
            addx = int(line.split()[1].strip())
            cycle += 1
            crt += pixel(cycle, x)
            signal_strength += calc_signal_strength(cycle, x)
            cycle += 1
            crt += pixel(cycle, x)
            signal_strength += calc_signal_strength(cycle, x)
            x += addx
    print("part one", signal_strength)
    print("part two")
    for i in range(len(crt)):
        if i % 40 == 0:
            print()

        sys.stdout.write(crt[i])
    print()


solve()
