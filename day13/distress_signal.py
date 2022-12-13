import fileinput, ast
from functools import cmp_to_key


def correct_order(left, right):
    for leftitem, rightitem in zip(left, right):
        order = 0
        match (leftitem, rightitem):
            case (list() as leftitem, list() as rightitem):
                order = correct_order(leftitem, rightitem)
            case (list() as leftitem, int() as rightitem):
                order = correct_order(leftitem, [rightitem])
            case (int() as leftitem, list() as rightitem):
                order = correct_order([leftitem], rightitem)
            case (int() as leftitem, int() as rightitem):
                if leftitem > rightitem:
                    order = -1
                elif rightitem > leftitem:
                    order = 1
        if order != 0:
            return order
    if len(right) > len(left):
        return 1
    elif len(left) > len(right):
        return -1
    else:
        return 0


def solve():
    # read input
    packets = []
    cnt = 1
    for line in fileinput.input():
        if not cnt % 3 == 0:
            packets.append(ast.literal_eval(line.strip()))
        cnt += 1
    # part one
    result = 0
    for i in range(int(len(packets) / 2)):
        left = packets[i * 2]
        right = packets[i * 2 + 1]
        if correct_order(left, right) != -1:
            result += i + 1
    print("part one", result)

    # part two
    packets.extend([[[2]], [[6]]])
    sortedlist = sorted(packets, key=cmp_to_key(correct_order), reverse=True)
    decoder_key = (sortedlist.index([[2]]) + 1) * (sortedlist.index([[6]]) + 1)
    print(decoder_key)


solve()
