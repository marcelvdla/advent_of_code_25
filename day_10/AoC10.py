from button import button
from tree import tree
import numpy as np
import re

def get_machines(file):
    indicator_lights = []
    buttons = []
    joltages = []

    with open(file, 'r') as f:
        for line in f:
            indicator_lights.append(re.search(r"\[(.+)\]", line)[1])
            button_regex = re.findall(r"\((\d[,\d+]*)\)", line)
            buttons.append([[int(a) for a in b.split(",")] for b in button_regex])
            joltages.append([int(i) for i in re.search(r"\{(.+)\}", line)[1].split(",")])

    return indicator_lights, buttons, joltages


def empty_state_length(n):
    state = ""
    for _ in range(n):
        state += "."

    return state


def find_shortest_paths(file):
    indicator_lights, buttons, joltages = get_machines(file)
    number_of_machines = len(indicator_lights)

    button_presses = 0

    for i in range(1):
        machine_buttons = [button(b) for b in buttons[i]]
        button_tree = tree(machine_buttons, indicator_lights[i])

        empty_state = empty_state_length(len(indicator_lights[i]))

        shortest_paths = [button_tree.traverse_breadth_first(b, empty_state, [], 0) for b in machine_buttons]
        shortest_lengths = [len(p) for p in shortest_paths]
        print(shortest_lengths)

        button_presses += min(shortest_lengths)

    return button_presses


    
if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: the least number of button presses is {find_shortest_paths('example_input.txt')}")
    # print(f"Actual file: size of the largest red square is {('actual_input.txt')} \n")

    # print("The answers for the second half:")
    # print(f"Test file: size of the largest red square is {('example_input.txt')} ")
    # print(f"Actual file: size of the largest red square is {('actual_input.txt')} ")