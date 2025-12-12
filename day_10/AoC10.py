from button import button
from tree import tree
from joltage_tree import joltage_tree
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
    indicator_lights, buttons, _ = get_machines(file)
    number_of_machines = len(indicator_lights)

    button_presses = 0

    for i in range(number_of_machines):
        print(f"   finding shortest combination for machine {i}/{number_of_machines}", end="\r", flush=True)
        machine_buttons = [button(b) for b in buttons[i]]
        button_tree = tree(machine_buttons, len(indicator_lights[i]))
        shortest_path = button_tree.traverse_breadth_first(indicator_lights[i])
        
        button_presses += len(shortest_path)

    return button_presses


def find_least_presses_joltage(file):
    _, buttons, joltages = get_machines(file)
    number_of_machines = len(buttons)

    button_presses = 0

    for i in range(number_of_machines):
        print(f"finding shortest combination for machine {i}/{number_of_machines}", end="\r", flush=True)
        machine_buttons = [button(b) for b in buttons[i]]
        button_tree = joltage_tree(machine_buttons, len(joltages[i]))
        shortest_path = button_tree.traverse_breadth_first(np.array(joltages[i]))
        
        button_presses += len(shortest_path)

    return button_presses
    
if __name__ == "__main__":
    print("Hello Advent of Code!")
    print("The answers for the first half:")
    print(f"Test file: the least number of button presses is {find_shortest_paths('example_input.txt')}")
    # print(f"Actual file: size of the largest red square is {find_shortest_paths('actual_input.txt')} \n")

    print("The answers for the second half:")
    print(f"Test file: the least number of button presses is {find_least_presses_joltage('example_input.txt')}")
    # print(f"Actual file: size of the largest red square is {find_shortest_paths('actual_input.txt')} \n")