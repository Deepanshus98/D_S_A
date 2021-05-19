class Graph:
 
    # Constructor
    def __init__(self, edges, N):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Function to perform DFS traversal on the graph on a graph
def DFS(graph, v, discovered, parent):
 
    # mark the current node as discovered
    discovered[v] = True
 
    # do for every edge `v —> w`
    for w in graph.adjList[v]:
 
        # if `w` is not discovered
        if not discovered[w]:
            if DFS(graph, w, discovered, v):
                return True
 
        # if `w` is discovered, and `w` is not a parent
        elif w != parent:
            # we found a back-edge (cycle)
            return True
 
    # No back-edges were found in the graph
    return False
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11), (11, 12)
        # edge `11 —> 12` introduces a cycle in the graph
    ]
 
    # total number of nodes in the graph
    N = 13
 
    # build a graph from the given edges
    graph = Graph(edges, N)
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * N
 
    # Perform DFS traversal from the first vertex
    if DFS(graph, 1, discovered, -1):
        print("The graph contains a cycle")
    else:
        print("The graph doesn't contain any cycle")
