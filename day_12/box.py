import numpy as np
from present import present

class box:
    def __init__(self, size : tuple[int], num_presents: list[int], present_shapes : list[present]):
        self.grid = np.zeros(size)
        self.gridpoints = size[0] * size[1]
        self.num_presents = num_presents
        self.presents_shapes = present_shapes

    def total_present_size_vs_grid(self):
        i = 0
        total_size_presents = 0
        for np in self.num_presents:
            total_size_presents += np * self.presents_shapes[i].size()
            i += 1

        return total_size_presents <= self.gridpoints


    def fit_present_to_grid(self, present : present):
        pass

    def update_grid(self, grid : np.array):
        self.grid = grid