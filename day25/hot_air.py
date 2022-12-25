import fileinput


def from_snafu(snafu):
    decimal = 0
    place = 0
    for digit in reversed(snafu):
        position_value = pow(5, place)

        if digit == "-":
            decimal -= position_value
        elif digit == "=":
            decimal -= 2 * position_value
        else:
            decimal += int(digit) * position_value
        place += 1

    return decimal


def to_snafu(decimal):
    snafu = ""
    while decimal > 0:
        digit = decimal % 5
        decimal //= 5
        if digit == 4:
            snafu = "-" + snafu
            decimal += 1
        elif digit == 3:
            snafu = "=" + snafu
            decimal += 1
        else:
            snafu = str(digit) + snafu
    return snafu


def solve():
    sum = 0
    for line in fileinput.input():
        snafu = line.strip()
        sum += from_snafu(snafu)
    print(sum)
    back_to_snafu = to_snafu(sum)
    print(back_to_snafu)

    print(from_snafu(back_to_snafu))


solve()
