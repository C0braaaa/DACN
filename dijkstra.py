import heapq

# Định nghĩa đồ thị bằng danh sách kề
graph = {
    'A': [('B', 2), ('C', 5), ('D', 3)],
    'B': [('A', 2), ('D', 1), ('E', 6)],
    'C': [('A', 5), ('D', 7), ('G', 4)],
    'D': [('A', 3), ('B', 1), ('C', 7), ('E', 2), ('F', 2), ('G', 8)],
    'E': [('B', 6), ('D', 2), ('F', 5)],
    'F': [('D', 2), ('E', 5), ('H', 6)],
    'G': [('C', 4), ('D', 8), ('H', 3)],
    'H': [('F', 6), ('G', 3)]
}

def dijkstra(graph, start):
    # Khởi tạo khoảng cách ban đầu tới tất cả đỉnh là vô cực
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Khoảng cách từ đỉnh nguồn đến chính nó là 0

    # Hàng đợi ưu tiên để chọn đỉnh có khoảng cách nhỏ nhất
    priority_queue = [(0, start)]  # (khoảng cách, đỉnh)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Nếu khoảng cách hiện tại lớn hơn khoảng cách đã ghi nhận, bỏ qua
        if current_distance > distances[current_vertex]:
            continue

        # Xét các đỉnh kề
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            # Nếu tìm được khoảng cách nhỏ hơn, cập nhật lại
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Gọi thuật toán Dijkstra từ đỉnh A
start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)

# In kết quả đường đi ngắn nhất từ A đến tất cả các đỉnh khác
print("Khoảng cách ngắn nhất từ đỉnh", start_vertex, "đến các đỉnh khác:")
for vertex, distance in shortest_distances.items():
    print(f"{start_vertex} -> {vertex}: {distance}")
