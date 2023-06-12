from collections import deque

def bfs(graph, start):
    visited = {}          # Set to track visited vertices
    queue = deque([start])   # Queue to store vertices to visit

    while queue:
        current = queue.popleft()
        if current not in visited.keys():
            visited[current] = True
            # Process current vertex here (e.g., print or store in a list)

            # Explore neighbors of current vertex
            for neighbor in graph[current]:
                if neighbor not in visited.keys():
                    queue.append(neighbor)

    # Optionally, you can return the visited vertices
    return visited.keys()

if __name__=="__main__":
    # Example graph represented as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    # Starting vertex for BFS
    start_vertex = 'A'

    # Perform BFS on the graph
    result = bfs(graph, start_vertex)

    # Print the visited vertices
    print(result)
