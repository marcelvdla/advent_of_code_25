import numpy as np
from joltage_node import joltage_node


class joltage_tree:
    def __init__(self, buttons : list, n_lights: int):
        self.buttons = buttons
        self.start_node = joltage_node(n_lights, 0)
        self.n = n_lights


    def traverse_breadth_first(self, goal : np.array):
        queue = [self.start_node]
        nodes_explored = 0

        while (len(queue) > 0):
            current_node = queue[0]
            
            if (all(current_node.configuration == np.array(goal))):
                return current_node.presses
            
            for next in self.buttons:
                
                new_node = joltage_node(self.n, current_node.presses)
                new_node.set_configuration(next.action, current_node.configuration)
                
                if all(new_node.configuration <= goal):
                    try:
                        if np.sum(goal - new_node.configuration) < np.sum(goal - queue[1].configuration):
                            queue = queue[0] + [new_node] + queue[1:]
                        else:
                            queue.append(new_node)
                    except:
                        queue.append(new_node)

            nodes_explored += 1
            print(f"nodes explored: {nodes_explored}", end = "\r", flush=True)
            queue.pop(0)

    def end_state_equals(self, end_state : str):
        return self.current_state == end_state