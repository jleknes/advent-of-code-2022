import fileinput
from enum import Enum


class Result(Enum):
    LOSS = 0
    DRAW = 3
    VICTORY = 6


def outcome(player1, player2):
    if (
        (player1 == "A" and player2 == "X")
        or (player1 == "B" and player2 == "Y")
        or (player1 == "C" and player2 == "Z")
    ):
        return Result.DRAW.value
    elif (
        (player1 == "A" and player2 == "Y")
        or (player1 == "B" and player2 == "Z")
        or (player1 == "C" and player2 == "X")
    ):
        return Result.VICTORY.value
    else:
        return Result.LOSS.value


def shape_score(shape):
    match shape:
        case "Y":
            return 2
        case "X":
            return 1
        case "Z":
            return 3


def shape_score_2(shape, result):
    match shape, result:
        case ["A", "X"]:
            return 0 + 3
        case ["A", "Y"]:
            return 3 + 1
        case ["A", "Z"]:
            return 6 + 2
        case ["B", "X"]:
            return 0 + 1
        case ["B", "Y"]:
            return 3 + 2
        case ["B", "Z"]:
            return 6 + 3
        case ["C", "X"]:
            return 0 + 2
        case ["C", "Y"]:
            return 3 + 3
        case ["C", "Z"]:
            return 6 + 1


def part_one():
    score = 0
    for line in fileinput.input():
        player1, player2 = line.split()
        score += outcome(player1, player2)
        score += shape_score(player2)
        print(player1, player2, score)
    print(score)


def part_two():
    score = 0
    for line in fileinput.input():
        player1, outcome = line.split()
        score += shape_score_2(player1, outcome)
    print(score)


part_two()
