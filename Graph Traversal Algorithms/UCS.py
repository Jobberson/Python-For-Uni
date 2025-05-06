import heapq

graph = {
    "A": [("B", 1), ("C", 2)],
    "B": [("D", 1), ("E", 1)],
    "C": [("E", 6)],
    "D": [],
    "E": []
}

def UCS(graph, start, goal):
    visited = set()
    queue = [(0, start)]
    cameFrom = {start: None}
    
    while queue:
        cost, current = heapq.heappop(queue)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = cameFrom[current]
            return path[::-1], cost
        
        if current in visited:
            continue
        
        visited.add(current)
        
        print("Visiting:", current, "with cost:", cost)
        
        for neighbor, edge_cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_cost, neighbor))
                if(neighbor not in cameFrom or cost + edge_cost < queue[0][0]):
                    cameFrom[neighbor] = current
                    
    return None

path, cost = UCS(graph, 'A', 'E')  
print("Path:", path)
print("Total cost:", cost)