import numpy as np
import button

class tree:
    def __init__(self, buttons : list, end_state: str):
        self.end_state = end_state
        self.buttons = buttons
        self.current_shortest = np.inf
        self.path = []
        self.max_depth = len(self.end_state) + 1

    # this is currently depth first oops
    def traverse_breadth_first(self, 
                               start : button, 
                               state : str,
                               path : list,
                               depth : int):
        state = start.press(state)
        current_state = start.press(state)
        path.append(start)

        queue = [[b] for b in self.buttons if b != start]

        while (len(queue) > 0):
            for p in queue:
                self.print_path(p)

            for b in queue[0]:
                current_state = b.press(current_state)
            
            if (self.end_state_equals(state)):
                path += queue[0]
                return path
            
            for next in [b for b in self.buttons if b != queue[0][-1]]:
                # print(queue[0], next)
                queue.append(queue[0] + [next])
                # print([self.print_path(p) for p in queue])
                queue.pop(0)
            
            current_state = state

            break




    def doesntwork(self):
        pass
        
        if (self.end_state_equals(state) or depth == self.max_depth):
            # print(f"path {[b.action for b in path]} to {state} found at depth {depth}")
            return path
        
        for b in self.buttons:
            # print(f"at depth {depth} all states should be the same: {state}")
            if b == current:
                continue
            
            # print(path)
            # check_path = [p for p in path]
            # check_path.append(b)
            # check_state = state

            new_path = self.traverse_breadth_first(b, state, path, depth + 1)
            self.print_path(new_path)

            if len(new_path) < self.current_shortest:
                self.path = new_path
                self.current_shortest = len(new_path)
        
        return self.path


    def end_state_equals(self, state : str):
        return self.end_state == state


    def print_path(self, path):
        print(f"path: {[b.action for b in path]}")