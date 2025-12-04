def check_valid(id):
    if len(id) % 2 != 0:
        return 0
    first_half = id[: len(id) // 2]
    second_half = id[ len(id) // 2:]
    if  first_half == second_half:
        return int(id)
    return 0


def split_number_in(n, number):
    split_length = len(number) // n
    number_list = []
    for i in range(n):
        number_list.append(number[i*split_length:(i+1)*split_length])
    
    if (len(number_list) > 1):
        return all([number == number_list[0] for number in number_list])
    return False


def check_valid_multiple_repeats(id):
    for l in range(2, len(id)+1):
        if (len(id) % l == 0) & (split_number_in(l, id)):
            return int(id)
    return 0


def check_range(ids, func):
    low, high = ids.split('-')
    invalids = [func(str(id)) for id in range(int(low), int(high) + 1)]
    return sum(invalids)


def read_ids(file, func):
    with open(file, 'r') as f:
        id_ranges = f.readline().split(',')
    
    return sum([check_range(ids, func) for ids in id_ranges])


if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"The sum of invalid IDs in the test set is {read_ids("test_IDs.csv", check_valid)}")
    print(f"The sum of invalid IDs in the actual set is {read_ids("IDs.csv", check_valid)}")
    
    print("The answers for the second half:")
    print(f"The sum of invalid IDs in the test set is {read_ids("test_IDs.csv", check_valid_multiple_repeats)}")
    print(f"The sum of invalid IDs in the actual set is {read_ids("IDs.csv", check_valid_multiple_repeats)}")