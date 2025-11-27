import Graph as G
import VariableConverter as VC

class CNFConstructor:
    def __init__(self, graph1: G.Graph, graph2: G.Graph):
        self.g1 = graph1
        self.g2 = graph2
        self.g1_size = self.g1.getNumberOfVertecies()
        self.g2_size = self.g2.getNumberOfVertecies()
        self.clause_counter = 0
        self.dimacs_cnf = ""

    def getDimacsCNF(self):
        return self.dimacs_cnf
    
    def writeDIMACS_CNFinto(self, filePath):
        file = open(filePath, 'w')
        file.write(self.dimacs_cnf)
        file.close()

    def generateCNF(self):
        v1_count = self.g1_size
        v2_count = self.g2_size
        if v1_count != v2_count:
            self.__unsolvableCNF()
        else:
            self.VarConv = VC.VariableConverter(v1_count)
            self.__isomorphismWholeCNF()
    
    def __unsolvableCNF(self):
        self.dimacs_cnf = ""
        self.dimacs_cnf += 'p cnf 1 2\n'
        self.dimacs_cnf += '1 0\n-1 0'

    def __isomorphismWholeCNF(self):
        num_vertecies = self.g1_size
        formula = ""
        formula += self.__encodeDefinedOnWholeV1()
        formula += self.__encodeIsAFunction()
        formula += self.__encodeInjection()
        formula += self.__encodeSurjection()
        formula += self.__encodeEdgeMatch()
        self.dimacs_cnf = ""
        self.dimacs_cnf += 'p cnf ' + str(num_vertecies**2) + ' ' + str(self.clause_counter) + '\n'
        self.dimacs_cnf += formula

    def __encodeDefinedOnWholeV1(self):
        #every vertex V1 maps to at least one vertex from V2
        out = ""
        for u in range(self.g1_size):
            for v in range(self.g1_size):
                out += str(self.VarConv.getVarID(u, v))
                out += ' '
            out += '0\n'
            self.clause_counter+=1
        return out
    
    def __encodeIsAFunction(self):
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
    
    def __encodeInjection(self):
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

    def __encodeSurjection(self):
        #every vertex from V2 is a product of a mapping of at least one vertex from V1
        out = ""
        for u in range(self.g1_size):
            for v in range(self.g1_size):
                out += str(self.VarConv.getVarID(v, u))
                out += ' '
            out += '0\n'
            self.clause_counter+=1
        return out

    def __encodeEdgeMatch(self):
        #there are edge conflicts
        out = ""
        for u in range(self.g1_size):
            for v in range(self.g1_size):
                for i in range(self.g1_size):
                    for j in range(self.g1_size):
                        if (
                            (self.g1.getEdgeBetweenVertecies(u,v) == 1) and (self.g2.getEdgeBetweenVertecies(i, j) == 0)
                                or
                            (self.g1.getEdgeBetweenVertecies(u,v) == 0) and (self.g2.getEdgeBetweenVertecies(i, j) == 1)
                        ):
                            out += '-' + str(self.VarConv.getVarID(u, i)) + ' -' + str(self.VarConv.getVarID(v,j))
                            out += ' 0\n'
                            self.clause_counter+=1
        return out
