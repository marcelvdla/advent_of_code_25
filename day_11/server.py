class server:
    def __init__(self, name : str, out : bool = False):
        self.name = name
        self.connections = []
        self.parents = []
        self.parents_copy = []
        self.path_to = []
        self.out = out

    def add_connection(self, server : 'server'):
        self.connections.append(server)

    def add_parent(self, parent : 'server'):
        self.parents.append(parent)
        self.parents_copy.append(parent)

    def remove_parent(self, parent : 'server'):
        self.parents.remove(parent)

    def has_parent(self, parent : 'server'):
        return parent in self.parents

    def reset_parents(self):
        self.parents = self.parents_copy

    def add_path_to(self, path : list):
        for i in range(len(path) // 2):
            head, tail = path[:-i], path[-i:]
            while (len(head) >= len(tail)):
                if (head[-len(tail):] == tail):
                    return False
                else:
                    head.pop(-1)
        
        self.path_to.append(path)
        return True
            