from collections import defaultdict
def topoSort(v, adj):
    visited = [False] * v
    stack = []

    def dfs(node):
        visited[node] = True
        for nei in adj[node]:
            if not visited[nei]:
                dfs(nei)
        stack.append(node)

    for i in range(v):
        if not visited[i]:
            dfs(i)

    return stack[::-1]

adj = {0:[2,3], 1:[3], 2:[3], 3:[]}
print(topoSort(4, adj))
