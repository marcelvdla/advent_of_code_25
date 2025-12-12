import numpy as np

class joltage_node:
    def __init__(self, length : int, parent_presses : int):
        self.configuration = np.zeros(length)
        self.presses = parent_presses

    def set_configuration(self, action : tuple[int], parent_config : list[int]):
        self.configuration = [i for i in parent_config]
        for i in action:
            self.configuration[i] += 1

        self.presses += 1
        
        return self.configuration
