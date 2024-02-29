import heapq
class Graph:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v, cost):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, cost))
    def astar(self, start, goal, heuristic):
        priority_queue = [(0, start, [])]
        visited = set()
        while priority_queue:
            (current_cost, current_node, path) = heapq.heappop(priority_queue)
            if current_node in visited:
                continue
            path = path + [current_node]
            if current_node == goal:
                return path
            visited.add(current_node)
            for neighbor, cost in self.graph.get(current_node, []):
                if neighbor not in visited:
                    total_cost = current_cost + cost + heuristic(neighbor, goal)
                    heapq.heappush(priority_queue, (total_cost, neighbor, path))
        return None
# Example usage:
if __name__ == "__main__":
    # Create a sample graph
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('D', 'E', 7)
    graph.add_edge('E', 'A', 8)

    # Define a heuristic function (Euclidean distance)
    def heuristic(node, goal):
        heuristic_cost = {
            'A': 10,
            'B': 6,
            'C': 4,
            'D': 2,
            'E': 0
        }
        return heuristic_cost[node]

    # Perform A* from 'A' to 'E'
    result_path = graph.astar('A', 'E', heuristic)

    if result_path:
        print("A* Path:", result_path)
    else:
        print("No path found.")
