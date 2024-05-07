import heapq

def Greedy_Prim(graph):
    Minimum_Spanning_Tree = []
    visited = set()
    start_node = input("Enter Start node: ")
    priority_Q = [(0,start_node,None)]
    
    while priority_Q:
        weight,currentnode ,parent = heapq.heappop(priority_Q)
        if currentnode not in visited:
            visited.add(currentnode)
            Minimum_Spanning_Tree.append((parent,currentnode,weight))
            for neighbor,edge_weight in graph[currentnode].items():
                    if neighbor not in visited:
                        heapq.heappush(priority_Q,(edge_weight, neighbor, currentnode))
    return Minimum_Spanning_Tree
def create_graph():
    graph = {}
    total_egdes = int(input("Enter total edges: "))
    for _ in range(total_egdes):
        start,end,weight = input().split()
        weight = int(weight)
        if start not in graph:
            graph[start] = {}
        if end not in graph:
            graph[end] = {}
        graph[start][end] = weight
        graph[end][start] = weight
    return graph
graph1 = create_graph()
print("Minimum Spanning Tree: ")
result = Greedy_Prim(graph1)
for edge in result:
    print(edge)
