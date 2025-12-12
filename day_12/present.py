import numpy as np

class present:
    def __init__(self, input : list[str]):
        self.id = int(input[0].strip(":"))
        self.shape = np.array([np.array([0 if point == "." else 1 for point in line]) for line in input[1:]])
    
    def rotate(self, direction : int):
        if direction == -1:
            return np.flip(np.transpose(self.shape), axis= 0)

        if direction == 1:
            return np.flip(np.transpose(self.shape), axis= 1)
        
    def size(self):
        return np.sum(self.shape)