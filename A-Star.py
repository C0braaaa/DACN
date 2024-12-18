from queue import PriorityQueue

def a_star_search(data, start, goal):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in data}
    g_score[start] = 0

    while not open_set.empty():
        current_cost, current_node = open_set.get()

        if current_node == goal:
            path = reconstruct_path(came_from, current_node)
            return path, g_score[goal]

        neighbors = data[current_node]
        heuristic = neighbors[-1]
        for i in range(0, len(neighbors) - 1, 2):
            neighbor, cost = neighbors[i], neighbors[i+1]
            tentative_g_score = g_score[current_node] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic
                open_set.put((f_score, neighbor))

    return None, float('inf')

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# Dữ liệu đồ thị
data = {
    'S': ['A', 7, 'B', 3, 6],
    'A': ['C', 2, 'D', 5, 6],
    'B': ['D', 7, 'E', 6, 5],
    'C': ['F', 4, 3],
    'D': ['F', 3, 'G', 6, 2],
    'E': ['G', 2, 2],
    'F': ['H', 5, 1],
    'G': ['H', 1, 0],
    'H': [0]
}

# Thực thi thuật toán
start = 'S'
goal = 'H'
path, cost = a_star_search(data, start, goal)
print(f"Đường đi ngắn nhất: {path} với chi phí: {cost}")
