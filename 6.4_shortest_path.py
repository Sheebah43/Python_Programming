# shortest path
import heapq

def dijkstra(graph, start):
    # graph: adjacency list {node: [(neighbor, weight), ...]}
    # start: starting node
    
    # Step 1: Initialize distances
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Step 2: Priority queue (min-heap)
    pq = [(0, start)]  # (distance, node)
    
    while pq:
        current_dist, current_node = heapq.heappop(pq)
        
        # Skip if we already found a shorter path
        if current_dist > distances[current_node]:
            continue
        
        # Step 3: Explore neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            
            # If shorter path found → update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances


if __name__ == "__main__":
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', 2), ('D', 5)],
        'C': [('D', 1)],
        'D': []
    }
    
    print("Shortest paths from A:", dijkstra(graph, 'A'))
