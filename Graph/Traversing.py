from AdjGraph import Graph
from collections import deque

def bfs(graph,node):
    vis = set()
    queue = deque([node])
    vis.add(node)
    while queue:
        n = queue.popleft()
        print(n,end=" ")
        for nei in graph.adjList[n]:
            if nei not in vis:
                vis.add(nei)
                queue.append(nei)


def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    print(node, end=" ")
    visited.add(node)

    for n in graph.adjList[node]:
        if n not in visited:
            dfs(graph, n, visited)


g = Graph(6)
g.Insert(0, 1)
g.Insert(0, 4)
g.Insert(1, 2)
g.Insert(1, 3)
g.Insert(1, 4)
g.Insert(2, 3)
g.Insert(3, 4)
g.Insert(3, 5)

g.display()
print("\nDFS Traversal:")
dfs(g, 0) 


print("\nBFS Traversal:")
bfs(g, 0) 
