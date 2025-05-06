graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E'],
    'D': [],
    'E': []
}

def dfs(graph, start):
    visited = set()
    stack = [start]
    order = []
    
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            order.append(current)
            
            print("Visiting:", current)
            
            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return order

print("Final order:", dfs(graph, "A"))