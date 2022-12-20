import fileinput

numbers = []
original_position = []

def read_input():
    i = 0
    for line in fileinput.input():
        number = int (line.strip())
        # add as a tuple to avoid problems with duplicates
        numbers.append((number,i))
        original_position.append((number,i))
        i+=1


def solve_part_one():
    for i in range (len(original_position)):
        number = original_position[i]
        curr_position = numbers.index(number)
        new_position = (curr_position+number[0])%(len(numbers))
        if (curr_position+number[0]>len(numbers)):
            new_position-=1
        numbers.pop(curr_position)
        # if element is popped before current position
        #if curr_position<new_position: new_position-=1
        if new_position==0: 
            new_position=len(numbers)-1
        print (number, curr_position, new_position)
        numbers.insert(new_position,number)
        print ("after ",i,numbers)
    print (numbers)

read_input()
solve_part_one()