from collections import defaultdict, deque

# Function to perform Depth-First Search
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            stack.extend(graph[vertex] - visited)

# Function to perform Breadth-First Search
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            queue.extend(graph[vertex] - visited)

# Function to construct a graph from user input
def construct_graph():
    graph = defaultdict(set)
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v = input("Enter an edge (format: source destination): ").split()
        graph[u].add(v)
        graph[v].add(u)

    return graph

# Main function for menu
def main():
    graph = None
    while True:
        print("\nMenu:")
        print("1. Construct graph")
        print("2. Depth-First Search (DFS)")
        print("3. Breadth-First Search (BFS)")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            graph = construct_graph()
        elif choice == '2':
            if graph is None:
                print("Please construct the graph first.")
            else:
                start_node = input("Enter the starting node for DFS: ")
                print("Depth-First Search:")
                dfs(graph, start_node)
        elif choice == '3':
            if graph is None:
                print("Please construct the graph first.")
            else:
                start_node = input("Enter the starting node for BFS: ")
                print("Breadth-First Search:")
                bfs(graph, start_node)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()








from collections import defaultdict, deque

def dfs_recursive(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=' ')

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def dfs(graph, start):
    visited = set()
    dfs_recursive(graph, start, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            print(vertex, end=' ')
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)


def construct_graph():
    graph = defaultdict(set)
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v = input("Enter an edge (format: source destination): ").split()
        graph[u].add(v)
        graph[v].add(u)

    return graph

def main():
    graph = None
    while True:
        print("\nMenu:")
        print("1. Construct graph")
        print("2. Depth-First Search (DFS)")
        print("3. Breadth-First Search (BFS)")
        print("4. Exit")
       
        choice = input("Enter your choice: ")

        if choice == '1':
            graph = construct_graph()
        elif choice == '2':
            if graph is None:
                print("Please construct the graph first.")
            else:
                start_node = input("Enter the starting node for DFS: ")
                print("Depth-First Search:")
                dfs(graph, start_node)
        elif choice == '3':
            if graph is None:
                print("Please construct the graph first.")
            else:
                start_node = input("Enter the starting node for BFS: ")
                print("Breadth-First Search:")
                bfs(graph, start_node)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()


