import numpy as np


def get_neighbors(grid, i, j):
    return grid[i-1:i+2,j-1:j+2]


def check_to_remove(grid, i, j):
    if grid[i][j] == 1:
        neighbors = get_neighbors(grid, i, j)
        assert(neighbors.shape == (3,3))
        if np.sum(neighbors) < 5:
            return 1
    return 0


def check_grid(grid):
    removed_rolls = 0
    indeces = []

    for i in range(1,len(grid) - 1):
        for j in range(1, len(grid[0])-1):
            if (check_to_remove(grid, i, j) == 1):
                removed_rolls += 1
                indeces.append((i,j))
    
    return removed_rolls, indeces


def total_rolls(file):
    grid = get_paper(file)
    grid = pad_zeroes(grid)

    return check_grid(grid)[0]


def update(grid, indeces):
    for index in indeces:
        grid[index[0], index[1]] = 0
    
    return grid


def remove_and_update(file):
    grid = get_paper(file)
    grid = pad_zeroes(grid)
    total_removed = 0

    removed_rolls, indeces = check_grid(grid)
    total_removed += removed_rolls

    while (removed_rolls > 0):
        grid = update(grid, indeces)
        removed_rolls, indeces = check_grid(grid)
        total_removed += removed_rolls

    return total_removed


def pad_zeroes(grid):
    padding = np.zeros((len(grid) + 2, len(grid[0]) + 2))

    for i in range(1, len(padding) -1):
        padding[i][1:-1] += grid[i-1]

    return padding


def get_paper(file):
    with open(file, 'r') as f:
        rolls = f.readlines()

    return np.array([np.array([0 if roll == "." else 1 for roll in line.strip("\n")]) for line in rolls])


if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: {total_rolls("example_rolls.txt")} rolls")
    print(f"Actual file: {total_rolls("actual_rolls.txt")} rolls")
    
    print("The answers for the second half:")
    print(f"Test file: {remove_and_update("example_rolls.txt")} rolls")
    print(f"Actual file: {remove_and_update("actual_rolls.txt")} rolls")
