file = open('day1_input.txt', 'r')
in_list = list(map(int, file.read().splitlines()))
file.close()

def part1(num_list):
    counter = 0
    for i in range(len(num_list)):
        if num_list[i] > num_list[i-1]:
            counter += 1
    return counter

sum_list = []
def part2(num_list):
    for i in range(len(num_list)-1):
        sum_list.append(num_list[i] + num_list[i-1] + num_list[i+1])
    counter = 0
    for j in range(2, len(sum_list)):
        if sum_list[j] > sum_list[j-1]:
            counter += 1
    return counter

if __name__ == '__main__':
    print(f'Part 1: {part1(in_list)}\nPart 2: {part2(in_list)}')