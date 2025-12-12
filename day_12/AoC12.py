import numpy as np
from present import present
from box import box

def get_boxes(file):
    present_shapes = []
    boxes = []

    with open(file, 'r') as f:
        for i in range(6):
            new_present = []
            line = f.readline().strip("\n")
            while (line != ""):
                new_present.append(line)
                line = f.readline().strip("\n")
            
            present_shapes.append(present(new_present))
            
        line = f.readline().strip("\n")
        while (line != ""):
            size, presents = line.split(": ")
            size = size.split("x")
            size = (int(size[0]), int(size[1]))

            presents = [int(p) for p in presents.split(" ")]
            boxes.append(box(size, presents, present_shapes))

            line = f.readline().strip("\n")

    return boxes


def fit_presents(file):
    boxes = get_boxes(file)
    fit = 0
    for box in boxes:
        if box.total_present_size_vs_grid():
            fit += 1

    return fit

    
if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file:  {fit_presents('example_input.txt')}")
    print(f"Actual file:  {fit_presents('actual_input.txt')} \n")

    # print("The answers for the second half:")
    # print(f"Test file:  {('example_input.txt')} ")
    # print(f"Actual file: {('actual_input.txt')} ")