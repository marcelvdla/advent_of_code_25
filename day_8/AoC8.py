import numpy as np
from node import node
from circuit import circuit
import math

def find_highest_three(lengths):
    total = 1
    for i in range(3):
        # print(lengths)
        j = np.argmax(lengths)
        total *= lengths[j]
        lengths = np.delete(lengths, j)

    return total


def get_boxes(file):
    boxes = []

    with open(file, 'r') as f:
        for line in f:
            numbers = line.strip("\n").split(",")
            boxes.append(np.array([float(n) for n in numbers]))
    
    return np.array(boxes)


def find_index_next_lowest(distances, current_low):
    next_low = np.inf
    for d in distances:
        if d > current_low and d < next_low:
            next_low = d

    return np.where(distances == next_low)[0][0]



def find_shortest_distance_left(boxes, boxes_to_check, circuits):
    current_distances = []
    indexes = []

    for j in boxes_to_check:
        parts = (boxes - boxes[j])**2
        sum_of_parts = np.sum(parts, 1)
        distances = np.sqrt(sum_of_parts)
        distances = np.delete(distances, j, 0)
        
        index = np.argmin(distances)

        if index >= j:
            nodes = [j, index+1]
        else:
            nodes = [j, index]

        # check if this already exists
        current_low = distances[index]
        while(connection_exists(circuits, nodes)):
            index = find_index_next_lowest(distances, current_low)
            
            if index >= j:
                nodes = [j, index+1]
                current_low = distances[index]
            else:
                nodes = [j, index]
                current_low = distances[index]
            
        
        current_distances.append(distances[index])
        indexes.append(nodes)
    
    lowest_distance_index = np.argmin(current_distances)
    nodes = indexes[lowest_distance_index]
    return nodes


def create_new_circuit(indexes):
    n1 = node(indexes[0])
    n2 = node(indexes[1])
    return circuit([n1, n2])


def connection_exists(circuits, nodes):
    if circuits == []:
        return False

    for c in circuits:
        if (c.hasConnection(nodes[0], nodes[1])):
            return True
        
    return False


def find_pairs(file, n):
    boxes = get_boxes(file)
    boxes_to_check = list(range(len(boxes)))

    nodes = find_shortest_distance_left(boxes, boxes_to_check, [])
    circuits = [create_new_circuit(nodes)]
    connections_made = 1

    while(connections_made < n):
        print(f"connection {connections_made} / {n}", end="\r", flush=True)
        
        nodes = find_shortest_distance_left(boxes, boxes_to_check, circuits)
        
        for c in circuits:
            added = False

            if c.containsNode(nodes[0]) and not c.containsNode(nodes[1]):
                node_in_circuit = c.getNodeById(nodes[0])
                new_node = node(nodes[1])
                c.addNodeToCircuit(new_node, node_in_circuit)
                connections_made += 1
                added = True

                break
            
            elif c.containsNode(nodes[1]) and not c.containsNode(nodes[0]):
                node_in_circuit = c.getNodeById(nodes[1])
                new_node = node(nodes[0])
                c.addNodeToCircuit(new_node, node_in_circuit)
                connections_made += 1
                added = True

                break

        if (not added):
            circuits.append(create_new_circuit(nodes))
            connections_made += 1

    circuit_lengths = [c.getCircuitSize() for c in circuits]
    return find_highest_three(circuit_lengths)

if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: the product of the largest three circuit sizes is {find_pairs('example_positions.txt', 10)}")
    print(f"Actual file: the product of the largest three circuit sizes is {find_pairs('actual_positions.txt', 1000)} \n")

    # print("The answers for the second half:")
    # print(f"Test file: the beam splits into {} timelines")
    # print(f"Actual file: the beam splits into {} timelines")