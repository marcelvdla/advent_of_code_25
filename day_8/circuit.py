class circuit:

    def __init__(self, initialnodes):
        self.nodes = initialnodes

    def getCircuitSize(self):
        return len(self.nodes)
    
    def addNodeToCircuit(self, added_node, neighbor):
        if (neighbor in self.nodes):
            # added_node.setNeighbor(neighbor)
            # neighbor.setNeighbor(added_node)
            self.nodes.append(added_node)

    def containsNode(self, id):
        for n in self.nodes:
            if n.getId() == id:
                return True
            
        return False
    
    def getNodeById(self, id):
        for n in self.nodes:
            if n.getId() == id:
                return n
            
    def hasConnection(self, id, id2):
        if self.getNodeById(id) != None and self.getNodeById(id2) != None:
            return True
        
        return False