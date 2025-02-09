import heapq

class Node:
    def __init__(self, state, cost, parent=None):
        self.state = state
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def ucs(graph, start, goal):
    visited = set()
    priority_queue = []

    start_node = Node(state=start, cost=0)
    heapq.heappush(priority_queue, start_node)

    while priority_queue:
        current_node = heapq.heappop(priority_queue)
                                
        if current_node.state == goal:
            return reconstruct_path(current_node)

        if current_node.state not in visited:
            visited.add(current_node.state)

            for neighbor, cost in graph[current_node.state].items():
                next_node = Node(state=neighbor, cost=current_node.cost + cost, parent=current_node)
                heapq.heappush(priority_queue, next_node)

    return None  # Goal not reachable

def reconstruct_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    return path

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
goal_node = 'D'

result = ucs(graph, start_node, goal_node)

if result:
    print(f"Optimal path from {start_node} to {goal_node}: {result}")
else:
    print(f"No path found from {start_node} to {goal_node}")
