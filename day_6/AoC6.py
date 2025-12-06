import numpy as np


def get_total_sum(math_problems, operators):
    result = []
    i = 0
    for op in operators:
        if op == "+":
            result.append(sum(math_problems[:,i]))
        else:
            result.append(np.prod(math_problems[:,i]))
        i += 1
    return sum(result)


def remove_empty_from(string):
    return string != ""


def get_math(file):
    math_problems = []
    operators = []
    with open(file, 'r') as f:
        for line in f:
            raw_data = line.strip("\n").split(" ")
            filtered_data = list(filter(remove_empty_from, raw_data))
            
            try:
                numbers = [int(num) for num in filtered_data]
                math_problems.append(numbers)
            except:
                operators = filtered_data
    
    return get_total_sum(np.array(math_problems), operators)


def read_right_to_left(data, start, end):
    math_problems = []
    for line in data:
        nums = line[start:end]
        math_problems.append(nums)

    actual_nums = []
    current_num = ""
    for i in range(len(math_problems[0])):
        for num in math_problems:
            current_num += num[i]
        actual_nums.append(int(current_num))
        current_num = ""
    
    return actual_nums


def get_total_sum_v2(problems, operators):
    result = []
    i = 0
    for op in operators:
        if op == "+":
            result.append(sum(problems[i]))
        else:
            result.append(np.prod(problems[i]))
        i += 1
    return sum(result)


def get_math_v2(file):
    math_problems = []
    with open(file, 'r') as f:
        data = f.readlines()
    
    data = [line.strip("\n") for line in data]
    operators = list(filter(remove_empty_from, data[-1].split(" ") ))
    
    block_start = 0

    for i in range(len(data[-1]) - 1):
        if data[-1][i] == "+" or data[-1][i] == "*":
            block_start = i

        if data[-1][i+1] == "+" or data[-1][i+1] == "*":
            right_to_left_nums = read_right_to_left(data[:-1], block_start, i)
            math_problems.append(right_to_left_nums)
    
    right_to_left_nums = read_right_to_left(data[:-1], block_start, len(data[0]))
    math_problems.append(right_to_left_nums)

    return get_total_sum_v2(np.array(math_problems, dtype=object), operators)


if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: sum of all problems: {get_math('test_math.txt')}")
    print(f"Actual file: sum of all problems: {get_math('actual_math.txt')} \n")

    print("The answers for the second half:")
    print(f"Test file: sum of all problems: {get_math_v2('test_math.txt')}")
    print(f"Actual file: sum of all problems: {get_math_v2('actual_math.txt')}")