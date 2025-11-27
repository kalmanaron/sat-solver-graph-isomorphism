class Graph:
    def __init__(self):
        self.matrix = []

    def loadGraphFromFile(self, filePath: str):
        file1 = open(filePath, 'r')
        input = file1.readlines()
        for line in input:
            line = line.strip().split(' ')
            for i in range(len(line)):
                line[i] = int(line[i])
            self.matrix.append(line)
        file1.close()
    
    def getNumberOfVertecies(self):
        return len(self.matrix)

    def getEdgeBetweenVertecies(self, vertex1: int, vertex2: int):
        return self.matrix[vertex1][vertex2]

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

class CNFConstructor:
    def __init__(self, graph1: Graph, graph2: Graph):
        self.file = open('./formula.cnf', 'w')
        self.g1 = graph1
        self.g2 = graph2
        self.g1_size = self.g1.getNumberOfVertecies()
        self.g2_size = self.g2.getNumberOfVertecies()
        self.clause_counter = 0

    def unsolvableCNF(self):
        self.file.write('p cnf 1 2\n')
        self.file.write('1 0\n-1 0')
    
    def generateCNF(self):
        v1_count = self.g1_size
        v2_count = self.g2_size
        if v1_count != v2_count:
            self.unsolvableCNF()
        else:
            self.VarConv = VariableConverter(v1_count)
            self.isomorphismWholeCNF()

    def isomorphismWholeCNF(self):
        num_vertecies = self.g1_size
        formula = ""
        formula += self.encodeDefinedOnWholeV1()
        formula += self.encodeIsAFunction()
        formula += self.encodeInjection()
        formula += self.encodeSurjection()
        cnf_formula = 'p cnf ' + str(num_vertecies) + ' ' + str(self.clause_counter) + '\n'
        cnf_formula += formula
        self.file.write(cnf_formula)

    def encodeDefinedOnWholeV1(self):
        #every vertex V1 maps to at least one vertex from V2
        out = ""
        for u in range(self.g1_size):
            for v in range(self.g1_size):
                out += str(self.VarConv.getVarID(u, v))
                out += ' '
            out += '0\n'
            self.clause_counter+=1
        return out
    
    def encodeIsAFunction(self):
        #a vertex from V1 doesnt get mapped to two vertexes from V2
        out = ""
        for k in range(self.g1_size):
            for i in range(self.g1_size):
                for j in range(self.g1_size):
                    if i!=j:
                        out += '-' + str(self.VarConv.getVarID(k, i)) + ' -' + str(self.VarConv.getVarID(k, j))
                        out += ' 0\n'
                        self.clause_counter+=1
        return out
    
    def encodeInjection(self):
        #two vertexes from V1 dont recieve the same mapping when they are not the same
        out = ""
        for u in range(self.g1_size):
            for v in range(self.g1_size):
                if v!=u:
                    for i in range(self.g1_size):
                        out += '-' + str(self.VarConv.getVarID(u, i)) + ' -' + str(self.VarConv.getVarID(v, i))
                        out += ' 0\n'
                        self.clause_counter+=1
        return out

    def encodeSurjection(self):
        #every vertex from V2 is a product of a mapping of at least one vertex from V1
        out = ""
        for u in range(self.g1_size):
            for v in range(self.g1_size):
                out += str(self.VarConv.getVarID(v, u))
                out += ' '
            out += '0\n'
            self.clause_counter+=1
        return out

G1 = Graph()
G2 = Graph()
G1.loadGraphFromFile('./graph1.txt')
G2.loadGraphFromFile('./graph2.txt')

CNF = CNFConstructor(G1, G2)
CNF.generateCNF()
print(CNF.encodeInjection())
print()
print(CNF.encodeSurjection())
print()
print(CNF.encodeIsAFunction())