import fileinput

numbers = []
original_position = []


def read_input():
    i = 0
    for line in fileinput.input():
        number = int(line.strip())
        # add as a tuple with position to avoid problems with duplicates
        numbers.append((number, i))
        original_position.append((number, i))
        i += 1


def solve_part_one():
    for i in range(len(original_position)):
        number = original_position[i]
        curr_position = numbers.index(number)
        new_position = (curr_position + number[0]) % (len(numbers) - 1)
        # if (curr_position+number[0]>len(numbers)):
        #    new_position-=1
        numbers.pop(curr_position)
        # if element is popped before current position
        # if curr_position<new_position: new_position-=1
        if new_position == 0:
            new_position = len(numbers)
        # print(number, curr_position, new_position)
        numbers.insert(new_position, number)
        # print("after ", i, numbers)
    print(numbers)
    zero_index = 0
    while numbers[zero_index][0] != 0:
        zero_index += 1
    print(zero_index)
    # print(numbers[1000 + zero_index - 1][0], numbers[2000 + zero_index - 1], numbers[3000 + zero_index - 1])
    # print(numbers[1000 - 1][0] + numbers[2000 - 1][0] + numbers[3000 - 1][0])
    # print(numbers[1000 + zero_index][0] + numbers[2000 + zero_index][0] + numbers[3000 + zero_index][0])


def solve_part_two():
    for i in range(len(numbers)):
        numbers[i] = (numbers[i][0] * 811589153, numbers[i][1])
        original_position[i] = numbers[i]
    print(numbers)
    for j in range(10):
        for i in range(len(original_position)):
            number = original_position[i]
            curr_position = numbers.index(number)
            # new_position = (curr_position + number[0]) % (len(numbers) - 1)
            new_position = curr_position + number[0]
            if new_position >= len(numbers) - 1:
                new_position %= len(numbers)
            # elif new_position < 0:
            #    new_position = (new_position % len(numbers)) * -1
            # if (curr_position+number[0]>len(numbers)):
            #    new_position-=1

            # if element is popped before current position
            # if curr_position<new_position: new_position-=1
            # if new_position == 0:
            #    new_position = len(numbers)
            # print(number, curr_position, new_position)
            if new_position > 0:
                numbers.pop(curr_position)
                numbers.insert(int(new_position) - 1, number)
            # print("after ", i, numbers)
        print("rounds", j, numbers)
    print(numbers)
    zero_index = 0
    while numbers[zero_index][0] != 0:
        zero_index += 1
    print(zero_index)
    # print(numbers[1000 + zero_index - 1][0], numbers[2000 + zero_index - 1], numbers[3000 + zero_index - 1])
    # print(numbers[1000 - 1][0] + numbers[2000 - 1][0] + numbers[3000 - 1][0])
    # print(numbers[1000 + zero_index][0] + numbers[2000 + zero_index][0] + numbers[3000 + zero_index][0])


read_input()
solve_part_one()
solve_part_two()
