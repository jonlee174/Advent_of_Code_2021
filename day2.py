from input import input_file

file = input_file('input_files/day2_input.txt')
def part1(input_values):
    horiz = 0
    up = 0
    down = 0
    for i in input_values:
        if 'f' in i:
            horiz += int(i[-1])
        elif 'n' in i:
            down += int(i[-1])
        elif 'p' in i:
            up += int(i[-1])
    depth = down - up
    return horiz*depth

def part2(input_values):
    fd = 0
    aim = 0
    depth = 0
    for i in input_values:
        if 'f' in i:
            fd += int(i[-1])
            depth += int(i[-1]) * aim
        elif 'n' in i:
            aim += int(i[-1])
        elif 'p' in i:
            aim -= int(i[-1])
    return fd*depth

if __name__ == '__main__':
    print(f'Part 1: {part1(file)}\nPart 2: {part2(file)}')
