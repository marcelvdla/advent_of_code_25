def maximum_joltage(row):
    first_high, second_high = 0, 0

    for battery in range(len(row)-1):
        if int(row[battery]) > first_high:
            first_high = int(row[battery])
            second_high = int(row[battery+1])
        elif int(row[battery+1]) > second_high:
            second_high = int(row[battery+1])

    joltage = int(str(first_high) + str(second_high))
    return joltage


def maximum_joltage_12(row, n, current):
    if n == 0:
        return current

    highest = 0
    for i in range(len(row)-n+1):
        if int(row[i]) > int(row[highest]):
            highest = i

    current.append(row[highest])
    maximum_joltage_12(row[highest+1:], n-1, current)

    assert(len(current) == 12)

    total = ""
    for i in current:
        total += i
    return int(total)


def read_joltages(file, func):
    with open(file, 'r') as f:
        joltages = f.readlines()

    if func == maximum_joltage:
        return sum([func(battery_row[:-1]) for battery_row in joltages])
    else:
        return sum([func(battery_row[:-1], 12, []) for battery_row in joltages])


if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: {read_joltages("test_joltage.txt", maximum_joltage)} jolts")
    print(f"Test file: {read_joltages("actual_joltage.txt", maximum_joltage)} jolts")
    
    print("The answers for the second half:")
    print(f"Test file: {read_joltages("test_joltage.txt", maximum_joltage_12)} jolts")
    print(f"Test file: {read_joltages("actual_joltage.txt", maximum_joltage_12)} jolts")
