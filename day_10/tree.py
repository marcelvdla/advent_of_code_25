import numpy as np
import button

class tree:
    def __init__(self, buttons : list, n_lights: int):
        self.current_state = n_lights * "."
        self.buttons = buttons
        self.current_shortest = np.inf
        self.path = []
        self.max_depth = n_lights + 1


    def __str__(self):
        path = ""
        for b in self.path:
            path += b.__str__()
        return path


    def traverse_breadth_first(self, state : str):
        queue = [[b] for b in self.buttons]

        while (len(queue) > 0):
            for b in queue[0]:
                self.current_state = b.press(self.current_state)
            
            if (self.end_state_equals(state)):
                self.path = queue[0]
                return queue[0]
            
            for next in [nb for nb in self.buttons if nb not in queue[0]]:
                check_next = queue[0] + [next]
                if len(check_next) <= self.max_depth:
                    queue.append(check_next)
            
            queue.pop(0)
            
            self.current_state = len(self.current_state) * "."
        
        return f"No path found in depth {self.max_depth}"

    def end_state_equals(self, end_state : str):
        return self.current_state == end_state