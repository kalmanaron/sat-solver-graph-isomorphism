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
