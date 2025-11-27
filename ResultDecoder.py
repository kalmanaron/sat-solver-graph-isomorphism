import VariableConverter as VC

class ResultDecoder:
    def __init__(self, graphSize):
        self.VarC = VC.VariableConverter(graphSize)
        self.content = ""
        self.readable = []
    
    def decodeFromFile(self, filePath):
        file = open(filePath, 'r')
        self.content = file.readline()
        file.close()
        self.__convertIntoVariables()
    
    def __convertIntoVariables(self):
        temp = self.content.split(' ')
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        for var in temp:
            if var > 0:
                tup = self.VarC.getVertexes(var)
                self.readable.append(tup)
    
    def output(self):
        print('The graphs are isomorphic.')
        print('Here is how to rename the verticies:')
        for tup in self.readable:
            print(str(tup[0]) + ' ---> ' + str(tup[1]))