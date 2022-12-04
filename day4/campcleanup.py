import fileinput

def contained(range1, range2):
    if (range1[0]<=range2[0] and range1[1]>=range2[1]) or (range2[0]<=range1[0] and range2[1]>=range1[1]):
        return 1
    else:
        return 0

def overlap(range1, range2):
    if bool(set(range(range1[0],range1[1]+1)) & set(range(range2[0],range2[1]+1))):
        return 1
    return 0

def part_two():
    sum = 0
    for line in fileinput.input():
        ranges = line.strip().split(',')
        range1 = [int(i) for i in ranges[0].split('-')] 
        range2 = [int(i) for i in ranges[1].split('-')] 
        sum+=overlap(range1, range2)
    print (sum)


def part_one():
    sum = 0
    for line in fileinput.input():
        ranges = line.strip().split(',')
        range1 = [int(i) for i in ranges[0].split('-')] 
        range2 = [int(i) for i in ranges[1].split('-')] 
        sum+=contained(range1, range2)
    print (sum)

part_two()

