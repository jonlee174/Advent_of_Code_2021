
from input import input_file

def part1():
    horiz = []
    up = []
    down = []
    for i in input_file('AoC#2_input.txt'):
        if 'f' in i:
            horiz.append(int(i[-1]))
        elif 'n' in i:
            down.append(int(i[-1]))
        elif 'p' in i:
            up.append(int(i[-1]))
    horizontal_val = sum(horiz)
    up_val = sum(up)
    down_val = sum(down)
    depth_val = down_val - up_val
    return horizontal_val*depth_val

def part2():
    fd = 0
    aim = 0
    depth = 0
    for i in input_file('AoC#2_input.txt'):
        if 'f' in i:
            fd += int(i[-1])
            depth += int(i[-1]) * aim
        elif 'n' in i:
            aim += int(i[-1])
        elif 'p' in i:
            aim -= int(i[-1])
    return fd*depth

if __name__ == '__main__':
    print(f'Part 1: {part1()}\nPart 2: {part2()}')