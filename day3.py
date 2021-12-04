from input import input_file
from statistics import mode

input_values = input_file('AoC#3_input.txt')
lists = [[] for _ in range(13)]
def part1(file_list):
    for i in file_list:
        lists[0].append(i[0])
        lists[1].append(i[1])
        lists[2].append(i[2])
        lists[3].append(i[3])
        lists[4].append(i[4])
        lists[5].append(i[5])
        lists[6].append(i[6])
        lists[7].append(i[7])
        lists[8].append(i[8])
        lists[9].append(i[9])
        lists[10].append(i[10])
        lists[11].append(i[11])

        gamma = str(mode(lists[0]))+str(mode(lists[1]))+str(mode(lists[2]))+str(mode(lists[3]))+str(mode(lists[4]))+str(mode(lists[5]))+str(mode(lists[6]))+str(mode(lists[7]))+str(mode(lists[8]))+str(mode(lists[9]))+str(mode(lists[10]))+str(mode(lists[11]))
        epsilon = ''
        for i in gamma:
            if i == '0':
                epsilon += '1'
            elif i == '1':
                epsilon += '0'
        gamma = int(gamma, 2)
        epsilon = int(epsilon, 2)
    return gamma*epsilon

lists_2 = [[] for _ in range(13)]
def part2(file_list):
    oxygen_list = []
    part1(input_values)
    for i in file_list:
        if i[0] == str(mode(lists[0])):
            oxygen_list.append(i)
            for o in oxygen_list:
                lists_2[0].append(o[0])
                lists_2[1].append(o[1])
                lists_2[2].append(o[2])
                lists_2[3].append(o[3])
                lists_2[4].append(o[4])
                lists_2[5].append(o[5])
                lists_2[6].append(o[6])
                lists_2[7].append(o[7])
                lists_2[8].append(o[8])
                lists_2[9].append(o[9])
                lists_2[10].append(o[10])
                lists_2[11].append(o[11])
                if o[0] != str(mode(lists_2[0])):
                    oxygen_list.remove(o)
    print(oxygen_list)
part2(input_values)
print(part1(input_values))