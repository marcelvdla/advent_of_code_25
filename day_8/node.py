class node:
    
    def __init__(self, id):
        self.id = id
        self.left = None
        self.right = None

    def setNeighbor(self, neighbor_id):
        if self.left == None:
            self.left = neighbor_id
        elif self.right == None:
            self.right = neighbor_id

    def hasFreeNeighbor(self):
        return self.right == None or self.left == None
    

