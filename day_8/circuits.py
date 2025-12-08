class circuit:

    def __init__(self, initialnode):
        self.initialnode = initialnode
        self.nodes = [initialnode]

    def getCircuitSize(self):
        return len(self.nodes)
    
    def addNodeToCircuit(self, id):
        