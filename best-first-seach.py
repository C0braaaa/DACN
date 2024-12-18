from queue import PriorityQueue  # Sử dụng PriorityQueue cho hàng đợi ưu tiên.

# Đồ thị được biểu diễn dưới dạng dictionary
# Mỗi đỉnh chứa danh sách các đỉnh kề và giá trị heuristic.
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 5)],
    'D': [('G', 6)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic của mỗi đỉnh đến đích
heuristic = {
    'A': 7,
    'B': 6,
    'C': 5,
    'D': 4,
    'E': 3,
    'F': 6,
    'G': 0
}

# Hàm Best-First Search
def best_first_search(graph, start, goal):
    # Khởi tạo hàng đợi ưu tiên và thêm đỉnh bắt đầu vào.
    open_set = PriorityQueue()
    open_set.put((heuristic[start], start))  # (giá trị heuristic, đỉnh)

    # Lưu vết các đỉnh đã được duyệt để tránh lặp lại.
    closed_set = set()

    # Duyệt các đỉnh trong hàng đợi.
    while not open_set.empty():
        # Lấy đỉnh có giá trị heuristic nhỏ nhất.
        _, current = open_set.get()
        print(f"Đang duyệt đỉnh: {current}")

        # Nếu tìm thấy đỉnh đích, kết thúc tìm kiếm.
        if current == goal:
            print("Tìm kiếm thành công!")
            return

        # Đánh dấu đỉnh hiện tại đã được duyệt.
        closed_set.add(current)

        # Duyệt qua các đỉnh kề của đỉnh hiện tại.
        for neighbor, cost in graph[current]:
            if neighbor not in closed_set:
                open_set.put((heuristic[neighbor], neighbor))

    print("Tìm kiếm thất bại!")

# Gọi hàm Best-First Search để tìm đường từ A đến G.
best_first_search(graph, 'A', 'G')
