from input import input_file

input_values = input_file('input_files/day3_input.txt')
def part_one(nums: list[str]) -> int:
    gamma_rate = ''
    epsilon_rate = ''
    num_length = len(nums[0])

    for i in range(num_length):
        zeros_count = 0
        ones_count = 0
        for num in nums:
            if num[i] == "0":
                zeros_count += 1
            elif num[i] == "1":
                ones_count += 1
        if zeros_count > ones_count:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


def part_two(nums: list[str]) -> int:
    o2_list = nums.copy()
    co2_list = nums.copy()
    num_length = len(nums[0])

    for i in range(num_length):
        zeros_count = 0
        ones_count = 0
        for num in o2_list:
            if num[i] == "0":
                zeros_count += 1
            elif num[i] == "1":
                ones_count += 1
        for num in o2_list.copy():
            if len(o2_list) > 1:
                if zeros_count > ones_count and num[i] == "1":
                    o2_list.remove(num)
                elif ones_count > zeros_count and num[i] == "0":
                    o2_list.remove(num)
                elif ones_count == zeros_count and num[i] == "0":
                    o2_list.remove(num)

    o2_rating = int(o2_list[0], 2)

    for i in range(num_length):
        zeros_count = 0
        ones_count = 0
        for num in co2_list:
            if num[i] == "0":
                zeros_count += 1
            elif num[i] == "1":
                ones_count += 1
        for num in co2_list.copy():
            if len(co2_list) > 1:
                if zeros_count > ones_count and num[i] == "0":
                    co2_list.remove(num)
                elif ones_count > zeros_count and num[i] == "1":
                    co2_list.remove(num)
                elif ones_count == zeros_count and num[i] == "1":
                    co2_list.remove(num)

    co2_rating = int(co2_list[0], 2)

    return co2_rating * o2_rating

if __name__ == '__main__':
    print(f'Part 1: {part_one(input_values)}\nPart 2: {part_two(input_values)}')
