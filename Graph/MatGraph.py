class Graph:
    def __init__(self,vertex):
        self.vertex = vertex
        self.matrix = [[0]*vertex for i in range(self.vertex)]

    def Insert(self,u,v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1 

    def display(self):
        for i in self.matrix:
            print(i)

g = Graph(4)
g.Insert(0, 1)
g.Insert(1, 2)
g.Insert(2, 3)
g.display()

    