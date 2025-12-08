import numpy as np
import circuits, node


def find_highest_three(lengths):
    total = 1
    for i in range(3):
        print(lengths)
        j = np.argmax(lengths)
        total *= lengths[j]
        np.delete(lengths, j)

    return total


def get_boxes(file):
    boxes = []

    with open(file, 'r') as f:
        for line in f:
            numbers = line.strip("\n").split(",")
            boxes.append(np.array([int(n) for n in numbers]))
    
    return np.array(boxes)


def find_pairs(file, n):
    circuits = []
    boxes = get_boxes(file)
    boxes_to_check = list(range(len(boxes)))
    found = []
    connections = 0

    while(connections < n):
        current_distances = []
        indexes = []
        for j in boxes_to_check:
            parts = (boxes - boxes[j])**2
            distances = np.sqrt((np.sum(parts, 1)))
            distances = np.delete(distances, j, 0)

            index = np.argmin(distances)
            current_distances.append(distances[index])
            if index >= j:
                indexes.append([j, index+1])
            else:
                indexes.append([j, index])
        

        current_lowest = np.argmin(current_distances)
        i, k = indexes[current_lowest]
        print(i,k)
        boxes_to_check.pop(boxes_to_check.index(i))

        # check if one of these is already in circuits
        added = False
        for c in circuits:
            if i in c and i not in found:
                c.append(k)
                added = True
                found.append(i)
            elif k in c and k not in found:
                c.append(i)
                added = True
                found.append(k)
        
        if not added:
            circuits.append([i,k])
        
        print(circuits)


    circuit_lengths = [len(c) for c in circuits]
    return find_highest_three(circuit_lengths)

if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: the product of the largest three circuit sizes is {find_pairs('example_positions.txt', 10)}")
    # print(f"Actual file: the beam gets split {find_pairs('actual_positions.txt')} times \n")

    # print("The answers for the second half:")
    # print(f"Test file: the beam splits into {} timelines")
    # print(f"Actual file: the beam splits into {} timelines")