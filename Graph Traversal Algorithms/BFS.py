from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["E"],
    "D": [],
    "E": []
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []
    
    while queue:
        current = queue.popleft()
        order.append(current)
        print("Visiting:", current)
        
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

print("Final Order", bfs(graph, "A"))