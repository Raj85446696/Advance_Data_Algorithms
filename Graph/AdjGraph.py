class Graph: 
    def __init__(self,V):
        self.V = V 
        self.adjList = {i:[] for i in range(V)}

    def Insert(self,u,v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def display(self):
        for i in self.adjList:
            print(f"{i} --> {self.adjList[i]}")