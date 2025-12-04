def rotate(current, rotation):
    direction = rotation[0]
    angle = int(rotation[1:]) % 100
    zero_passes = int(int(rotation[1:]) / 100)

    if direction == "L":
        if current == 0:
            zero_passes -= 1
        result = current - angle
        if result == 0:
            zero_passes += 1
        return (result, zero_passes) if result >= 0 else (100 + result, zero_passes + 1)

    result = current + angle
    return (result, zero_passes) if result <= 99 else (result - 100, zero_passes + 1)


def read_instructions(file):
    with open(file, 'r') as f:
        input = f.readlines()
    return input


def get_answer():
    current, answer = 50, 0
    for rotation in read_instructions('input.csv'):
        current, zero_passes = rotate(current, rotation)
        answer += zero_passes
    return answer


def test_rotate():
    assert(rotate(0, "L15")[0] == 85)
    assert(rotate(0, "R15")[0] == 15)
    assert(rotate(0, "L150")[0] == 50)
    assert(rotate(0, "R150")[0] == 50)
    assert(rotate(0, "L252")[0] == 48)
    assert(rotate(0, "R315")[0] == 15)


def test_example_input():
    truth =             [82, 52, 0, 95, 55, 0, 99, 0, 14, 32]
    truth_zero_passes = [1,  0,  1,  0,  1, 1,  0, 1,  0,  1]
    answer = 0
    i = 0
    current = 50
    for rotation in read_instructions('testInput.csv'):
        oldcurrent = current
        current, zero_passes = rotate(current, rotation)
        answer += zero_passes
        print(i, oldcurrent, "-->", rotation[:-1], current, zero_passes)
        assert(current == truth[i])
        # assert(zero_passes == truth_zero_passes[i])
        i += 1
    assert(answer == 6)


if __name__ == "__main__":
    print("Hello Advent of Code!")
    test_rotate()
    print("Testing the example input for method 0x434C49434B...")
    test_example_input()
    print(f"The actual password to open the door is {get_answer()}")