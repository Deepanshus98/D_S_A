def toposort(graph):
    visited = [False for i in range(len(graph))]
    result = []

    def DFS(node):
        if visited[node]:
            return
        visited[node] = True
        for adj in graph[node]:
              DFS(adj)
        result.append(node)
    
    for i in range(len(graph)):
        DFS(i)

    return result
