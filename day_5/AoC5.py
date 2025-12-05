def check_overlap(input, ranges):
    try:
        ranges.pop(ranges.index(input))
    except:
        print("reading", end = "\r", flush=True)
    
    for i in range(len(ranges)):
        
        if input[0] <= ranges[i][0]:
            #    |________________|      <- input
            #       |__________|         <- ranges[i]
            if input[1] >= ranges[i][1]:
                ranges[i] = input
                return ranges

            #    |__________|            <- input
            #       |__________|         <- ranges[i]
            elif input[1] <= ranges[i][1] and input[1] >= ranges[i][0]:
                ranges[i] = [input[0], ranges[i][1]]
                return ranges
            
        elif input[0] >= ranges[i][0] and input[0] <= ranges[i][1]:
            #          |__________|      <- input
            #       |__________|         <- ranges[i]
            if input[1] >= ranges[i][1]:
                ranges[i] = [ranges[i][0], input[1]]
                return ranges

            #          |____|            <- input
            #       |_____________|      <- ranges[i]
            elif input[1] <= ranges[i][1]:
                return ranges

    ranges.append(input)
    return ranges


def filter_overlapping(ranges):
    ranges = ranges[1:]
    rangelength = len(ranges)

    for r in ranges:
        ranges = check_overlap(r, ranges)

    while (len(ranges) < rangelength):
        rangelength = len(ranges)
        for r in ranges:
            ranges = check_overlap(r, ranges)

    return ranges


def get_ingredients(file):
    ranges = [[0, 0]]
    ingredients = []

    with open(file, 'r') as f:
        for line in f:
            l = line.strip("\n").split('-')
            if len(l) == 1 and l[0] != "":
                ingredients.append(int(l[0]))
            elif len(l) == 2:
                ranges = check_overlap([int(l[0]), int(l[1])], ranges)
    
    return filter_overlapping(ranges), ingredients


def find_fresh_ingredients(file):
    ranges, ingredients = get_ingredients(file)
    fresh = []

    for i in ingredients:
        for r in ranges:
            if r[0] <= i <= r[1]:
                fresh.append(i)
    
    return fresh


def find_num_fresh_ingredients(file):
    ranges, _ = get_ingredients(file)
    total = 0

    for r in ranges:
        total += (r[1] + 1 - r[0])

    return total


if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: {len(find_fresh_ingredients("example_ingredients.txt"))} fresh ingredients")
    print(f"Actual file: {len(find_fresh_ingredients("actual_ingredients.txt"))} fresh ingredients")
    
    print("The answers for the second half:")
    print(f"Test file: {find_num_fresh_ingredients("example_ingredients.txt")} ingredients")
    print(f"Actual file: {find_num_fresh_ingredients("actual_ingredients.txt")} ingredients")
