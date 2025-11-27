class VariableConverter:
    def __init__(self, graph_size: int):
        self.graph_size = graph_size

    def getVarID(self, vertex1: int, vertex2: int):
        id = vertex1 * self.graph_size
        id += vertex2 + 1
        return id
    
    def getVertexes(self, id: int):
        id -= 1
        v1 = id // self.graph_size
        v2 = (id % self.graph_size)
        return (v1, v2)
