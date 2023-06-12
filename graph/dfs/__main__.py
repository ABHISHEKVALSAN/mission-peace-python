def dfs(graph, start):
    visited = {} # Set to track visited vertices
    stack = [start]  # Stack to store vertices to visit

    while stack:
        current = stack.pop()
        if current not in visited.keys():
            visited[current] = True
            # Process current vertex here (e.g., print or store in a list)

            # Explore neighbors of current vertex
            for neighbor in graph[current]:
                if neighbor not in visited.keys():
                    stack.append(neighbor)

    # Optionally, you can return the visited vertices
    return list(visited.keys())

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Starting vertex for DFS
start_vertex = 'A'

# Perform DFS on the graph
result = dfs(graph, start_vertex)

# Print the visited vertices
print(result)
