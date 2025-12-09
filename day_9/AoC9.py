import numpy as np
from termcolor import colored

def compute_areas(tiles):
    num_tiles = len(tiles)
    areas = np.zeros((num_tiles, num_tiles))

    for i in range(num_tiles):
        for j in range(num_tiles):
            sides = np.abs(tiles[j] - tiles[i]) + 1
            areas[i][j] = np.prod(sides)

    return areas


def get_red_tiles(file):
    tiles = []

    with open(file, 'r') as f:
        for line in f:
            tiles.append(np.array([int(x) for x in line.strip("\n").split(",")]))

    return np.array(tiles)


def largest_red_square(file):
    tiles = get_red_tiles(file)
    areas = compute_areas(tiles)
    return int(np.max(areas))


def valid_corner(corner, tiles_x, tiles_y):
    # print(f"checking corner {corner} with red tiles in row/colum: {tiles_x, tiles_y}")
    if (len(tiles_x) == 2 and len(tiles_y) == 2):

        # x_interval = tiles_x[0][1] <= corner[1] <= tiles_x[1][1]
        x_interval = corner[1] in range(min([tiles_x[0][1], tiles_x[1][1]]), max([tiles_x[0][1], tiles_x[1][1]]) + 1)
        # y_interval = tiles_y[0][0] <= corner[0] <= tiles_y[1][0]
        y_interval = corner[0] in range(min([tiles_y[0][0], tiles_y[1][0]]), max([tiles_y[0][0], tiles_y[1][0]]) + 1)

        if (not x_interval):
            print(f" {corner[1]} is not in the interval {tiles_x[0][1], tiles_x[1][1]} ")
        else: 
            print(f" {corner[1]} is in the interval {tiles_x[0][1], tiles_x[1][1]} ")

        if (not y_interval):
            print(f" {corner[0]} is not in the interval {tiles_y[0][0], tiles_y[1][0]} ")
        else: 
            print(f" {corner[0]} is in the interval {tiles_y[0][0], tiles_y[1][0]} ")

        if (x_interval or y_interval):
            return True
    elif (len(tiles_x) != len(tiles_y)):
        print(f"{corner} comes here")
        return False
    
    if (len(tiles_x) <= 1 or len(tiles_y) <= 1):
        return True
    
    return False


def is_red_square_contained(tiles, corners):
    corners_to_validate = [[corners[0][0], corners[1][1]], [corners[1][0], corners[0][1]]]

    for ctv in corners_to_validate:
        tiles_x, tiles_y = [], []
        for t in tiles:
            if t[0] == ctv[0]:
                tiles_x.append(t)
            if t[1] == ctv[1]:
                tiles_y.append(t)
        if (not valid_corner(ctv, tiles_x, tiles_y)):
            print(f"corner {ctv} is not valid")
            return False
        else:
            print(f"corner {ctv} is valid")
    
    return True


def crossed_boundary_x(x_start, x_end, y, tiles):
    print(f"checking for edge of square ({min(x_start, x_end), max(x_start, x_end)}) y={y}")
    for x in range(min(x_start, x_end), max(x_start, x_end)):
        # all tiles 
        lines = np.where(tiles[:,0] == x)[0]
        # print(x, lines)
        
        if (len(lines) < 2):
            continue
        
        start_line = tiles[lines[0], 1]
        end_line = tiles[lines[1], 1]

        if (min(start_line, end_line) <= y <= max(start_line, end_line)):
            print(f"crosses between line ({min(start_line, end_line), max(start_line, end_line)} at x={x}) \n\n")
            return True
    
    return False


def crossed_boundary_y(y_start, y_end, x, tiles):
    print(f"checking for edge of square ({min(y_start, y_end), max(y_start, y_end)}) x={x}")
    for y in range(min(y_start, y_end), max(y_start, y_end)):
        
        # all lines is this correct for y? 
        lines = np.where(tiles[:,1] == y)[0]
        # print(y, lines)

        if (len(lines) < 2):
            continue

        start_line = tiles[lines[0], 0]
        end_line = tiles[lines[1], 0]
    
        if (min(start_line, end_line) <= x <= max(start_line, end_line)):
            print(f"crosses between line ({min(start_line, end_line), max(start_line, end_line)} at y={y}) \n\n")
            return True
    
    return False


def square_crosses_boundary(corners, tiles):
    lines_x = [corners[0][0], corners[1][0]]
    lines_y = [corners[0][1], corners[1][1]]

    for i in [0,1]:
        if(crossed_boundary_x(lines_x[0], lines_x[1], lines_y[i], tiles)):
            return True
        if(crossed_boundary_y(lines_y[0], lines_y[1], lines_x[i], tiles)):
            return True
    
    return False



def largest_red_square_contained(file):
    tiles = get_red_tiles(file)
    areas = compute_areas(tiles)
    # print(areas)
    highest = np.argmax(areas)

    # print(highest)
    # print(highest // len(tiles))
    # print(highest % len(tiles))
    # print(tiles[1], tiles[5])

    corner_index = [highest // len(tiles), highest % len(tiles)]
    corners = np.array([tiles[corner_index[0]], tiles[corner_index[1]]])
    i = 1
    print(f"checking for square {corners} with size {int(np.max(areas))}")#, end ="\r", flush=True)
    print_grid(tiles, corners)

    while (square_crosses_boundary(corners, tiles)):
        # print(f"trying {i}th new square: {corners}", end="\r", flush=True)
        areas[corner_index[0], corner_index[1]] = 0
        areas[corner_index[1], corner_index[0]] = 0
        highest = np.argmax(areas)
        corner_index = [highest // len(tiles), highest % len(tiles)]
        corners = np.array([tiles[corner_index[0]], tiles[corner_index[1]]])
        i += 1
        if i == 20:
            break
        print(f"checking for square {corners} with size {int(np.max(areas))}")#, end ="\r", flush=True)
        print_grid(tiles, corners)
    
    return int(np.max(areas))


def print_grid(tiles, corners):
    grid = np.zeros((np.max(tiles[:,1])+2, np.max(tiles[:,0])+2))

    xmin, xmax = min(corners[:,0]), max(corners[:,0])
    ymin, ymax = min(corners[:,1]), max(corners[:,1])

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if xmin <= x <= xmax and ymin <= y <= ymax:
                grid[y][x] = 2
    
    for tile in tiles:
        grid[tile[1]][tile[0]] = 1

    print("y x  1  2  3  4  5  6  7  8  9 10 11 12 ")
    for y in range(len(grid)):
        line = f"{y}"
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                line += " . "
            elif grid[y][x] == 1:
                line += colored(" # ", 'red')
            else:
                line += " 0 "
        print(line)

if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: size of the largest red square is {largest_red_square('example_input.txt')}")
    print(f"Actual file: size of the largest red square is {largest_red_square('actual_input.txt')} \n")

    print("The answers for the second half:")
    print(f"Test file: size of the largest red square is {largest_red_square_contained('example_input.txt')} ")
    # print(f"Actual file: size of the largest red square is {largest_red_square_contained('actual_input.txt')} ")