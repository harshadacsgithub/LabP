class Graph:
    def __init__(self):
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append((u, v, w))

    def minimum_spanning_tree(self):
        self.graph.sort(key=lambda x: x[2])

        parent = {}  
        rank = {}    
        result = []
        total_cost = 0

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        for u, v, w in self.graph:
            if u not in parent:
                parent[u] = u
                rank[u] = 0
            if v not in parent:
                parent[v] = v
                rank[v] = 0

            if find(u) != find(v):
                union(u, v)
                result.append((u, v, w))
                total_cost += w

        return result, total_cost

def take_input():
    edges = int(input("Enter the number of edges: "))
    g = Graph()
    print("Enter edges in the format 'source destination weight': ")
    for _ in range(edges):
        u, v, w = input().split()
        g.add_edge(u, v, int(w))
    return g

print("Enter graph details:")
graph = take_input()
mst_edges, total_cost = graph.minimum_spanning_tree()
print("Minimum Spanning Tree edges using Kruskal's algorithm:")
for edge in mst_edges:
    print(edge)
print("Total cost of Minimum Spanning Tree:", total_cost)


